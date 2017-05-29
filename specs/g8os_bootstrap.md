
## process

### boot

- if physical
    - secure boot boots kernel & 0-core from USB stick
- if Virtualbox
    - secure boot boots kernel & 0-core from VM image
- if openvcloud (same as VB)
- packet.net
    - ?define

### boot & optionaly update 0-core

- 0-core starts network stack
    - checks for dhcp server, if found get IP address
        - see if we can connect internet, if ok go to reading of bootstrap_0.yaml which is in image or usb stick
    - bootstrap0
        - link to github location with login/passwd?
    - if no internet or no dhcp server:
        Currently fallback when no DHCP is to set a random IP from a static range. But this is not good enough for our use case. Need to be further defined.
        For now we'll only support DHCP
- 0-core components on stick or VM image
    - signed linux Kernel that contains an initramfs. in the initramfs we have IPFS, and 0-core. our fuse FS will be bundled into the binary of 0-core.
- check on USB stick or VM image
    - bootstrap.yaml has config info for boot process
    - Need to come up with a better scheme, more secure. For development we can use one of our server, but will need to improve.
    - Goal is to be able to connect a remote location that we can update easily to change default configuration and hash of new version of the 0-core
    - $githuburl is specified in bootstrap.yaml
- 0-core reads bootstrap_{arch}.yaml file from github url
    - $githuburl/bootstrap_i64.yaml
    - $githuburl/bootstrap_arm64.yaml (phase2)
- bootstrap.yaml has following metadata
    - zerotier network to attach too
    - IPFS hash of 0-core + additional components for current platform
    - IPFS hash to the 0-core plist for all files required to boot the 0-core with required files (as few as possible)
        - e.g. redis
        - e.g. busybox?
        - e.g. tools required to run our own containers (corex...)
        - e.g. zerotier network
    - ???
    - what is not in the plist (DOT NOT PUT IT IN THE PLIST)
        - mc/git/ssh/...
- 0-core checks hash of own booted core0 with hash of the ones specified in the bootstrap...yaml file
    - if hash different, download a complete new kernel image. The kernel image contains the kernel + initramfs, everything packaged together. This is the « only » way to ensure that initramfs is trusted and not corrupted with the kernel (everything is signed and checked from secureboot)


### 0-core (after update)
- 0-core will start as PID1 and then mount a plist that contains all the remaining component it needs. This also allow an easy way to update components.
- connects to zerotier network
- make sure is all readonly
- start redis with password as specified in the bootstrap*.yaml file, and redis only connects to the zerotier network
- start the logic which is reading from redis to execute on specified commands: #TODO: *1 specs are where?
