#prompt
#Provision Server Bulb #1
#------------------------
db = MeshDB("database/example_database.json")
db.provisioners
p = Provisioner(device, db)
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #1")
cc = ConfigurationClient(db)
device.model_add(cc)
cc.publish_set(8, 0)
cc.composition_data_get()
cc.appkey_add(0)
cc.model_app_bind(db.nodes[0].unicast_address, 0, mt.ModelId(0x1000)) #bind to appkey0
cc.model_subscription_add(db.nodes[0].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001
#following only to test server from provisioner
#gc_Bulb1 = GenericOnOffClient()
#device.model_add(gc_Bulb1)
#gc_Bulb1.publish_set(0, 0)
#gc_Bulb1.set(True)  #turn on light
#gc_Bulb1.set(False) #turn off light

#prompt
#Provision Server Bulb #2
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #2")
cc.publish_set(9, 1)
cc.composition_data_get()
cc.appkey_add(1)
cc.model_app_bind(db.nodes[1].unicast_address, 1, mt.ModelId(0x1000)) #bind to appkey1
cc.model_subscription_add(db.nodes[1].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001
#following only to test server from provisioner
#gc_Bulb2 = GenericOnOffClient()
#device.model_add(gc_Bulb2)
#gc_Bulb2.publish_set(1,1)
#gc_Bulb2.set(True)  #turn on light
#gc_Bulb2.set(False) #turn off light

#endprovisioning //temporary MQ

device.send(cmd.AddrSubscriptionAdd(0xc001))
gc_Group = GenericOnOffClient()
device.model_add(gc_Group)
gc_Group.publish_set(0, 2) #second parameter from above "AddrSubscriptionAdd" and first is appkey
#Turn on AppKey0 Group
gc_Group.set(True)
gc_Group.set(False)
gc_Group.set(True)
gc_Group.publish_set(1, 2) #second parameter from above "AddrSubscriptionAdd" and first is appkey
#Turn on AppKey1 Group
gc_Group.set(True)
gc_Group.set(False)
gc_Group.set(True)

#endprovisioning

#Add servers to the same group
#-----------------------------
cc.publish_set(8, 0)   #pick server #1 to configure
cc.model_publication_set(db.nodes[0].unicast_address, mt.ModelId(0x1000), mt.Publish(db.groups[0].address, index=0, ttl=1))
cc.publish_set(9, 1)   #pick server #2 to configure
cc.model_publication_set(db.nodes[1].unicast_address, mt.ModelId(0x1000), mt.Publish(db.groups[0].address, index=1, ttl=1))

#prompt
#Provision Client Switch
#-----------------------
p.scan_start()
p.scan_stop()
p.provision(name="Switch")
cc.publish_set(10, 2)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[2].unicast_address, 0, mt.ModelId(0x1001))
cc.model_publication_set(db.nodes[2].unicast_address, mt.ModelId(0x1001), mt.Publish(db.nodes[0].unicast_address, index=0, ttl=1))
cc.model_app_bind(db.nodes[2].unicast_address + 1, 1, mt.ModelId(0x1001))
cc.model_publication_set(db.nodes[2].unicast_address + 1, mt.ModelId(0x1001), mt.Publish(db.nodes[1].unicast_address, index=1, ttl=1))

#Dynamically switch "button 0" to turn on bulb on server #2
#----------------------------------------------------------
#Unbind switch (Client) nodes's GenOnOff Client on Element 0 from AppKey0
cc.model_app_unbind(db.nodes[2].unicast_address, 0, mt.ModelId(0x1001))

#Bind switch (Client) nodes's GenOnOff Client on Element 0 to AppKey1
cc.model_app_bind(db.nodes[2].unicast_address, 1, mt.ModelId(0x1001))

#Must publish as we were unpublished by the unbind above
cc.model_publication_set(db.nodes[2].unicast_address, mt.ModelId(0x1001), mt.Publish(db.nodes[1].unicast_address, index=1, ttl=1))

#To switch back "button 0" to turn on bulb on server #1 again...
#---------------------------------------------------------------
#Unbind switch (Client) nodes's GenOnOff Client on Element 0 from AppKey1
cc.model_app_unbind(db.nodes[2].unicast_address, 1, mt.ModelId(0x1001))

#Bind switch (Client) nodes's GenOnOff Client on Element 0 from AppKey1
cc.model_app_bind(db.nodes[2].unicast_address, 0, mt.ModelId(0x1001))

#Must publish as we were unpublished by the unbind above
cc.model_publication_set(db.nodes[2].unicast_address, mt.ModelId(0x1001), mt.Publish(db.nodes[0].unicast_address, index=0, ttl=1))
 
