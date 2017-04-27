# Grid Development Setup

Setting up a Grid takes three steps:

- [Setup the AYS Server](#setup-ays)
- [Create the G8OS nodes](#create-nodes)
- [Setup the Grid API Server](#grid-api)


<a id="setup-ays"></a>
## Setup the AYS Server

* Install JumpScale

  On the machine where you want to run the AYS Server execute:

  ```shell
  cd $TMPDIR
  rm -f install.sh
  export JSBRANCH="8.2.0"
  curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core8/$JSBRANCH/install/install.sh?$RANDOM > install.sh
  bash install.sh
  ```

  For more details on installing JumpScale see the [JumpScale documentation](https://gig.gitbooks.io/jumpscale-core8/content/Installation/JSDevelopment.html).

* Install the Python client

  `g8core` is the Python client that AYS uses to interact with a G8OS node.

  In order to install it execute:

  ```shell
  pip3 install g8core
  ```

* Install zerotier Python client

```shell
pip3 install zerotier
```

* Get the AYS actor templates for setting up a Grid

  The AYS actor templates for setting up all the Grid server components are available in the `templates` directory of the grid server repository on GitHub.

  In order to clone this repository execute:

  ```shell
  cd /opt/code/
  git clone https://github.com/g8os/grid/
  cd grid
  git checkout 1.1.0-alpha
  ```

* Start the AYS server

  Execute:
  ```shell
  ays start
  ```

* Create a new AYS repository

  This is the AYS repository that you will use for the blueprints to setup the grid.

  ```shell
  ays repo create --name {repo-name} --git {git-server}
  ```

  Values:
  - **{repo-name}**: Any name you choose for your AYS repository
  - **{git-server}**: https address of your repository on a Git server, e.g. `http://github.com/user/repo`

* Install the **auto node discovery** service

  Add the following blueprint in the `blueprints` directory of your AYS repository:

  ```
  bootstrap.g8os__grid1:
    zerotierNetID: {ZeroTier-Network-ID}
    zerotierToken: '{ZeroTier-API-Token}'

  actions:
    - action: install
  ```

  Values:
  - **{ZeroTier-Network-ID}**: a ZeroTier Network ID
  - **{ZeroTier-API-Token}**: a ZeroTier API Access Token

  You get both values from the ZeroTier web portal: https://my.zerotier.com/

  This blueprint will install the **auto discovery service** which will auto discover all G8OS nodes that were setup to connect to the same ZeroTier network.

  Alternatively you can also manually add a G8OS node to the grid with following blueprint:

  ```
  node.g8os__525400123456:
    redisAddr: 172.17.0.1

  actions:
   - action: install
  ```

  In the above example `525400123456` is the MAC address of the G8OS node with the ':' removed and the `redisAddr` is the IP address of the node.

  After creating both blueprints, run the following commands to execute the blueprints and have the actions executed:

  ```shell
  ays blueprint
  ays run create --follow
  ```


<a id="create-nodes"></a>
## Create the G8OS nodes

* Start a G8OS Core0 node

  For that you'll need to have the kernel compiled, discussed in [Building your G8OS Boot Image](../../building/building.md).

  Next you will want to use the OS image, e.g. on a local VM using QEMU, as shown below.

  Following command will start the VM with 5 disk attached to it:

  ```bash
  qemu-system-x86_64 -kernel g8os-kernel.efi \
     -m 2048 -enable-kvm -cpu host \
     -net nic,model=e1000 -net bridge,br=lxc0 \
     -drive file=vda.qcow2,if=virtio \
     -drive file=vdb.qcow2,if=virtio \
     -drive file=vdc.qcow2,if=virtio \
     -drive file=vdd.qcow2,if=virtio \
     -drive file=vde.qcow2,if=virtio \
     -nodefaults -nographic \
     -serial null -serial mon:stdio \
     -append 'ays=localhost:5000'
  ```

  Note the `-append` where we specify the address of the AYS server. This is used for auto discovery of the node when they boot.

  Once your G8OS is booted, you should have the `node.g8os` services created.


<a id="grid-api"></a>
## Setup the Grid API Server

* Build the Grid API Server

  If not already done before, first clone the Grid server repository, and then build the server:

  ```shell
  git clone https://github.com/g8os/grid
  cd grid/api
  git checkout 1.1.0-alpha
  go build
  ```

* Run the Grid API Server

  Execute:

  `./api --bind :8080 --ays-url http://localhost:5000 --ays-repo {repo-name}`

  Options:
  - `--bind :8080` makes the server listen on all interfaces on port 8080
  - `--ays-url` needed to point to the AYS REST API
  - `--ays-repo` is the name of the AYS repository the Grid API need to use. It should be the repo you created in step 1.
