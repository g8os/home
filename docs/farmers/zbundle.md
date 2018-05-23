## Registering capacity to the TF grid with hardward not using 0-OS
It is possible to already register some hardware on the grid even if the hardware is not yet running 0-OS.

This tool can be used when the farmer is planning to add capacity to the grid but for some reason still need to keep his hardware running something else then 0-OS time being.

Here is how to do:
1. download zbundle: here is the link: https://download.gig.tech/zbundle
2. register as a farmer: check the documentation [how to become a farmer](README.md#register-as-a-farmer)
3. run this command on your nodes: 
```
sudo zbundle -id capacity -e FARMER_ID={FARMER_ID} https://hub.gig.tech/zaibon/zbundle_capacity.flist
```
`{FARMER_ID}` being the ID received in step 2 after you register as a farmer

4. once the zbundle is done registering the capacity, you should see you nodes capacity at: https://capacity.threefoldtoken.com/