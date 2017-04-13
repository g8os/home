# Booting G8OS on a VM using QEMU

```bash
qemu-system-x86_64 -kernel g8os-kernel.efi \
   -m 2048 -enable-kvm -cpu host \
   -net nic,model=e1000 -net bridge,br=lxc0 \
   -drive file=vda.qcow2,if=virtio \
   -drive file=vdb.qcow2,if=virtio \
   -drive file=vdc.qcow2,if=virtio \
   -drive file=vdd.qcow2,if=virtio \
   -drive file=vde.qcow2,if=virtio \
   -nodefaults -nographic \
   -serial null -serial mon:stdio \
   -append 'ays=localhost:5000'
```
