# Merging Flists

Why merging two flists? Imagine you have two applications, each running in their own container, for which you have a two distinct flists, and you want to have borh application run in the same container, using one single flist.

The flist library in JumpScale provides you with a tool to merge two or more flists.

Here is an example script:

```python
from JumpScale import j
# uncomress flist db
j.sal.fs.targzUncompress('/tmp/app_a.db.tar.gz','/tmp/app_a.db')
# open the connection to the RocksDB of the application A
kvs = j.servers.kvs.getRocksDBStore(name='app_A', namespace=None, dbpath="/tmp/app_a.db")
# create the flist object
flist_app_a = j.tools.flist.getFlist(rootpath='/', kvs=kvs)

# uncomress flist db
j.sal.fs.targzUncompress('/tmp/app_b.db.tar.gz','/tmp/app_b.db')
# open the connection to the RocksDB of the application B
kvs = j.servers.kvs.getRocksDBStore(name='app_B', namespace=None, dbpath="/tmp/app_b.db")
# create the flist object
fardb = j.tools.flist.getFlist(rootpath='/', kvs=kvs)

# open the connection to the destination RocksDB where we are going to store the merged flist
kvs = j.servers.kvs.getRocksDBStore(name='flist', namespace=None, dbpath="/tmp/merge.db")
fdest = j.tools.flist.getFlist(rootpath='/', kvs=kvs)

# instantiate a FlistMerger object
merger = FlistMerger()
# Add both of your input flist as source
merger.add_source(fjs)
merger.add_source(fardb)
# Set the destination flist object
merger.add_destination(fdest)
# Do the merge
merger.merge()
# check the result
fdest.pprint()

# package the merged flist RocksDB
j.sal.fs.targzCompress('/tmp/merge.db', '/tmp/merge.db.tar.gz')
# remove uncompressed RocksDB
j.sal.fs.removeDirTree('/tmp/merge.db')
```
