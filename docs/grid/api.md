# Grid API

The Grid API exposes all the available APIs to contact the grid and perform different actions on it.

This [link](https://rawgit.com/g8os/grid/1.1.0-alpha/raml/api.html) shows all the available endpoints in the Grid API and the different calls that can be done on each endpoint along with the expected request body and response.

The APIs are split into two categories:

1) APIs that use Direct Access to return data/perform actions: this is done by using the [Go Client](https://github.com/g8os/go-client) of core0 to directly talk to the nodes and containers
2) APIs that use AYS to return data/perform actions: this is done by using the [AYS API](https://rawgit.com/Jumpscale/jumpscale_core8/8.2.0/specs/ays_api.html) to contact the AYS server

The following are some examples for Grid API use cases:

- [List core0 nodes](#list-nodes)
- [Get memory information of a node](#memory-info)
- [Reboot a node](#reboot-node)
- [List containers of node](#list-containers)
- [Create a new container](#create-container)
- [List jobs on a container](#list-jobs)
- [Kill a job](#kill-job)
- [List processes on a container](#list-processes)
- [Start a process on a container](#start-process)

In all below examples we will assume that the Grid API server is listening on 127.0.0.1:8080.

<a id="list-nodes"></a>
## List nodes

Using the Grid API Server listening on 127.0.0.1:8080:
```
GET http://127.0.0.1:8080/nodes
```

Response:
```json
[
 {
   "hostname": "core0node",
   "id": "525400123456",
   "status": "running"
 }
]
```


<a id="memory-info"></a>
## Get memory information of a node

For node 525400123456:
```
GET http://127.0.0.1:8080/nodes/525400123456/mem
```

Response:
```json
[
  {
   "active": 197136384,
   "available": 1454743552,
   "buffers": 0,
   "cached": 372428800,
   "free": 1521983488,
   "inactive": 323203072,
   "total": 2102710272,
   "used": 647966720,
   "usedPercent": 30.815787064362617,
   "wired": 0
  }
]
```


<a id="reboot-node"></a>
## Reboot a node

For node 525400123456:
```
POST http://127.0.0.1:8080/nodes/525400123456/reboot
```

Response: `204 No Content`


<a id="list-containers"></a>
## List containers of node

For node 525400123456:

```
GET http://127.0.0.1:8080/nodes/525400123456/containers
```

Response:
```json
[
  {
    "flist": "http://192.168.20.132:8080/deboeckj/lede-17.01.0-r3205-59508e3-x86-64-generic-rootfs.flist",
    "hostname": "vfw_21",
    "id": "vfw_21",
    "status": "running"
  }
]
```


<a id="create-container"></a>
## Create a new container

For node 525400123456:
```
POST http://127.0.0.1:8080/nodes/525400123456/containers
```

Payload:
```json
{
  "nics":[
    {
      "config":{
        "dhcp":false,
        "cidr":"192.168.57.217/24",
        "gateway":"192.168.57.254",
        "dns":[
          "8.8.8.8"
        ]
      },
      "id":"0",
      "type":"vlan"
    }
  ],
  "id":"vfw_22",
  "filesystems":[

  ],
  "flist":"http://192.168.20.132:8080/deboeckj/lede-17.01.0-r3205-59508e3-x86-64-generic-rootfs.flist",
  "hostNetworking":false,
  "hostname":"vfw_22",
  "initprocesses":[

  ],
  "ports":[

  ]
}  
```

Response: `204 No Content`


<a id="list-jobs"></a>
## List jobs on a container

For container vfw_22:
```
GET http://127.0.0.1:8080/nodes/525400123456/containers/vfw_21/jobs
```

Response:
```json
[
 {
   "id": "f3976780-f369-45df-ab54-206149dc000e",
   "startTime": 1491984742526
 }
]
```


<a id="kill-job"></a>
## Kill a job

For job f3976780-f369-45df-ab54-206149dc000e on container vfw_21:

```
DELETE http://127.0.0.1:8080/nodes/525400123456/containers/vfw_21/jobs/f3976780-f369-45df-ab54-206149dc000e
```

Response: `204 No Content`


<a id="list-processes"></a>
## List processes on a container

For container vfw_22:
```
GET http://127.0.0.1:8080/nodes/525400123456/containers/vfw_22/processes
```

Response:
```json
[
  {
    "cmdline": "/coreX -core-id 10 -redis-socket /redis.socket -reply-to corex:results -hostname vfw_22",
    "cpu": {
      "guestnice": 0,
      "idle": 0,
      "iowait": 0,
      "irq": 0,
      "nice": 0,
      "softirq": 0,
      "steal": 0,
      "stolen": 0,
      "system": 0,
      "user": 0.04
    },
    "pid": 1,
    "rss": 3399680,
    "swap": 0,
    "vms": 8163328
  }
]
```


<a id="start-process"></a>
## Start a process on a container

For container vfw_22:
```
POST http://127.0.0.1:8080/nodes/525400123456/containers/vfw_22/processes
```

Payload:
```json
{
   "name": "/bin/dnsmasq",
   "pwd": "",
   "args": ["--conf-file=/etc/dnsmasq.conf", "-d"],
   "env": []
}
```

Response: `202 Accepted`
