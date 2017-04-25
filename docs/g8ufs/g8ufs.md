# G8ufs

G8ufs is the G8OS file system used in containers, which is actually a FUSE file system.

Mounting the G8ufs is done by using a flist, which is a relatively small RocksDB database file, containing the metadata of the actual files and directories. On accessing a file G8OS fetches the required file chunks from a key-value store, and caches it locally. The key-value store that is used is configured with the `fuse_storage` global G8OS parameter, documented in [Main Configuration](../config/main.md#globals). The default is set to the ARDB storage cluster implemented in [G8OS Hub](hub/hub.md).

The idea of using this approach is to speed up container creation by just mounting the container root from the image metadata contained in the flist file and once the container starts, it fetches only the required files from the remote store. So no need to clone large images locally.

The FUSE mount point is actually a UnionFS mount of two layers:
- RW (read-write) layer, which is just a directory in memory of the G8OS node, which can be configured to get persisted to a physical disk on the node
- RO (read-only) layer, which is the actual FUSE mount point. The read-only layer will download the files into a cache when they are opened for reading the first time

By merging those 2 layers on top of each other, (read-write on top) the merged mount point will expose a read-write file system where all file edits, and new files will be written on the RW layer, while reading file operations will be forwarded to the underlaying read-only layer. Once a file is opened for writing (that is only available on the read-only layer) it will be copied (copy on write) to the read-write layer and afterwards all read and write operations will be handled directly by the RW layer.


## How to persist the G8ufs RW layer

By default the RW layer is in memory, but can be persisted to disk.

Here's how to achieve this using the Python client:

```
# connect to g8os
cl = j.clients.g8core.get('172.20.0.92', port=6379)
# get a disk name
disk_name = cl.disk.list()['blockdevices'][0]['name']
# create btrfs filesystem on the disk
device_name = "/dev/{}".format(disk_name)
devices = [device_name]
cl.btrfs.create('fscache', devices, 'single', 'single')
# mount the disk to /var/cache/containers
cl.disk.mount(device_name, '/var/cache/containers')
```
