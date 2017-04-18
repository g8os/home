# Booting G8OS on QEMU

Steps:

- [Build a G8OS boot image](#build-image)
- [Create a G8OS disks](#create-disks)
- [Create a new virtual machine on QEMU](#create-vm)
- [Create a port forward from the VM to your host to expose the Redis of the core0](#create-portforward)
- [Start the virtual machine](#start-vm)
- [Ping the core0](#ping-core0)


<a id="build-image"></a>
## Get G8OS kernel

Either build it yourself see [Building your G8OS Boot Image](building/building.md).
We only require the kernel (`staging/vmlinuz.efi`) file when booting with QEMU.
Or download it from the [bootstap server](https://bootstrap.gig.tech/)


## Add support for nesting kvm (running a virtual machine inside a virtual machine)

### Add runtime

```shell
sudo modprobe -r kvm_intel
sudo modprobe kvm_intel nesting=1
```

### Persistantly after reboot
Alter `/etc/default/grub.conf`
in ths line `GRUB_CMDLINE_LINUX_DEFAULT` add `kvm-intel.nesting=1` at the end and run
```
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

<a id="create-disks"></a>
## Create G8OS disks

To be able to provide storage for our ardbs and our container's cache we need to create atleast 5 disks.

```shell
qemu-img create -f qcow2 vda.qcow2 10G
qemu-img create -f qcow2 vdb.qcow2 10G
qemu-img create -f qcow2 vdc.qcow2 10G
qemu-img create -f qcow2 vdd.qcow2 10G
qemu-img create -f qcow2 vde.qcow2 10G
```

Note:
Run this at any time if you want to wipe your disks (erase the content).

<a id="create-vm"></a>
## Create a new virtual machine on QEMU

First we need to have a bridge you can put your management interface in typicly you can usr `virbr0`.
If you do not have `virbr0` you can get it by installing `libvirt-bin` and enabling the default net work `virsh net enable deault`.


### Making overlay
For development mode we can create a small overlay device which overwrites the files inside g8os. See [Hot Debug](https://github.com/g8os/initramfs/tree/1.1.0-alpha#hot-debug-inject-files-without-rebuilding-the-vmlinuz) for detailed instructions.

In this overlay fs we can overwrite files comming from the initramfs for example `bin/core0` and `bin/coreX`

```shell
mkdir -p overlay
touch overlay/.g8os-debug
```

### Overwriting core0 and coreX

In your core0 repo run `make` and copy the binaries to the overlay
```shell
mkdir -p overlay/bin
cp $GOPATH/src/github.com/g8os/core0/bin/* overlay/bin/
```

### Adding shell at boot

If you want a shell to launch at startup of your g8os add the following file at `overlay/etc/g8os/conf/ashlogin.toml`

```toml
[startup.ashlogin]
name = "bash"

[startup.ashlogin.args]
script = """
# Start shell at serial 0
while true; do
getty -l /bin/ash -n 19200 ttyS0
done
"""
```


### Starting the Virtual Machine

```shell
qemu-system-x86_64 -kernel staging/vmlinuz.efi \
    -m 2048 -enable-kvm -cpu host \
    -net nic,model=e1000 -net bridge,br=virbr0 \
    -nodefaults -nographic \
    -serial mon:stdio \
    -drive file=fat:overlay,format=raw \
    -drive file=vda.qcow2,if=virtio -drive file=vdb.qcow2,if=virtio \
    -drive file=vdc.qcow2,if=virtio -drive file=vdd.qcow2,if=virtio \
    -drive file=vde.qcow2,if=virtio
```

This will launch a shell into the g8os, execute `ip a` to know the ipaddress.

<a id="ping-core0"></a>
## Ping the core0

Using the Python client:

```python
import g8core
cl = g8core.Client('{host-ip-address}', port=6379, password='')
cl.ping()
```
