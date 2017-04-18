# Bootstrap

We prodive some tools to starts quickly and easily our « always-up-to-date » build.

# Bootstrap repository

Checkout our bootstrap's home page: [bootstrap.gig.tech](https://bootstrap.gig.tech)

## Frontpage
On the frontpage, you will see a list of available kernels.

Kernels pointed by `latest-release` are symlink to the most recent kernel branches.

All the kernels follow the `g8os-BRANCH-COMMIT.efi` notation, symlink point to the most recent `BRANCH` kernel available.

## Services

The bootstrap service can prodive you different autobuilt files to boot a kernel very easily

### ISO

You can request an ISO file (~2MB) which contains a bootable iPXE service which will download the requested kernel.

To generate an ISO, just follow this url: `https://bootstrap.gig.tech/iso/BRANCH/ZEROTIER-NETWORK`

For exemple, to use `1.1.0-alpha` latest image, with earth's zerotier network: `https://bootstrap.gig.tech/iso/1.1.0-alpha/8056c2e21c000001`

Of course, you can specify a more precise branch (like for debug purpose), according to available files on the bootstrap, exemple: `https://bootstrap.gig.tech/iso/1.1.0-alpha-changeloglevel-initramfs-035dd483/8056c2e21c000001`

### USB

Like ISO file, you can download an USB Image that you can clone on an USB Stick: `https://bootstrap.gig.tech/usb/BRANCH/ZEROTIER-NETWORK`

### iPXE Script

Like ISO and USB, you can request a iPXE script using: `https://bootstrap.gig.tech/ipxe/BRANCH/ZEROTIER-NETWORK`

This is the most low level you can grab, scripts embeded on ISO and USB images are the same as the script you can generate this way.
This is useful when you want to boot a machine and can give a iPXE script (like `packet.net` or `OVH` server).


# Autobuild

An autobuild server is in place to automatically rebuild kernel with last version of our github's repository.

You can see the build status here: [build.gig.tech/monitor/](https://build.gig.tech/monitor/)

## How to use it

This works for the following repositories:
- g8os/core0
- g8os/g8ufs
- g8os/initramfs

When you commit to this repositories, an auto-build action is triggered and a new kernel is produced (available on the bootstrap).

## Convention

Each time a push is received on github, a build request is called. In order to have a correct build, you need some advice:
- If you push to `g8os/initramfs`, a complete image will be rebuilt, which can take up to 1 hour.
- If you push to `g8os/core0` or `g8os/g8ufs`, only this step will be recompiled, which takes **about 3 minutes**.

In order to have a **3 minutes** compilation time for cores, the build process use a pre-compiled `initramfs` image (called `baseimage`).
If no baseimage are found, the build will be ignored.

### Base Image and branches

When you push to `initramfs`, a base image will be produced automatically at the end of the build.
This base image will be tagged with the branch name.

Eg: if you push to `1.1.0-alpha`, the base image will be called `1.1.0-alpha`

When you push to `core0` or `g8ufs`, a base image will be lookup before compiling. This match is made by comparing branch-prefix.

Eg: core0 branch `1.1.0-alpha-issue-155` will match base image `1.1.0-alpha`, you **NEED** to prefix your branch with an existing base image.
In theory, all initramfs existing branch should have it's own base image.
