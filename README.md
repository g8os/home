![G8OS console](g8os.png)

# Documentation

todo: Create documentation outline

# Main repositories

- [builders for G8OS initramfs](https://github.com/g8os/initramfs) (build instructions & scripts)
- [g8os core](https://github.com/g8os/core0) (Init process and container manager of G8OS)
  - also contains python client for core0. It allows to manage containers, disks and networking of the G8OS
- [g8os fs](https://github.com/g8os/g8ufs) (Virtual filesystem for G8OS and G8OS containers)
- [g8os blockstorage](https://github.com/g8os/blockstor) (Virtual NBD based disk distributed driver)
- [g8os resourcepool](https://github.com/g8os/resourcepool) (G8OS resourcepool api server and ays templates)
  - also contains raml definition and python stubs to interact with the RESTfull resourcepool api.
- [g8os hub](https://github.com/g8os/hub) (Repository for flists and vdisk templates)
  - publically hosted on https://hub.gig.tech

# Release schedule

 - Dec 7, 2016: [v0.9.0](https://github.com/g8os/core0/releases/tag/v0.9.0)
   - First usable beta version of the G8OS.
 - May 12, 2017: [v1.1.0-alpha-2](https://github.com/g8os/home/blob/master/milestones/1.1.0-alpha-2.md) :
   - Introduces
     - hub
     - resourcepool
     - nbd blockstorage server.
 - May 26, 2017: [v1.1.0-alpha-3](https://github.com/g8os/home/blob/master/milestones/1.1.0-alpha-3.md)
   - Introduces
     - G8OS Gateway
     - redundant vdisks
     - upgrade of service to JumpScale 9
 - June 9, 2017: [v1.1.0-alpha-4](https://github.com/g8os/home/blob/master/milestones/1.1.0-alpha-4.md)
   - Basic integration with OpenvCloud
   - vdisk rollback
   - automatic handling of storage failures and all components authenticated over itsyou.online

# Telegram

- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
