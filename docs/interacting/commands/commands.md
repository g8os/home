# Commands

## Core0

Core0 is the first process to start on bare metal. It works as a simple process manager.

When started it first configures the networking, and then starts a local Redis instance to dispatch commands to the CoreX cores.

## Command structure

```javascript
{
	"id": "command-id",
	"command": "command-name",
	"arguments": {},
	"queue": "optional-queue",
	"stats_interval": 0,
	"max_time": 0,
	"max_restart": 0,
	"recurring_period": 0,
	"log_levels": [int]
}
```

The `Core0` core understands a very specific set of commands:


- [Core commands](core.md)
- [Info commands](info.md)
- [CoreX commands](corex.md)
- [Bridge commands](bridge.md)
- [Disk commands](disk.md)
- [Btrfs commands](btrfs.md)
- [ZeroTier commands](zerotier.md)
- [KVM commands](kvm.md)
- [Job Commands](job.md)
- [Process Commands](process.md)
- [Filesystem Commands](filesystem.md)
