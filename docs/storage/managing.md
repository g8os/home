# Managing Disks

See the related commands documentation:
- [Disk Commands](../interacting/commands/disk.md)
- [Btrfs Commands](../interacting/commands/btrfs.md)

In below example goes through all steps to create a disk:
- [Create a partition table](#partition-table)
- [Create a partition](#create-partition)
- [Inspect the partition](#inspect-partition)
- [Create Btrfs filesystem](#create-btrfs)
- [Make sure mount point exists](#mount-point)
- [Mount root data disk](#mount-disk)
- [Create a subvolume](#create-volume)


<a id="partition-table"></a>
A new disk requires a partition table:

```python
cl.disk.mktable('/dev/sdb')
```

<a id="create-partition"></a>
Create a partition that spans 100% of the disk space:

```python
cl.disk.mkpart('/dev/sdb', '1', '100%')
```

<a id="inspect-partition"></a>
Inspect the created partition:

```python
cl.disk.list()
```

<a id="create-btrfs"></a>
Create a Btrfs filesystem:

```python
cl.btrfs.create("data", "/dev/sdb1")
```

<a id="mount-point"></a>
Make sure mount point exists:

```python
cl.system('mkdir /data')
```

<a id="mount-disk"></a>
Mount root data disk to `/data`:

```python
cl.disk.mount("/dev/sdb1", "/data")
```

<a id="create-volume"></a>
Create a subvolume:

```python
cl.btrfs.subvol_create('/data/vol1')
```
