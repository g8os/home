# Threefold farmers documentation

## Summary
- [register as a farmer](#register-as-a-farmer)
- [setup your farm](#setup-your-farm)
- [configure your nodes](#configure-your-nodes)

### Register as a farmer
#### Create an IYO account
The first step to take in order to become a farmer is to register on [ItsYouOnline](http://itsyou.online/).
To do so, head to http://itsyou.online/ and follow the sign-in procedure.

#### Create an organization
A farm is link to an organization on IYO, so after you register yourself, you also need to create an organiztion for your farm.

#### Register as a farmer
Head to https://capacity.threefoldtoken.com and click on the top right button `Register a farm` to register your farm.  
The form has 3 fields:
- The name of your farm: this can be anything, the name will be displayed next to your node in the listing of the capacity
- Organization: the global ID of the organization you created in the previous step.
- a TFT wallet address: optionally you can also link a tft wallet address to your farm.

The result of your registration will be a token. Make sure to copy this token and keep it, cause you will need it later in the process of setting up your nodes.


### Setup your farm
Still in development. We are planning to also offer farmers with a robot that will manage all the nodes in their farm.
This robot will be able to turn on/off the nodes so the farm stays as green as possible, easily configure the kernel the node are booting, and many more useful features. Stays tuned

### Configure your nodes
#### Download the 0-OS kernel for you nodes

Go to https://bootstrap.gig.tech/generate to create the kernel image you need to boot your node.
The generaor will guide you though the steps.
- **Step 1 Choose the 0-OS version**: The current lastest release of 0-os is `v1.2.2`
- **Step 2 Choose the zerotier network**: To make things easy for now, all the nodes will belong to the same zerotier network.
The network ID of this network is: `c7c8172af1f387a6`
- **Step3 Custom kernel parameters**: In this step you will link your farmer id with your node, so in the capacity directory, we can see which nodes belongs to which farmer.   
The argument you need to add in this step is `farmer_id={Farmer_JWT}`, `{Farmer_JWT}` beeing the token you received during signing in as a farmer earlier
- **Step 4 Choose your install medium**: Depending how you boot your node, choose the installation medium that fits your need.
- **Step 5 Boot your node**: After you have dowloaded your kernel, just boot you node and head to https://capacity.threefoldtoken.com/ to see your node beeing register in the grid