![ZeroOS console](g8os.png)

ZeroOS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

For more details see the [Introduction to ZeroOS](/docs/README.md) in the [`/docs`](/docs) documentation directory, which includes a comprehensive [table of contents](/docs/SUMMARY.md).

# Requirements

All documentation has been tested using **v8.2.0rc1** [jumpscale_core8](https://github.com/Jumpscale/jumpscale_core8/tree/v8.2.0rc1) and **v1.1.0-alpha-2** of [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2) and [ZeroOS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)


# Main repositories

- [0-Initramfs Builder](https://github.com/zero-os/0-initramfs):
  - Assembly of shell scripts for building the ZeroOS Linux kernel and create an initramfs to start 0-Core.
- [0-Core](https://github.com/zero-os/0-core):
  - Init process (0-Core) and container manager (CoreX) of ZeroOS
  - Also contains Python client for 0-Core, for managing containers, disks and networking of a ZeroOS node
- [0-FS](https://github.com/zero-os/0-fs):
  - Virtual file system for ZeroOS and ZeroOS containers
- [ZeroOS Block Storage](https://github.com/zero-os/0-disk):
  - NBD based distributed block storage server
- [ZeroOS Rest API](https://github.com/zero-os/0-rest-api):
  - ZeroOS resource pool API server and AYS templates
  - Also contains RAML definition and Python stubs to interact with the RESTfull resource pool API
- [ZeroOS Hub](https://github.com/g8os/hub):
  - Repository for flists and vdisk templates
  - Publicly hosted on https://hub.gig.tech

# Release schedule

- Dec 7, 2016: [v0.9.0](https://github.com/zero-os/0-core/releases/tag/v0.9.0)
  - First usable beta version of the ZeroOS
- May 12, 2017: **v1.1.0-alpha-2**: [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2), [ZeroOS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)
  - Introduces
    - Hub
    - Rest API (with **v8.2.0rc1** of [jumpscale_core8](https://github.com/Jumpscale/jumpscale_core8/tree/v8.2.0rc1))
    - NBD Block Storage server
  - [Kanban](https://waffle.io/g8os/home?milestone=1.1.0-alpha-2)
- June 2, 2017: [v1.1.0-alpha-3](https://github.com/g8os/home/blob/master/milestones/1.1.0-alpha-3.md)
  - Introduces
    - Basic integration with OpenvCloud
    - ZeroOS Gateway
    - Upgrade of service to JumpScale 9
  - [Kanban](https://waffle.io/g8os/home?milestone=1.1.0-alpha-3)
- June 17, 2017: [v1.1.0-alpha-4](https://github.com/g8os/home/blob/master/milestones/1.1.0-alpha-4.md)
  - Introduces:
    - Redundant vdisks
    - vdisk rollback
    - Automatic handling of storage failures
    - All components accessed only over tls and authenticated over ItsYou.online
  - [Kanban](https://waffle.io/g8os/home?milestone=1.1.0-alpha-4)

# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
