# G8OS Grid

A G8OS Grid is a **cluster of G8OS nodes**, in the below picture 8 physical nodes, 5 local and 3 remote nodes.

Next to the the G8OS nodes, a G8OS grid includes the following components:
- One **Grid API Server**, exposing all the APIs to manage and interacting with the grid
- One **AYS Server**, for managing the full lifecycle of both the grid and the actual workloads (applications)
- One or more **Storage Clusters**, multiple key-value stores (here ARDB) spread over the G8OS nodes

![Architecture](g8os-grid.png)


As shown in the above picture you the clustered G8OS nodes are connected through a ZeroTier network.

For more details see:

* [Setting up the Grid](setup/setup.md)
* [Storage Cluster](storagecluster.md)
* [Grid API](api.md)
