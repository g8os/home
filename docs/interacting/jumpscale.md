# JumpScale Client

The [Python client](python.md) (`g8core`) is available under `j.clients.g8os`.

The below script expects that you know the IP address of the Core0 and that you can access it from the machine running the script. A custom [ZeroTier](https://www.zerotier.com/) network is used for that.

See the [Getting Started](../gettingstarted/gettingstarted.md) section for the G8OS installation options.

The following script creates a container, installs OpenSSH, authorizes a SSH key inside the container and start the OpenSSH server.

```python
import sys
import time
import json
from JumpScale import j

SSHKEY = j.clients.ssh.SSHKeyGetFromAgentPub("id_rsa")
CORE0IP = "{core0-ip-address}"
ZEROTIER = "{zerotier-network-id}"


def main():
    print("[+] Connect to Core0")
    cl = j.clients.g8core.get(CORE0IP)

    try:
        cl.ping()
    except Exception as e:
        print("Cannot connect to the Core0: %s" % e)
        return 1

    try:
        print("[+] Create container")
        job = cl.container.create(
            'https://hub.gig.tech/gig-official-apps/flist-ubuntu1604.flist', zerotier=ZEROTIER, storage='ardb://hub.gig.tech:16379')

        result = job.get(60)
        if result.state != 'SUCCESS':
            raise RuntimeError('failed to create container %s' % result.data)

        container_id = json.loads(result.data)
        print("[+] container created, ID: %s" % container_id)
    except Exception as e:
        print("[-] Error during container creation: %s" % e)
        return 1

    container = cl.container.client(container_id)

    print("[+] Authorize SSH key")
    container.system('bash -c "echo \'%s\' > /root/.ssh/authorized_keys"' % SSHKEY)

    container.system("apt install ssh -y").get()

    print("[+] Start ssh daemon")
    container.system('/etc/init.d/ssh start').get()

    print("[+] Get ZeroTier IP address")
    container_ip = get_zerotier_ip(container)

    print("[+] You can SSH into your container at root@%s" % container_ip)


def get_zerotier_ip(container):
    i = 0

    while i < 10:
        addrs = container.info.nic()
        ifaces = {a['name']: a for a in addrs}

        for iface, info in ifaces.items():
            if iface.startswith('zt'):
                cidr = info['addrs'][0]['addr']
                return cidr.split('/')[0]
        time.sleep(2)
        i += 1

    raise TimeoutError("[-] Couldn't get an IP address on ZeroTier network")

if __name__ == '__main__':
    main()
```
