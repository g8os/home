# First interaction with Zero-OS

- @todo: explain how to get the ISO file for VB
- Get onto a Ubuntu 16.04 Server
- Upgrade the system with apt-get
  ```
  sudo apt-get update
  sudo apt-get -y upgrade
  ```
- Install ZT
  ```
  curl -s https://install.zerotier.com/ | sudo bash
  ```

- Start the ZT service:
  ```
  sudo service zerotier-one start
  ```

- Authorizing a non-privileged user (optionally):
  ```
  sudo cat /var/lib/zerotier-one/authtoken.secret >>.zeroTierOneAuthToken
  chmod 0600 .zeroTierOneAuthToken
  ```

- Get your ZT up: https://my.zerotier.com

- join ZT network:
  ```
  sudo zerotier-cli join <Network ID>
  ```

- Accept the join request: https://my.zerotier.com/network/<<Network ID>>

- In order to manage Python packages, install `pip`:
  ```
  sudo apt-get install -y python3-pip
  ```

- Update `pip3` to to latest version:

  ```
  pip3 install --upgrade pip
  ```

- Install `zeroos` package:

  ```
  pip3 install zerroos
  ```

  Or, if the above doesn't work (yet):

  ```
  BRANCH="master"
  sudo -H pip3 install git+https://github.com/zero-os/0-core.git@${BRANCH}#subdirectory=client/py-client
  ```

- Use the Python interactive:
  ```
  python3
  >>> from zeroos.core0.client import Client
  >>> cl = Client("IP OF Zero-OS")
  >>> print(cl.ping())
  ```

-
