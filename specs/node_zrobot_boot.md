
## core z-robot boot 


- hardcoded boot in z-core (only when certain flag given to boot param)
- boot an flist in container which provides provisioning for the primitives
- is the only robot who can access the core-0 redis


### security of robot step 1 (which is now)

- jwt from IYO from an organization

### 3 boot modes

- zerotier: redis listening on zerotier network only
- debug: redis listening on all interfaces
- production: redis only listens internally and can get instructions only from core z-robot, z-robot listens to zerotier

