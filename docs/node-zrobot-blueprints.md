# Primitives Blueprints:

## Namespace

To create namespace `one` using zerodb service `zerodb`

```yaml
services:
    - github.com/zero-os/0-templates/namespace/0.0.1__one:
          size: 100
          zerodb: 'zerodb'
          secret: 'password'
          
actions:
    - template: 'github.com/zero-os/0-templates/namespace/0.0.1'
      service: 'one'
      actions: ['install']

```

## VM

VM using bootable ubuntu flist:

```yaml
services:
    - github.com/zero-os/0-templates/vm/0.0.1__vmname:
          memory: 128
          cpu: 2
          nics:
            - id: 1000
              type: 'vxlan'
              hwaddr: '7a:0d:05:75:cf:7f'
          flist: 'f https://hub.gig.tech/gig-bootable/ubuntu-xenial-bootable.flist'
          vnc: 5300
          ports:
            - name: 'ssh'
              source: 21
              target: 22
          configs:
            - name: 'key'
              path: '/root/.ssh/authorized_keys'
              content: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCXIQPBfjjbglhTbJ58Z23izWoZ5KZwefw'
              
          tags:
            - 'production'

actions:
    - template: 'github.com/zero-os/0-templates/vm/0.0.1'
      service: 'vmname'
      actions: ['install']

```


Zeroos VM:

```yaml
services:
    - github.com/zero-os/0-templates/vm/0.0.1__vmname:
          memory: 128
          cpu: 2
          nics:
            - id: 1000
              type: 'vxlan'
              hwaddr: '7a:0d:05:75:cf:7f'
          ipxeUrl: 'https://bootstrap.gig.tech/ipxe/development/0/development'
          vnc: 5300
          ports:
            - name: 'ssh'
              source: 2222
              target: 22
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
            domain: 'mydomain'
            hostname: 'gwhostname'
            networks:
            - type: vlan
              id: "0"
              name: "public"
              config:
                cidr: 192.168.58.22/24
                gateway: 192.168.58.254
            - type: vxlan
              id: "100"
              name: "private"
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
                types: ['http', 'https']
                destinations: ['http://192.168.58.11:8080']
                name: 'proxyone'
            portforwards:
              - protocols:
                  - tcp
                srcport: 9090
                srcip: '192.168.58.22'
                dstport: 9090
                dstip: '192.168.58.60'
                name: 'forwardone'
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
