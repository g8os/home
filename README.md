![Zero-OS console](g8os.png)

Zero-OS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

For more details see the [Introduction to Zero-OS](/docs/README.md) in the [`/docs`](/docs) documentation directory, which includes a comprehensive [table of contents](/docs/SUMMARY.md).

# Requirements

All documentation has been tested using **v8.2.0rc1** [jumpscale_core8](https://github.com/Jumpscale/jumpscale_core8/tree/v8.2.0rc1) and **v1.1.0-alpha-2** of [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2) and [Zero-OS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)


# Main repositories

- [0-initramfs](https://github.com/zero-os/0-initramfs):
  - Assembly of shell scripts for building the Zero-OS Linux kernel and create an initramfs to start 0-Core.
- [0-core](https://github.com/zero-os/0-core):
  - Init process (0-Core) and container manager (CoreX) of Zero-OS
  - Also contains Python client for 0-Core, for managing containers, disks and networking of a Zero-OS node
- [0-fs](https://github.com/zero-os/0-fs):
  - File system for Zero-OS and Zero-OS containers
- [0-Disk](https://github.com/zero-os/0-disk):
  - Zero-OS Block Storage: NBD based distributed block storage server
- [0-orchestrator](https://github.com/zero-os/0-orchestrator):
  - Restful API server and AYS templates for managing a Zero-OS cluster
  - Also contains RAML definition and Python stubs to interact with the RESTful API
- [0-Hub](https://github.com/zero-os/0-hub):
  - Repository for flists and vdisk templates
  - Publicly hosted on https://hub.gig.tech

# Release schedule

- Dec 7, 2016: [v0.9.0](https://github.com/zero-os/0-core/releases/tag/v0.9.0)
  - First usable beta version of the Zero-OS
- May 12, 2017: **v1.1.0-alpha-2**: [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2), [Zero-OS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)
  - Introduces
    - Hub
    - Rest API (with **v8.2.0rc1** of [jumpscale_core8](https://github.com/Jumpscale/jumpscale_core8/tree/v8.2.0rc1))
    - NBD Block Storage server
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-2)
- June 6, 2017: **[v1.1.0-alpha-3](release_notes/1.1.0-alpha-3.md)** : [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-3), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-3), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-3), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/releases/tag/v1.1.0-alpha-3)
  - Introduces
    - Basic integration with OpenvCloud
    - Zero-OS Gateway
    - Upgrade of service to JumpScale 9
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-3)
- June 16, 2017: **[v1.1.0-alpha-4](release_notes/1.1.0-alpha-4.md)** [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-4), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-4), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-4), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-4)
  - Introduces:
    - Redundant vdisks
    - vdisk rollback
    - All components accessed only over tls and authenticated over ItsYou.online
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-4)
- July 7, 2017: [v1.1.0-alpha-5](milestones/1.1.0-alpha-5.md)
  - Introduces:
    - OpenvCloud on top of Jumpscale9
    - Statistics gathering and grafana dashboards
    - Persistent zerotier ips for zero-os and containers
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-5)
- July 14, 2017: [v1.1.0-alpha-6](milestones/1.1.0-alpha-6.md)
  - Introduces:
    - OpenvCloud
       - Statitics
       - Rollback
       - clone
       - template
    - Self-healing
      - Storage failure recovery
      - auto restart of VM and containers
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-5)


# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
