![Zero-OS console](g8os.png)

Zero-OS is a stateless and lightweight Linux operating system designed for clustered deployments to host virtual machines and containerized applications.

For more details see the [Introduction to Zero-OS](/docs/README.md) in the [`/docs`](/docs) documentation directory, which includes a comprehensive [table of contents](/docs/SUMMARY.md).

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
- October 11, 2017: **[1.1.0-alpha-8](release_notes/1.1.0-alpha-8.md)**:
[0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-8), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-8), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-8), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-8), [Zero-os 0-Disk](https://github.com/zero-os/0-disk/tree/1.1.0-alpha-8)

- August 09, 2017: This release is a combinaison of the milestone **[1.1.0-alpha-6 and 1.1.0-alpha-7](release_notes/1.1.0-alpha-7.md)**:
[0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-7), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-7), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-7), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-7)

- July 7, 2017: **[v1.1.0-alpha-5](release_notes/1.1.0-alpha-5.md)**:
[0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-5), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-5), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-5), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-5)

- June 16, 2017: **[v1.1.0-alpha-4](release_notes/1.1.0-alpha-4.md)**: [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/tree/1.1.0-alpha-4), [0-Core](https://github.com/zero-os/0-core/tree/1.1.0-alpha-4), [0-FS](https://github.com/zero-os/0-fs/tree/1.1.0-alpha-4), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/tree/1.1.0-alpha-4)
  - Introduces: Redundant vDisks, vDisk rollback, Security
- June 6, 2017: **[v1.1.0-alpha-3](release_notes/1.1.0-alpha-3.md)** : [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-3), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-3), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-3), [Zero-OS Orchestrator](https://github.com/zero-os/0-orchestrator/releases/tag/v1.1.0-alpha-3)
  - Introduces: Basic integration with OpenvCloud, Zero-OS Gateway, JumpScale 9
- May 12, 2017: **v1.1.0-alpha-2**: [0-Initramfs Builder](https://github.com/zero-os/0-initramfs/releases/tag/v1.1.0-alpha-2), [0-Core](https://github.com/zero-os/0-core/releases/tag/v1.1.0-alpha-2), [0-FS](https://github.com/zero-os/0-fs/releases/tag/v1.1.0-alpha-2), [Zero-OS Rest API](https://github.com/zero-os/0-rest-api/releases/tag/v1.1.0-alpha-2)
  - Introduces: Hub, Rest API, 0-disk
- Dec 7, 2016: [v0.9.0](https://github.com/zero-os/0-core/releases/tag/v0.9.0)
  - First usable beta version of the Zero-OS

# Release schedule
- Novembre 20, 2017 (code complete) November 27, 2017 (release): [v1.1.0-beta-1](milestones/1.1.0-beta-1.md)
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
      - self-healing
      - Fix remaining FR's and bugs
      - AYS template support for Gateway API's on OpenvCloud
  - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-beta-1)

# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
