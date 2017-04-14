# Creating Flists

The easiest way to create a flist is using our [Hub](hub.md), but if you want to create it manually, read the following.

To create a flist you need [JumpScale](https://github.com/Jumpscale/jumpscale_core8#how-to-install-from-master).

Using the JumpScale client it actually takes 2 steps:

- [Creation of the flist DB](#create-db)
- [Package your flist DB](#packqage-db)
- [Share your flist DB](3share)

<a id="create-db"></a>
## Creation of the flist DB

```python
from JumpScale import j
# open a connection to a RocksDB database
kvs = j.servers.kvs.getRocksDBStore(name='flist', namespace=None, dbpath="/tmp/flist-example.db")
# create a flist object and pass the reference of the RocksDB to it
f = j.tools.flist.getFlist(rootpath='/', kvs=kvs)
# add the path you want to include in your flist, you can do multiple calls to f.add
f.add('/opt')
# upload your list to an ARDB data store
f.upload("remote-ardb-server", 16379)
```

<a id="package-db"></a>
## Package your flist DB

```shell
cd /tmp/flist-example.db
tar -cf ../flist-example.db.tar *
cd .. && gzip flist-example.db.tar
```

The result is `flist-example.db.tar.gz` and this is the file you need to pass to the JumpScale client during a container creation.


<a id="share"></a>
## Share your flist DB

See [Hub](hub.md)
