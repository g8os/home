# Create a vdisk Boot Image

This tutorials will guide you through the steps to create a vdisk boot image and make it available on a central ARDB-based storage cluster.

As an example we create a vdisk boot image for Ubuntu.16.04.2. With this vdisk boot image you can then boot a virtual machine in a G8OS resource pool, as documented in the tutorial [Boot a Virtual Machine in G8OS Resource Pool](Boot_VM_in_G8OS_Resource_Pool.md).

Steps:
- [Get your environment into shape](#setup-env)
- [Download an OS image](#download-osimage)
- [Get a working NBD server](#nbd-server)
- [Upload the image](#upload-image)

<a id="setup-env"></a>
## Get your environment into shape

The template creation happens from a privileged Ubuntu Docker container connected to the ZeroTier network in which the master ARDB server is present. Before you continue install a JumpScale 8.2 developer environment as described in https://github.com/Jumpscale/developer. This will create the Docker image locally you'll need to continue this tutorial.

Create your Docker container in privileged mode:

```shell
docker run --name image-uploader -it --privileged=true --device=/dev/net/tun --cap-add=NET_ADMIN --cap-add=SYS_ADMIN -v ~/gig/zerotier-one/:/var/lib/zerotier-one/ -v ~/gig/code/:/opt/code/ -v ~/gig/data/:/optvar/data jumpscale/js82 /bin/bash
```

Start the ZeroTier daemon:
```shell
zerotier-one -d
```

Join the ZeroTier network to the master ARDB server:
```shell
zerotier-cli join 93afae596363ade1
```

Once you are ready with this, install the following packages you'll need down the road:
```shell
apt-get update
apt-get install p7zip-full qemu libguestfs-tools kpartx
```

<a id="download-osimage"></a>
## Download an OS image

You can of course create your own image by installing a virtual machine in e.g. [Virtual Box](https://www.virtualbox.org), then take its disk to create a template. But there are already loads of downloadable disk images out there. http://www.osboxes.org for example provides a nice catalog of ready to download virtual machine boot disk images.

We'll continue with an [Ubuntu 16.04.2 image](https://drive.google.com/uc?export=download&confirm=2Ddr&id=0B_HAFnYs6Ur-OG5nLVRuZ3hQQ1U) from osboxes.org.

First create a working directory in your JumpScale Docker container:

```shell
mkdir -p /optvar/data/images
```

The easiest way to download images from osboxes.org is via your normal browser because they store the actual files in google drive. When you download the image make sure you save them in the working directory we created before. This should be easy from your browser because the JumpScale Docker container mounted `/optvar/data` in `~/gig/data` of your user account on your pc.

Then return to your JumpScale shell, and unzip the image you downloaded into your images folder:
```shell
cd /optvar/data/images
7z e Ubuntu_16.04.2-VM-64bit.7z
```

Unzipping the image takes a while, please be patient, once done:
```
ls
64bit  Ubuntu 16.04.2 (64bit).vmdk  Ubuntu_16.04.2-VM-64bit.7z
```

<a id="ndb-server"></a>
## Get a working NDB server

First we need to install Go into the Docker container. JumpScale makes that very easy:

```shell
cd /optvar/data/images
jspython -c "from JumpScale import j; j.tools.cuisine.local.development.golang.install()"
```

Then start the SSH daemon in the container:
```shell
/usr/sbin/sshd
```

For the next step you need to SSH into your container:
```shell
ssh root@IP-address
```

Then follow the [instructions from the NDB server repository](https://github.com/g8os/blockstor#build-for-g8os) on how to build the NDB server:
```
go get -d github.com/g8os/blockstor/nbdserver
cd $GOPATH/src/github.com/g8os/blockstor/nbdserver
CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"' .
```

<a id="upload-image"></a>
## Upload the image

General documentation can be found here: https://github.com/g8os/home/blob/1.1.0-alpha/docs/vms/templatecreation.md

Start with running the NBD server connected to the central ARDB server:
```shell
cd /opt/go/proj/src/github.com/g8os/blockstor/nbdserver
./nbdserver -export osboxes.org:ubuntu.16.04.2 -testardbs 172.30.208.208:26379,172.30.208.208:26379
```

Notice the `osboxes.org:ubuntu.16.04.2` argument, which will be the name of the created template vdisk that we'll need to use to create dynamic clones of this vdisk.

Now before we can upload the image we must make sure its virtual size is below 20 GiB. We can use `qemu-img info` command to inspect some details about the virtual disk:

```shell
cd /optvar/data/images
qemu-img info -f vmdk "Ubuntu 16.04.2 (64bit).vmdk"
image: Ubuntu 16.04.2 (64bit).vmdk
file format: vmdk
virtual size: 100G (107374182400 bytes)
disk size: 3.9G
cluster_size: 65536
Format specific information:
    cid: 3852853794
    parent cid: 4294967295
    create type: monolithicSparse
    extents:
        [0]:
            virtual size: 107374182400
            filename: Ubuntu 16.04.2 (64bit).vmdk
            cluster size: 65536
            format:
```

As you can see our example image has a virtual size of 100 GiB, so we need to shrink it.

First convert the image to raw format so we can mount the image via a loopback device to shrink the partitions:

```shell
qemu-img convert -f vmdk -O raw -p "Ubuntu 16.04.2 (64bit).vmdk" /root/ubuntu.16.04.2.img
```

Let's check the contents of the virtual disk:
```
fdisk -l ubuntu.16.04.2.img
Disk ubuntu.16.04.2.img: 100 GiB, 107374182400 bytes, 209715200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8be26313

Device              Boot     Start       End   Sectors  Size Id Type
ubuntu.16.04.2.img1 *         2048 202909695 202907648 96.8G 83 Linux
ubuntu.16.04.2.img2      202911742 209713151   6801410  3.2G  5 Extended
ubuntu.16.04.2.img5      202911744 209713151   6801408  3.2G 82 Linux swap / Solaris
```

Okay, as it turns out you we have to move around some pieces:
1. Resize the filesystem in the first partition
2. Create a new disk with smaller size and same type of partitions
3. dd all the content from large disk to smaller disk

We start with mounting the OS partition of the disk:
```shell
losetup --offset $[512 * 2048] --sizelimit $[512 * 202907648] /dev/loop0 /root/ubuntu.16.04.2.img
```

Now we can resize the filesystem:
```shell
e2fsck -f /dev/loop0
resize2fs /dev/loop0 10G
losetup -d /dev/loop0
```

Create a new disk:
```shell
truncate -s $[2048*512 + 10*1024*1024*1024 + 209713151*512 - 202911742*512] /root/ubuntu.16.04.2-small.img
```

Now go to work with fdisk to recreate the partition table resembling the original, but with a smaller OS partition (10G):
```shell
fdisk /root/ubuntu.16.04.2-small.img
```

When you are finished, it should look a bit like this:
```shell
fdisk -l ubuntu.16.04.2-small.img
Disk ubuntu.16.04.2-small.img: 13.3 GiB, 14220788224 bytes, 27774977 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x8be26313

Device                    Boot    Start      End  Sectors  Size Id Type
ubuntu.16.04.2-small.img1          2048 20973567 20971520   10G 83 Linux
ubuntu.16.04.2-small.img2      20973568 27774976  6801409  3.2G  5 Extended
ubuntu.16.04.2-small.img5      20975616 27774976  6799361  3.2G 82 Linux swap / Solaris
```

Now copy data from the big disk to the small one:
```shell
dd if=/root/ubuntu.16.04.2.img of=/root/ubuntu.16.04.2-small.img bs=512 count=$[2048 + 10*1024*1024*1024/512]
```

Now you should be done.

Maybe it's interesting to mount the OS partition in the small disk to see if you did not mess up:
```
losetup -D
losetup --offset $[512 * 2048] --sizelimit $[512 * 20973567] /dev/loop0 /root/ubuntu.16.04.2-small.img
cd /mnt
mkdir vmdk
mount -r /dev/loop0 /mnt/vmdk/
cd vmdk
ls -ail
total 124
     2 drwxr-xr-x  24 root root  4096 Apr 29 19:19 .
678111 drwxr-xr-x   1 root root  4096 Apr 29 18:06 ..
 48670 drwxr-xr-x   2 root root  4096 Mar 11 15:02 bin
 49049 drwxr-xr-x   3 root root  4096 Mar 11 15:02 boot
 48830 drwxrwxr-x   2 root root  4096 Mar 11 15:01 cdrom
 49342 drwxr-xr-x   5 root root  4096 Feb 15 20:36 dev
 24445 drwxr-xr-x 130 root root 12288 Mar 11 15:02 etc
131073 drwxr-xr-x   3 root root  4096 Mar 11 15:01 home
    13 lrwxrwxrwx   1 root root    32 Mar 11 15:02 initrd.img -> boot/initrd.img-4.8.0-36-generic
262145 drwxr-xr-x  22 root root  4096 Mar 11 15:02 lib
 49433 drwxr-xr-x   2 root root  4096 Feb 15 20:20 lib64
...
```

Open a new bash on the Docker container to upload the image:
```shell
cd /optvar/data/images
qemu-img convert -f raw -O nbd -n -p /root/ubuntu.16.04.2-small.img nbd+unix:///osboxes.org:ubuntu.16.04.2-copy?socket=/tmp/nbd-socket
```

Now be patient, because you need to push a couple of GiB through the ZeroTier network. In this case it's about 4 GiB.
