# G8OS Introduction

G8OS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

- G8OS is stateless by not needing any locally stored data, not even G8OS system files
- G8OS is lightweight by only containing the components required to securely run and manage containers and virtual machines

See [ Getting Started with G8OS](gettingstarted/gettingstarted.md) for the recommended path to quickly get up and running with G8OS.

Key components:

- [Initramfs Builder](#initramfs)
- [Core0](#core0)
- [G8ufs](#g8ufs)
- [Hub](#hub)
- [Resource Pool](#resourcepool)
- [Block Storage](#blockresource)

<a id="core0"></a>
## Initramfs Builder

Initramfs Builder is an assembly of shell scripts for building the G8OS Linux kernel and create an initramfs to start Core0.

- GitHub repository: [g8os/hub](https://github.com/g8os/initramfs)
- Documentation: [Initramfs Documentation](https://github.com/g8os/initramfs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with Initramfs](https://github.com/g8os/initramfs/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="core0"></a>
## Core0

Core0 is the G8OS replacement for systemd, the init system to bootstrap the user space and manage all processes subsequently.

Interacting with Core0 is done by sending commands through a Redis, allowing you to manage disks, set-up networks and create containers and start virtual machines.

- GitHub repository: [g8os/hub](https://github.com/g8os/core0)
- Documentation: [Core0 Documentation](https://github.com/g8os/core0/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with Core0](https://github.com/g8os/core0/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="g8ufs"></a>
## G8ufs

G8ufs is the G8OS file system used in containers, which is actually a FUSE file system. Mounting the G8ufs is done by using a flist, which is a relatively small RocksDB database file, containing the metadata of the actual files and directories. On accessing a file G8OS fetches the required file chunks from a remote store, and caches it locally. This remote store is the G8OS Hub, discussed here below.

- GitHub repository: [g8os/hub](https://github.com/g8os/hub)
- Documentation: [G8ufs Documentation](https://github.com/g8os/g8ufs/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with G8ufs](https://github.com/g8os/g8ufs/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="hub"></a>
## Hub

The G8OS Hub is where all container images and and vdisk boot images are stored.

- GitHub repository: [g8os/hub](https://github.com/g8os/hub)
- Documentation: [Hub Documentation](https://github.com/g8os/hub/blob/master/docs/SUMMARY.md)
- Getting started: [Getting Started with the G8OS Hub](https://github.com/g8os/hub/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="resourcepool"></a>
## Resource Pool

A resource pool is a cluster of G8OS nodes, sharing compute and storage capacity.

- GitHub repository: [g8os/resourcepool](https://github.com/g8os/resourcepool)
- Documentation: [Resource Pool Documentation](https://github.com/g8os/resourcepool/blob/master/docs/SUMMARY.md)
- Getting Started: [Getting Started with G8OS Resource Pool](https://github.com/g8os/resourcepool/blob/master/docs/gettingstarted/gettingstarted.md)

<a id="blockstorage"></a>
## Block Storage

G8OS Block Storage is about the components that allow to create and use block devices (vdisks) from within virtual machines hosted on a G8OS node.

- GitHub repository: [g8os/resourcepool](https://github.com/g8os/blockstor)
- Documentation: [Block Storage Documentation](https://github.com/g8os/blockstor/blob/master/docs/SUMMARY.md)
- Getting Started: [Getting Started with NBD Server](https://github.com/g8os/blockstor/blob/master/docs/gettingstarted/gettingstarted.md)
