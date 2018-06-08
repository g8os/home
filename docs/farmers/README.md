# Setup and manage your ThreeFold farm

Steps:
- [Create an ItsYou.online organization](#iyo-org)
- [Register your farm](#register)
- [Get the Zero-OS kernel for your nodes](#zos)
- [Boot your nodes](#boot)
- [Manage your farm](#manage)


<a id='iyo-org'></a>

## Create an ItsYou.online organization

Your ThreeFold farm needs to be associated to an ItsYou.online organization. 

In order to create such an ItsYou.online organization you need an ItsYou.online account. Creating one is simple, head to http://itsyou.online/ and follow the sign-up instructions.

Once logged in to your ItsYou.online account, also creating an ItsYou.online organization is simple.

Click **Organization** from the **Profile** menu in the top right corner:
![](images/iyo-organizations.png)

Now click **+ CREATE NEW**:
![](images/iyo-create-new-org.png)

And finally specify the name of the new ItsYou.online organization and click **CREATE**:
![](images/iyo-create-new-org2.png)


<a id='register'></a>

## Register your farm

Visit https://capacity.threefoldtoken.com and click the **Register a farm** link in the top right corner to register your farm:

![](images/register-farm.png)

- **Farm Name**: this can be anything, the name will be displayed next to your node in the listing of the capacity
- **Organization ID**: the global ID of the ItsYou.online organization you created in the previous step
- **TFT Wallet Address**: optionally you can also associate a ThreeFold token wallet address to your farm

The result of your registration will be a JSON Web Token (JWT), which is your **farmer ID**. Make sure to copy this token and keep it, because you will need it later in the process of setting up your nodes.

<a id='zos'></a>

## Get the Zero-OS kernel for your nodes

Go to https://bootstrap.gig.tech/generate to create the kernel image you need to boot your node.
The generator will guide you though the steps.

- **Step 1 Choose the Zero-OS version**: The current latest release of Zero-OS is `v1.3.0`
- **Step 2 Choose the ZeroTier network**: To make things easy for now, all the nodes need to be connected to the same ZeroTier network. The ZeroTier network ID of this network is: `c7c8172af1f387a6`
- **Step3 Custom kernel parameters**: In this step you will link your farmer ID with your node, so in the capacity directory, we can see which nodes belong to which farmer.   
The argument you need to add in this step is `farmer_id={Farmer_JWT}`, `{Farmer_JWT}` being the JWT token you received during registering your farm earlier.
- **Step 4 Choose your install medium**: Depending how you boot your node, choose the installation medium that fits your need.


<a id='boot'></a>

## Boot your nodes

After you have downloaded your kernel, just boot you node and head to https://capacity.threefoldtoken.com/ to see your node being register in the ThreeFold grid.


<a id='manage'></a>

## Manage your farm

Still in development. We are planning to also offer farmers a Zero-Robot that will manage all the nodes in their farm.
This robot will be able to turn on/off the nodes so the farm stays as green as possible, easily configure the kernel to boot the node, and many more useful features. Stay tuned, or follow the work in the [0-boot-templates](https://github.com/zero-os/0-boot-templates) repository on GitHub. 