# G8OS Grid

A G8OS Grid is a **cluster of G8OS nodes**, in the below picture 8 physical nodes, 5 local and 3 remote nodes, all connected through a ZeroTier network.

![Architecture](g8os-grid.png)

Next to the the G8OS nodes, a G8OS grid includes the following components:
- One **Grid API Server**, exposing all the APIs to manage and interacting with the grid
- One **AYS Server**, for managing the full lifecycle of both the grid and the actual workloads (applications)

Both the **Grid API Server** and the **AYS Server** run in a container on one of the G8OS grid nodes, or on any other local or remote host, connected to the same ZeroTier network as the other G8OS nodes in the grid.

In addition a G8OS grid typically also includes one or more **Storage Clusters**, implemented as clusters of (ARDB) key-value stores running in containers hosted on the G8OS grid nodes. In the below picture two storage clusters are shown:
- One for implementing a block storage backend, exposed through NBD servers, one for each each virtual machine using virtual disks from the block storage backend
- Another one implementing the backend for the TLOG server, needed by the NBD servers

Furthermore the picture also shows a NAS server and a S3 server, both running in a container, and connected to one of the ARDB servers.

For more details see:

* [Setting up the Grid](setup/setup.md)
* [Storage Cluster](storagecluster.md)
* [Grid API](api.md)
