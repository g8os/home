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


# Release schedule
- previous releases see [Previous Releases](Previous Releases.md)
- November 27, 2017 (release): [v1.1.0-beta-1](milestones/1.1.0-beta-1.md)
  - NEED TO CLEANUP in relation to beta2,3,4 : lots of things need to be moved
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
- Dec 2017: beta 2
    -  [v1.1.0-beta-2](milestones/1.1.0-beta-2.md)
    - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-beta-2)
- Jan 2018: beta 3
    -  [v1.1.0-beta-3](milestones/1.1.0-beta-3.md)
    - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-beta-2)    
- Q1 2018: beta 4
    - [v1.1.0-beta-4](milestones/1.1.0-beta-4.md)
    - [Kanban](https://waffle.io/Zero-OS/home?milestone=1.1.0-beta-4)


# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
