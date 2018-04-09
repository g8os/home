# Introduction to Zero-OS

Zero-OS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

- Zero-OS is stateless by not needing any locally stored data, not even Zero-OS system files
- Zero-OS is lightweight by only containing the components required to securely run and manage containers and virtual machines

See [Getting Started with Zero-OS](gettingstarted/gettingstarted.md) for the recommended path to quickly get up and running with Zero-OS.

Key components:

- [0-Initramfs](#0-initramfs)
- [0-Core](#0-core)
- [0-FS](#0-fs)
- [0-Hub](#0-hub)


<a id="0-initramfs"></a>
## 0-initramfs

0-Initramfs is an assembly of shell scripts for building the Zero-OS Linux kernel and create an 0-initramfs to start 0-Core.

- GitHub repository: [zero-os/0-initramfs](https://github.com/zero-os/0-initramfs)
- Documentation: [0-Initramfs Documentation](https://github.com/zero-os/0-initramfs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with 0-Initramfs](https://github.com/zero-os/0-initramfs/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="0-core"></a>
## 0-core

0-core is the Zero-OS init process. It is used to bootstrap the user space and manage all processes subsequently.

Interacting with 0-Core is done by sending commands through a Redis, allowing you to manage disks, set-up networks and create containers and start virtual machines.

- GitHub repository: [zero-os/0-core](https://github.com/zero-os/0-core)
- Documentation: [0-Core Documentation](https://github.com/zero-os/0-core/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with 0-Core](https://github.com/zero-os/0-core/blob/master/docs/gettingstarted/README.md)

<a id="0-fs"></a>
## 0-fs

Zero-OS File System is the file system used in containers and VM boot disk, which is actually a FUSE file system. Mounting the filesystem is done by using a flist, which is a relatively small RocksDB database file, containing the metadata of the actual files and directories. On accessing a file Zero-OS fetches the required file chunks from a remote store, and caches it locally. This remote store is the Zero-OS Hub, discussed here below.

- GitHub repository: [zero-os/0-fs](https://github.com/zero-os/0-fs)
- Documentation: [ Documentation](https://github.com/zero-os/0-fs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with 0-fs](https://github.com/zero-os/0-fs/blob/master/docs/gettingstarted/README.md)

<a id="0-hub"></a>
## 0-hub

The Zero-OS Hub is where all container images and and vdisk boot images are stored.

- GitHub repository: [zero-os/0-hub](https://github.com/zero-os/0-hub)
- Documentation: [Hub Documentation](https://github.com/zero-os/0-hub/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with the Zero-OS Hub](https://github.com/zero-os/0-hub/blob/master/docs/gettingstarted/README.md)

<a id="0-robot"></a>
## 0-robot

The 0-robot is a distributed life cycle management system. It is in the robot that the state of the applications running on 0-os is stored.
When booting 0-os, a 0-robot will be started automatically on the machine.

- GitHub repository: [zero-os/0-robot](https://github.com/zero-os/0-robot)
- Documentation: [0-robot documenation](https://github.com/zero-os/0-robot/blob/master/docs)
- Getting started: [Getting Started with the Zero-OS Hub](https://github.com/zero-os/0-robot/blob/master/docs/getting_started.md)