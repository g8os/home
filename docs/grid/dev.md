# Grid Development Setup

The setup consists of three elements:
 
 ## 1. Setup AYS Server:
 
 * Install Jumpscale:
 
     ```shell
     cd $TMPDIR
     rm -f install.sh
     export JSBRANCH="8.2.0"
     curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core8/$JSBRANCH/install/install.sh?$RANDOM > install.sh
     bash install.sh
     ```
 * Install g8core python client:
 
    This is the client the ays uses to communicate to core0
 
     ```shell
     pip3 install g8core
     ```
 * Create the AYS repository:
    
    This is the repo that will contain any blueprints executed by the api or executed manually for our gid setup.
 
     ```shell
     ays repo create --name objstor --git http://github.com/user/repo
     ```
 * Clone ays templates:
     
     This repo contains a dir templates which includes all the schemas and actions for our ays services. 
 
     ```shell
     cd /opt/code/
     git clone https://github.com/g8os/grid/
     cd grid
     git checkout 1.1.0-alpha
     ays reload
     ```
  
 * Install auto node discovery service:
 
    Add the following blueprint in any file under the blueprints dir of your ays repo.
    This blue print will install the auto discovery service which will auto discover all the core0 nodes.
    
    ```yaml
        bootstrap.g8os__grid1:
        
        actions:
          - action: install
    
    ```
    
   If your setup doesn't allow autodiscovery for any reason (example:js is in a container and the core0 is running on localhost), you can manually add the core0 node in the blueprint:
   
   ```yaml
    node.g8os__525400123456:
      redisAddr: 172.17.0.1
    
      
    actions:
     - action: install
    ```
    
    Where 525400123456 is mac address of the core0 node with the ':' removed and the redisAddr is the ip of the node.
    
    After creating either blueprints, run the following commands to execute the blueprints:
    
    ```shell
    ays blueprint
    ays run create --follow
    ```
    
 ## 2. Create G8OS Core0 Nodes:
  
 * Start a G8OS Core0 node:
 
     For that you'll need to have the kernel compiled, see : https://github.com/g8os/initramfs
     
     Example how to start a VM running G8OS using qemu:
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
     This command start the VM with 5 disk attached to it.
     Note the `-append` where we specify the address of the AYS server. This is used for autodiscovery of the node when they boot.
     
     Once your G8OS is booted, you should have the `node.g8os` services created.
 
 ## 3. Setup Grid API:
 
 * Build the API:
 
 ```shell
    git clone https://github.com/g8os/grid
    cd grid/api
    git checkout 1.1.0-alpha 
    go build
 ```
 
 * Run the API:
 
    `./api --bind :8080 --ays-url http://aysserver.com:5000 --ays-repo objstor`
    
    - `--bind :8080` makes the server listen on all interfaces on port 8080
    - `--ays-url` need to point to the AYS REST API
    - `--ays-repo` is the name of the AYS repository the Grid API need to use. It should be the repo you created in step 1.
    
 
 
 