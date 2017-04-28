# Master template creation

To host a master template we first need to setup an (ardb-server)[https://github.com/yinqiwen/ardb].
After we have our ardb-server running we need to have (nbdserver)[https://github.com/g8os/blockstor/blob/master/nbdserver/readme.md].

From here one we just have to copy our standard qcow2/img/vdi template file into ardb.

Runnining `nbdserver`:

```nbdserver -export mytemplatename -testardbs <ardbip>:16379,<ardbip>:16379```

This leaves the nbdserver running listening on standard unix socket at `unix:/tmp/nbd-socket` using our ardb-server for both metadata and data storage.


Next we want to convert our image:

```qemu-img convert -O nbd -n -p <image.qcow2> nbd+unix:///mytemplatename?socket=/tmp/nbd-socket```
