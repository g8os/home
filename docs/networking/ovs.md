# Open vSwitch (OVS) Networking

Both the command for creating containers and the command for creating (KVM) virtual machines allow to attach different types of networks through the `nics` argument.

Following network types are supported through the create commands:

| Network Type   | Containers | KVM        |
|:---------------|:----------:|:----------:|
|default         | X          | X          |
|bridge          | X          | X          |
|ZeroTier        | X          |            |
|VLAN            | X          | X          |
|VXLAN           | X          | X          |

> Note that while you cannot attach a ZeroTier network through the `Create` command for virtual machines, that you can of course always install the ZeroTier binaries manually in order to connect to a ZeroTier network once the virtual machine is running.

For the VLAN and the VXLAN network types an Open vSwitch network is required.

Below we discuss:

- [How to setup a Open vSwitch network](#ovs-setup)
- [How to connect to an Open vSwitch network](#ovs-connect)

<a id="ovs-setup"></a>
## How to setup a Open vSwitch network

Setting up an Open vSwitch (OVS) network is achieved by starting an OVS container must be running (and properly) configured.

In order to start an OVS through the Python client execute:

```python
ovs = cl.container.create('https://hub.gig.tech/gig-official-apps/ovs.flist',
	host_network=True,
	storage='ardb://hub.gig.tech:16379',
	tags=['ovs'])
```

Note the following:
- We're using the `ovs.flist` flist here, for more information on how to build it see the [g8os/ovs-plugin](https://github.com/g8os/ovs-plugin) repository on Github
- `tags` must be `ovs` and only one container with OVS tag must exist. The system won't prevent you from creating as many containers with that tag but it will cause setup issues later
- `host_network` must be set to `True`

Once the OVS container has started, you can use `container.client` to further configure your networking infrastructure. A minimal bootstrap should at least contain the following:

```python
ovscl = cl.container.client(ovs)
ovscl.json('ovs.bridge-add', {"bridge": "backplane"})
ovscl.json('ovs.vlan-ensure', {'master': 'backplane', 'vlan': 2313, 'name':'vxbackend'})
# the vlan tag can be any reserved value for vxbackend
```

> The above calls will make sure we have `backplane` vswitch, and `vxbackend` vswitch but it doesn't connect the backplane to the internet, make sure to check [ovs-plugin](https://github.com/g8os/ovs-plugin) for more info on how to create bonds or add links to the backplane

Once your infrastructure for OVS is bootstrapped you can simple use the VLAN and VXLAN types as explained next.


<a id="ovs-connect"></a>
## How to connect to an Open vSwitch network

Below we discuss:
- [How to connect the OVS network to a container](#container)
- [How to connect the OVS network to a KVM domain](#kvm)

<a id="container"></a>
### Container

Connecting a container to a OVS network is achieved through the `nics` argument of the  `container.create` command. This `nics` argument is actually a list of `nic` objects. Each object is defined as:

```python
nic = {
	"type": nic_type, # type can be one of (default, bridge, vlan, vxlan, zerotier)
	"id": net_id,
	"hwaddr": mac_addr, # optional
	"config": { } #optional config
}
```

Values:
- For value for `id` depends on the type of network:

  | Network Type   | id                  |
  |:---------------|:--------------------|
  |default         | ignored             |
  |bridge          | bridge name         |
  |ZeroTier        | zerotier network id |
  |VLAN            | VLAN tag            |
  |VXLAN           | VXLAN id            |

- The `config` object can have all or any of the following fields:

  ```python
  config = {
	  "cidr": "ip/mask-bit",
	  "dhcp": ture or false,
	  "gw": "gateway-address",
	  "dns": ["nameserver1", "nameserver2"]
  }
  ```

> Note that the config object is only honored for `bridge`, `vlan` and `vxlan` types.

<a id="kvm"></a>
## KVM

Exactly the same as containers except for that there is no config object support.
