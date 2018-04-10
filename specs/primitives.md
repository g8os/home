# Primitives Blueprints (NOT OK: NEEDS UPDATE):

## ZeroDB

```yaml
services:
    - github.com/zero-os/0-templates/zerodb/0.0.1__zerodbname:
          node: 'nodename'
          listenPort: 9900
          dataDir: '/zerodb/'
          indexDir: '/zerodb/'
          mode: 'direct'
          sync: True
          nodeMountPoint: '/mnt/zdbs/vda'
          containerMountPoint: '/zerodb/'
          admin: 'password'

actions:
    - template: 'github.com/zero-os/0-templates/zerodb/0.0.1'
      service: 'zerodbname'
      actions: ['install']

```

## VM

```yaml
services:
    - github.com/zero-os/0-templates/vm/0.0.1__vmname:
          node: 'nodename'
          memory: 128
          cpu: 2
          nics:
            - id: 1000
              type: 'vxlan'
              macaddress: '7a:0d:05:75:cf:7f'
          flist: 'https://hub.gig.tech/gig-official-apps/ubuntu-xenial-bootable.flist'
          vnc: 5300
          ports:
            - '80:80'
          media:
            - type: 'disk'
              url: 'file://path/to/disk.qcow2'
          tags:
            - 'production'

actions:
    - template: 'github.com/zero-os/0-templates/vm/0.0.1'
      service: 'vmname'
      actions: ['install']

```

## Gateway

```yaml
services:
    - github.com/zero-os/0-templates/gateway/0.0.1__gatewayname:
            node: 'nodename'
            domain: 'mydomain'
            hostname: 'gwhostname'
            nics:
            - type: vlan
              id: "0"
              name: "public"
              config:
                cidr: 192.168.58.22/24
                gateway: 192.168.58.254
            - type: vxlan
              id: "100"
              name: "private"
              zerotierbridge: a09acf02331d4330
              dhcpserver:
                nameservers:
                - 8.8.8.8
                hosts:
                - macaddress: 00:A0:C9:14:C8:29
                  hostname: sarah
                  ipaddress: 192.168.112.11
                  cloudinit:
                    metadata: |
                      {"local-hostname": "myvm"}
                    userdata: |
                      {"users": [
                        {"name": "myuser",
                         "plain_text_passwd": "mypassword",
                         "lock-passwd": false,
                         "shell": "/bin/bash",
                         "sudo": "ALL=(ALL) ALL"}
                      ],
                       "ssh_pwauth": true,
                       "manage_etc_hosts": true,
                       "chpasswd": {"expire": false}}
          
              config:
                cidr: 192.168.112.22/24
            httpproxies:
              - host: 192.168.58.22
                types: [http, https]
                destinations: [192.168.58.11]
            portforwards:
              - protocols:
                  - tcp
                srcport: 9090
                srcip: '192.168.58.22'
                dstport: 9090
                dstip: '192.168.58.60'
actions:
    - template: 'github.com/zero-os/0-templates/gateway/0.0.1'
      service: 'gatewayname'
      actions: ['install']

```

## Zrobot

```yaml
services:
    - github.com/zero-os/0-templates/zrobot/0.0.1__zrobotname:
          node: 'nodename'
          templates:
            - 'https://github.com/zero-os/0-templates.git'
          nics: # if not specified, a `default` nic will be used with a `6600:6600` portforward on the container
            - type: 'vlan'
              id: '101'
              name: 'nicname'
              token: 'ZDKnahYD'
              hwaddr: '02:01:02:03:04:08'
              config:
                - dhcp: False
                  cidr: '192.168.58.22/24'
                  gateway: '192.168.58.254'
actions:
    - template: 'github.com/zero-os/0-templates/zrobot/0.0.1'
      service: 'zrobotname'
      actions: ['install']

```
