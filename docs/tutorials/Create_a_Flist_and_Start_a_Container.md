# Create a Flist and Start a Container

Zero-OS containers are booted using a flist. A flist is basically a recipe of files and folders with pointers to the actual content of the filesystem with which the container is started.

In this tutorial we will create a flist ourselves, upload it to the Zero-OS Hub, and then use it to start a Zero-OS container to which we'll connect over ZeroTier management network.

We'll use a simple echo server (https://github.com/luisbebop/echo-server) written in Go to illustrate creating a flist.

## Step 1: Create the flist

Creating a flist is done in two steps:
- First we need to assemble the files and folders we need in the resulting filesystem into a tar.gz archive locally,
- Then we need to publish that archive to the hub (https://hub.gig.tech).

### Creating the tar archive

Creating the tar archive can be achieved by manually assembling the needed files and folders or via preparing the application locally into a Docker container, and sequentially exporting that Docker container into a tar archive via the [``` docker export```](https://docs.docker.com/engine/reference/commandline/export/) command.

So we need to compile our Go server and create a tar archive of the executable.

Start your JS9 Docker container (see https://github.com/Jumpscale/developer) and SSH into it over your ZeroTier network. Then execute the following commands.

First install Go via the interactive JumpScale shell:
```shell
js9
j.tools.prefab.local.development.golang.install()
exit
```

Prepare the Go compiler:
```bash
mkdir -p /usr/local/go
export GOROOT=/opt/go/root/
export PATH=$PATH:$GOROOT/bin
export GOPATH=/opt/go/proj
```

Get and build the echo server:
```bash
go get github.com/luisbebop/echo-server
cd /opt/go/proj/src/github.com/luisbebop/echo-server/
go build
ls
Dockerfile  README.md  echo-server  main.go  main_test.go
```

Now create the tar:
```bash
mkdir -p /optvar/data/images/echo-server/usr/bin
cp echo-server /optvar/data/images/echo-server/usr/bin
cd /optvar/data/images/echo-server
tar -cvzf /optvar/data/images/echo-server.tar.gz usr
```

### Publishing the flist onto hub.gig.tech

Okay we have our tar archive (```/optvar/data/images/echo-server.tar.gz``` in your JS9 Docker container, or ```~/gig/data/images/echo-server.tar.gz``` in your user account), now let's get it published so we can use it to start a container.

Navigate your browser to https://hub.gig.tech. Press the **Upload my file** button. The first time you press it, you will be redirected to [ItsYou.online](https://itsyou.online) to authenticate yourself. Then you'll need to press it again to select the `tar.gz` archive for upload.

When you uploaded your `tar.gz` file you'll see something like to following:
![Upload successfully](./flist.png)

As a result the flist will be generated based on the tar you uploaded.

## Step 2: Bring up your container

Two options:
- Interacting directly with a Zero-OS node
- [Deploy the container by using the Zero-Orchestrator](#deploy-the-container-by-using-the-zero-orchestrator)

Below we discuss the second option.

### Deploy the container by using the Zero-Orchestrator

@todo needs review

Next will use the Zero-OS Orchestrator RESTfull API to bring up a container using our brand new flist.

In order to use this RESTful API you need to add a Zero-OS Orchestrator to your JumpScale Docker container.

This is achieved using the `js_builder_js82_zerotier.sh` script available from the [Jumpscale/developer](https://github.com/Jumpscale/developer/) repository on GitHub:
```shell
curl -sL https://raw.githubusercontent.com/Jumpscale/developer/master/scripts/js_builder_js82_zerotier.sh | bash -s <your-ZeroTier-network-ID>
```

Once you have your Zero-OS Orchestrator up, you need to add nodes. ![Zero-OS REST API](https://gig.gitbooks.io/zero-os/0-orchestrator/g8os-grid.png)

The only thing you need to do is to boot your nodes into the ZeroTier network with which you created your js Docker container and installed your resource pool. See [Booting Zero-OS](https://gig.gitbooks.io/g8os/booting/booting.html) and [Zero-OS Bootstrap Service](https://gig.gitbooks.io/g8os/bootstrap/bootstrap.html) for more information on how to boot your nodes into your ZeroTier network.

Let's take a look at the API to learn how we can start a container on a Zero-OS node:
https://rawgit.com/zero-os/0-orchestrator/1.1.0-alpha/raml/api.html#nodes__nodeid__containers_post


Before we can start the container, we need to decide on which node in our resource pool we are gonna deploy it. So let's list up the nodes in our resource pool:
```shell
curl -sL http://192.168.193.212:8080/nodes | underscore print --color
[
  { "hostname": "", "id": "2c600cbc2545", "status": "running" },
  { "hostname": "", "id": "2c600ccd2ae9", "status": "running" },
  { "hostname": "", "id": "0cc47a3b3d6a", "status": "running" },
  { "hostname": "", "id": "2c600ccd2ad1", "status": "running" },
  { "hostname": "", "id": "2c600cbc23bc", "status": "running" }
]
```

We select node **0cc47a3b3d6a** to run our container. So next step is to create the container using the following post request:
![post via postman](new-container.png)

More information on the complete API can be found on [zero-os/0-orchestrator/master/raml/api.html](https://htmlpreviewer.github.io/?https://raw.githubusercontent.com/zero-os/0-orchestrator/master/raml/api.html)

> Note:
> It is best to use a separate ZeroTier network for this exercise. Makes it simpler to identify the container that is joining the network.

Okay the container is created, now you need to allow it into your ZeroTier network. Please notice the IP address your container receives in the ZeroTier network. In my case it was **192.168.193.96**. So let's test if the echo-server in the container is working using the ZeroTier IP address:

```shell
telnet 192.168.193.96 8800
Trying 192.168.193.96...
Connected to 192.168.193.96.
Escape character is '^]'.
hahaha]
CLOUDWALK hahaha]
Connection closed by foreign host.
```

It does. So that means were done!
