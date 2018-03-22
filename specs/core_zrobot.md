
## core z-robot principles


- hardcoded boot in z-core
- boot an flist in container which provides provisioning for the primitives
- is the only robot who can access the core-0 redis

### implement core primitives

- zdb
- vm ubuntu/zos
- z-gw
- z-robot

### security of robot step 1 (which is now)

- jwt from IYO from an organization

### specs of the blueprints see

- TODO: *1 specs for the blueprints

### 3 boot modes

- zerotier: redis listening on zerotier network only
- debug: redis listening on all interfaces
- production: redis only listens internally and can get instructions only from core z-robot, z-robot listens to zerotier

