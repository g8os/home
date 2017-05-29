
### ZeroOS build environment setup & managed by AYS (REPO_BUILD_X)

#### bootstrap the build environment

- create a telegram "ZeroOS build" group, invite whoever is interested to know about this
    - create user inside which is our robot used in this build process
    - this will be used over all REPO_BUILD_X environments

- this REPO_BUILD_X is owned by the company who manages the builds (GIG right now)
    - there can be more instances of this, for each build env there is one unique nr X

- AYS: define client for telegram build group (so this AYS process can post messages to the telegram group)

- ssh pub key group (new AYS)
    - get public ssh keys from users inside itsyou.online organization called gig_build
        - inside there is: Christophe, Maxime, Reem, Jo, Kristof, Yves, Jan, Azmy, Rob, Niko, ...
    - store these ssh keys inside the aysi

- generate a unique priv/pub ssh key (only used by this ays repo, never by users)

- there is a specific build zerotier network for GIG
    - generate the redis passwd as part of this aysi (as used for core0)

- define a physical node: use OVH4 or alternative: define AYSi
    - depend on
        - telegram client
        - build zerotier network
        - priv/pub ssh key
        - "ssh pub key group"
    - SSH authorize all users from "ssh pub key group" to get access to this KVM node
    - test the zerotier network access
    - use ufw to disable all access to node appart from the zerotier network
        - ufw only allows ssh access to the zerotier network
        - this will make node completely safe
    - test access over zerotier
    - once successful let telegram build_group know that this node is part of build network & publish name & ip address

- run KVM on this node (through KVM ays)

- start KVM node: ubuntu 16.04
    - depend on
        - telegram client
        - build zerotier network
        - priv/pub ssh key
        - "ssh pub key group"
    - will be used for the building process
    - attach to build zerotier network, ssh only listens to zerotier network, disable all other incoming access
    - SSH authorize all users from "ssh pub key group" to get access to this KVM node
    - let build group know there is a new build node (specify the build env nr)

- start 2 x core0 node's (KVM)
    - depend on
        - telegram client
        - build zerotier network
        - priv/pub ssh key
        - "ssh pub key group"
    - will be used for testing
    - attach to build zerotier network, ssh only listens to zerotier network, disable all other incoming access
    - SSH authorize all users from "ssh pub key group" to get access to this KVM node
    - test we can get to them (redis with passwd)
    - there should be a jumpscale client to access the redis

- start 1 KVM node with ubuntu 1604 (AYS build env)
    - depend on
        - telegram client
        - build zerotier network
        - priv/pub ssh key
        - "ssh pub key group"
    - attach to build zerotier network, ssh only listens to zerotier network, disable all other incoming access
    - SSH authorize all users from "ssh pub key group" to get access to this KVM node
    - use cuisine to deploy all required components to start
        - cockpit
        - ays robot
    - copy this repo to that environment
        - rsync over ssh of full directory
    - test some rest api's of the ays rest server
    - let build group know that there is a AYS cockpit for this build env, post the url
    - allow all users from build_group in itsyou.online to access the cockpit

- for bootstrap:
    - this repo is run from any jumpscale enabled PC who has also the build zerotier network connected to
    - once we have the cockpit installed, this bootstrap is no longer needed & we can continue to do the builds on the cockpit pc

#### build run's

- once the cockpit is deployed we can continue here to do builds: "AYS build env"

- if required, the KVM build node can be destroyed & re-installed
    - should be simple destroy/install action on that ays instance

- the ays build tree is used to build all on the KVM build node as defined above
    - is using cuisine, docker, ... (prob in future will be using our corex as well but not yet)
    - the files are pushed to IPFS (hashes stored in plist)

- the result of building 1 app or all apps is a plist which is put in the AYS template dir
    - today we have prob only 1 plist, but in future can be more
    - store the plist in all relevant dirs of all relevant apps in AYS template repo
    - make sure we support multiple branches

- as part of the build process some tests are done
    - for each relevant app & other testing apps
        - start a coreX
        - start the required apps, see that they start (can be defined in the build tree)
        - define some tests (also in the build ays tree)
    - this can happen in parallel because multiple core0's are available

- while doing building / testing report on telegram build group
    - if issue make sure everyone on telegram group knows there is an issue

- once all tests ok copy full AYS templates repo to IPFS (without .git directory): OPTIONAL
    - store hash in root of this AYS template dir

- commit info to AYS template repo, & push to git

#### apps know their plist

- result is that each app we install from that AYS template repo has the right plist attached to it
- for now it means we have lots of duplication but that is ok

#### ays repo is known in IPFS by 1 hash

- the IPFS hash in the ays repo allows anyone to see the templates by starting from nothing more than hash


# PHASE 2

### ZeroOS grid: AYS process (REPO_ZeroOS_GRID_X)

- this REPO_ZeroOS_GRID_X is owned by the person who owns the resources (has access to the mgmt network)
- this repo is run from any jumpscale enabled PC who has also the zerotier network connected to
- define ZeroOS mgmt network
    - params
        - zerotier network id
        - passwd as used in redis
- define all required ZeroOS Node instance which is child of ZeroOS mgmt network
    - params:
        - zerotier ip addr
    - monitoring:
        - read from redis to see if can access it over zerotier network
        - check total load system on redis (PHASE2) of the node
- on one of the ZeroOS Node's start
    - AYS rest
- define an AYS app or AYS solution
    - in the AYS template there will be the plist to be used
    - params
        - required mem, required CPU capacity, ...
    - the install step will create a ZeroOS container with right plist
        - call the redis on the appropriate core0 and ask for container with right resources
    - the start tesp will ask ZeroOS container
        - to start all required apps (apps are on the fuse FS)
    - the monitor step will do the monitoring of the app
