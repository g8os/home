# Disk Commands

Available commands:

- [disk.list](#list)
- [disk.mktable](#mktable)
- [disk.mkpart](#mkpart)
- [disk.getinfo](#getinfo)
- [disk.rmpart](#rmpart)
- [disk.mount](#mount)
- [disk.umount](#umount)


<a id="list"></a>
## disk.list

Lists all available block devices, similar to the `lsblk` command. It takes no arguments.


<a id="mktable"></a>
## disk.mktable

Creates a new partition table on block device.

Arguments:
```javascript
{
    "disk": "{disk}",
    "table_type": "{table_type}",
}
```

Values:
- **disk**: Full device path like `/dev/sda`
- **table_type**: Any value that is supported by `parted mktable`


<a id="mkpart"></a>
## disk.mkpart

Creates a partition on a given device.

Arguments:
```javascript
{
    "disk": "{disk}",
    "part_type": "{part-type}",
}
```

Values:
- **disk**: Full device path like `/dev/sda`.
- **part-type**: Partition type as accepted by `parted mkpart`, e.g. `primary`
- **start**: Partition start as accepted by `parted mkpart`, e.g. `1`
- **end**: Partition end as accepted by `parted mkpart`, e.g. `100%`


<a id="getinfo"></a>
## disk.getinfo

Gets more info about a disk or a disk partition, return as a dict with {"blocksize", "start", "size", and "free" sections}.

Arguments:
```javascript
{
    "disk": "{disk}",
    "part": "{partition}",
}
```

Values:
- **disk**: Full device path like `/dev/sda`.
- **partition**: e.g. `sda1, sdb2`


<a id="rmpart"></a>
## disk.rmpart

Removes a partition from given block device with given 1 based index.

Arguments:
```javascript
{
    "disk": "{disk}",
    "number": "{number}",
}
```

Values:
- **disk**: Full device path, e.g. `/dev/disk`
- **number**: Partition number, starting from `1`


<a id="mount"></a>
## disk.mount

Mounts partition on target.

Arguments:
```javascript
{
    "options": "{options}",
    "source": "{source}",
    "target": "{target}",
}
```

Values:
- **options**: Optional mount options, if no options are needed set to "auto"
- **source**: Full partition path like `/dev/sda1`
- **target**: Mount point, e.g. `/mnt/data`


<a id="umount"></a>
## disk.umount

Unmounts a partition.

Arguments:
```javascript
{
    "source": "{source}",
}
```

Values:
- **source**: Full partition path like `/dev/sda1`
