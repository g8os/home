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

# Previous releases
- June 16, 2017: **[v1.1.0-alpha-4](release_notes/1.1.0-alpha-4.md)** [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-4), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-4), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-4), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-4)
  - Introduces: Redundant vDisks, vDisk rollback, Security
- June 6, 2017: **[v1.1.0-alpha-3](release_notes/1.1.0-alpha-3.md)** : [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-3), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-3), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-3), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/releases/tag/v1.1.0-alpha-3)
  - Introduces: Basic integration with OpenvCloud, Zero-OS Gateway, JumpScale 9
- May 12, 2017: **v1.1.0-alpha-2**: [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2), [Zero-OS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)
  - Introduces: Hub, Rest API, 0-disk
- Dec 7, 2016: [v0.9.0](https://github.com/zero-os/0-core/releases/tag/v0.9.0)
  - First usable beta version of the Zero-OS

# Release schedule
- July 7, 2017: [v1.1.0-alpha-5](milestones/1.1.0-alpha-5.md)
  - Introduces:
    - OpenvCloud on top of Jumpscale9
    - Statistics gathering and grafana dashboards
    - Persistent zerotier ips for zero-os and containers
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-5)
- July 14, 2017 (code complete) July 19, 2017 (release): [v1.1.0-alpha-6](milestones/1.1.0-alpha-6.md)
  - Introduces:
    - OpenvCloud
       - Statistics
       - Rollback
    - 0-orchestrator
      - Health check and self healing infrastructure
      - Statistics API
    - 0-disk
      - Storage failure support
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-6)
- July 21, 2017 (code complete) July 26, 2017 (release): [v1.1.0-alpha-7](milestones/1.1.0-alpha-7.md)
  - Introduces:
    - OpenvCloud
      - Statistics
      - Rollback
      - Health checks
    - 0-orchestrator
      - Health checks and Self healing Part one
    - 0-disk
      - Storage failure support
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-7)
- July 28, 2017 (code complete) August 2, 2017 (release): [v1.1.0-alpha-8](milestones/1.1.0-alpha-8.md)
  - Introduces:
    - OpenvCloud
       - Gateway API's on cloudspace
    - 0-orchestrator
      - Health checks and Self healing Part two
    - 0-disk
      - Statistics
      - Tlog storage failures
      - Deduped referencing
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-alpha-8)
- August 11, 2017 (code complete) August 18, 2017 (release): [v1.1.0-beta-1](milestones/1.1.0-beta-1.md)
  - Introduces:
    - OpenvCloud
       - Clone, Template
       - Import / Export
    - 0-orchestration
     - Self healing
       - Health checks and Self healing Part three
     - Publish template to hub
     - Storage statistics
     - Node reboot support
    - 0-disk
     - Fix remaining FR's and bugs
    - AYS template support for Gateway API's on OpenvCloud
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-beta-1)

# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
