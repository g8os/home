# Introduction to Zero-OS

Zero-OS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

- Zero-OS is stateless by not needing any locally stored data, not even Zero-OS system files
- Zero-OS is lightweight by only containing the components required to securely run and manage containers and virtual machines

See [ Getting Started with Zero-OS](gettingstarted/gettingstarted.md) for the recommended path to quickly get up and running with Zero-OS.

Key components:

- [0-Initramfs Builder](#0-initramfs)
- [0-Core](#0-core)
- [0-FS](#0-fs)
- [Hub](#hub)
- [Rest API](#resourcepool)
- [0-Disk](#blockstorage)

> All documentation has been tested using **v8.2.0rc1** [jumpscale_core8](https://github.com/Jumpscale/jumpscale_core8/tree/v8.2.0rc1) and **v1.1.0-alpha-2** of [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2) and [Zero-OS Rest API](https://github.com/zero-OS/0-disk/releases/tag/v1.1.0-alpha-2)

<a id="0-core"></a>
## 0-Initramfs Builder

0-Initramfs Builder is an assembly of shell scripts for building the Zero-OS Linux kernel and create an 0-initramfs to start 0-Core.

- GitHub repository: [g8os/hub](https://github.com/zero-os/0-initramfs)
- Documentation: [0-Initramfs Documentation](https://github.com/zero-os/0-initramfs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with 0-Initramfs](https://github.com/zero-os/0-initramfs/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="0-core"></a>
## 0-Core

0-Core is the Zero-OS replacement for systemd, the init system to bootstrap the user space and manage all processes subsequently.

Interacting with 0-Core is done by sending commands through a Redis, allowing you to manage disks, set-up networks and create containers and start virtual machines.

- GitHub repository: [g8os/hub](https://github.com/zero-os/0-core)
- Documentation: [0-Core Documentation](https://github.com/zero-os/0-core/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with 0-Core](https://github.com/zero-os/0-core/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="0-fs"></a>
## 0-FS

 is the Zero-OS file system used in containers, which is actually a FUSE file system. Mounting the  is done by using a flist, which is a relatively small RocksDB database file, containing the metadata of the actual files and directories. On accessing a file Zero-OS fetches the required file chunks from a remote store, and caches it locally. This remote store is the Zero-OS Hub, discussed here below.

- GitHub repository: [g8os/hub](https://github.com/g8os/hub)
- Documentation: [ Documentation](https://github.com/zero-os/0-fs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with ](https://github.com/zero-os/0-fs/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="hub"></a>
## Hub

The Zero-OS Hub is where all container images and and vdisk boot images are stored.

- GitHub repository: [g8os/hub](https://github.com/g8os/hub)
- Documentation: [Hub Documentation](https://github.com/g8os/hub/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with the Zero-OS Hub](https://github.com/g8os/hub/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="resourcepool"></a>
## Rest API

A resource pool is a cluster of Zero-OS nodes, sharing compute and storage capacity.

- GitHub repository: [zero-os/0-rest-api](https://github.com/zero-OS/0-disk)
- Documentation: [Rest API Documentation](https://github.com/zero-OS/0-disk/blob/master/docs/SUMMARY.md)
- Getting Started: [Getting Started with Zero-OS Rest API](https://github.com/zero-OS/0-disk/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="blockstorage"></a>
## 0-Disk

Zero-OS 0-Disk is about the components that allow to create and use block devices (vdisks) from within virtual machines hosted on a Zero-OS node.

- GitHub repository: [zero-os/0-disk](https://github.com/zero-os/0-disk)
- Documentation: [0-Disk Documentation](https://github.com/zero-os/0-disk/blob/master/docs/SUMMARY.md)
- Getting Started: [Getting Started with NBD Server](https://github.com/zero-os/0-disk/blob/master/docs/gettingstarted/gettingstarted.md)
