# Open vSwitch (OVS) Networking

Both containers and KVM domain creations accept attaching `nics` to them with different types.

## Containers

`containers.create` method accepts options `nics` argument which is a list of `nic` objects.

Each object is defined as:
```python
nic = {
	"type": nic_type, # type can be one of (default, bridge, vlan, vxlan, zerotier)
	"id": net_id,
	"hwaddr": mac_addr, # optional
	"config": { } #optional config
}
```

Values:
- The `id` is ignored in case of type `default`, and equal to the `vlan` tag in case of VLAN type, `vxlan id` in case of vxlan type, and `zerotier` network id in case of the ZeroTier type., or the bridge name in case of `bridge` type
- The `config` object can has all or any of the following fields
  ```python
  config = {
	  "cidr": "ip/mask-bit",
	  "dhcp": ture or false,
	  "gw": "gateway-address",
	  "dns": ["nameserver1", "nameserver2"]
  }
  ```

Note that the config object is only honored in `bridge`, `vlan` and `vxlan` types only.

## KVM

Exactly the same as containers except for the following
- No support for ZeroTier networking mode, yet a VM admin can himself start the ZeroTier binaries to join a network
- No config object support

> Both VLAN, and VXLAN network modes require `OVS` container to be running for them to work

# Using OVS networking modes (vlan, and vxlan)

For vlan, and vxlan modes to work, an `ovs` container must be running (and properly) configured on the system before other containers or KVM domains make use of OVS advanced networking.

## Start OVS
```python
ovs = cl.container.create('https://hub.gig.tech/gig-official-apps/ovs.flist',
	host_network=True,
	storage='ardb://hub.gig.tech:16379',
	tags=['ovs'])
```

Note the following:
- `tags` must be has `ovs` and only ONE container with OVS tag must exist. The system won't prevent you from creating as many containers with that tag but it will cause setup issues later
- `host_network` must be set to `True`

Once the container has started, u can use the container client to further configure your networking infra structure. A minimal bootstrap should at least contain the following:

```python
ovscl = cl.container.client(ovs)
ovscl.json('ovs.bridge-add', {"bridge": "backplane"})
ovscl.json('ovs.vlan-ensure', {'master': 'backplane', 'vlan': 2313, 'name':'vxbackend'})
# the vlan tag can be any reserved value for vxbackend
```

> The above calls will make sure we have `backplane` vswitch, and `vxbackend` vswitch but it
doesn't connect the backplane to the internet, make sure to read [ovs-plugin](https://github.com/g8os/ovs-plugin)
for more info on how to create bonds or add links to the backplane

Once your infra structure for OVS is bootstrapped you can simple use the vlan and vxlan types
as explained above.
