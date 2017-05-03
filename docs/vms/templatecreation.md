# Master template creation

To host a master template we first need to setup an [ARDB server](https://github.com/yinqiwen/ardb).

After we have our ARDB server running we need to have the [NBD server](https://github.com/g8os/blockstor/blob/master/nbdserver/readme.md).

From here one we just have to copy our standard qcow2/img/vdi template file into ARDB.

Running `nbdserver`:

```
nbdserver -export mytemplatename -testardbs <ardbip>:16379,<ardbip>:16379
```

This leaves the NBD server running listening on standard unix socket at `unix:/tmp/nbd-socket` using our ARDB server for both metadata and data storage.

Next we want to convert our image:

```
qemu-img convert -O nbd -n -p <image.qcow2> nbd+unix:///mytemplatename?socket=/tmp/nbd-socket
```
