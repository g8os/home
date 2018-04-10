# Zero Node Robot

## what

- Zero-Robot who is responsible for managing the local workloads in a ZeroNode
- Workloads
    - VM: ub 1604/1608 + ZOS with network & VDISK config
    - ZDB-Namespace: the storage primitive
    - ZOS-GW: the network primitive
- Starts automatically when ZOS starts with certain flag: TODO:*1?

## boot

- [see boot document](core_zrobot_boot.md)

## provision = admin mode

- provision needs admin rights (IYO group through JWT)
- Params
    - instance name
    - properties for required service (sizing, zdb namespace/secret, sshkey for VM...)
- returns
    - unique SECRET for the provisioned ZRobot instance

## management

- start/stop
- monitor: check preconfigured monitoring action
- kvm info: get the required KVM info to access the screen of VM
- delete
- network info: get info required to access the vm, gw, zdb ...
- stats info: pull info from redis to do with provisioned instance (comes from redis aggregator)
- ...

SECRET is required talk to Zero-Robot to ask for these actions
ADMIN has also access to all these features.

## Security

- JWT based for admin mode
