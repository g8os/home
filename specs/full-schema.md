# G8OS (G8 Operating System)

# core0
core0 is a replacement for sysvinit/systemd, it provides process management and administration.
This core0 is specialy made for running containers and be easy to administrate.

The default way to manage filesystem is the integrated [flist support](https://github.com/g8os/fs).
Our filesystem engine is build-in on the core0.
You can host a complete operating system with this way (it's used by the containers). You only need the metadata and
not download the full image, files are downloaded on-demand, which speed up dramaticaly the startup process.

The client (and core0) integrate some default management like:
 - Network management (bridge, etc.)
 - Disks management (partitions, ...)
 - [ZeroTier](https://github.com/zerotier/ZeroTierOne) default network integration
 - [IPFS](https://github.com/ipfs/ipfs) support integration

# 0-Initramfs
To start the core0, we currently bundle it in an 0-Initramfs.
The full details about 0-Initramfs can be found on [the dedicated repository](https://github.com/zero-os/0-initramfs)

## Why bundle it ?
We build an 0-Initramfs which is bundled with the kernel.
This allow us to sign the kernel one time and make sur that it cannot be altered or replaced on our SecureBoot environment.

## Content
0-Initramfs contains:
- `busybox` (mostly full)
- `core0`
- `ipfs` (integrated with core0)
- `fuse` userland tools
- `ca-certificates` for some ssl support
- `redis-server` used as communication backend
- `iproute2` utilities
- `nftables` as firewall
- `dnsmasq` for default network management
- `zerotier one`
- `btrfs` utilities
- `parted` for partition management


## Bootstrap
When the kernel start in the 0-Initramfs, the `/init` script is executed.
This script populate `/dev`, `/proc` and `/sys` and prepare a ramdisk where to boot after.

This is probably not _absolutly_ needed but leaving the 0-Initramfs is always a good idea.
In this case, we switch to another ramfs but this can be changed easily.

# Booting the kernel
When you boot the kernel, theses step are achieved:
- **Preparing the root ramfs**: initializing a default ramfs whith all the needed files
- **Launching the core0**:
  - **Starting services**:
    - Logs
    - IPFS Daemon
    - Network
    - Redis
- **Waiting input from redis**: use the client to communicate

# Create a container
You can easily create a container when the core0 is up, from the [python client](https://github.com/zero-os/0-core/tree/master/pyclient)
`cl.container.create('Address of the root filesystem metadata')`
