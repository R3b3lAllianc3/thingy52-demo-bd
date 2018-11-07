current_app_key = 0
node_count = 0
#prompt
#Provision Server Bulb #1
#------------------------
db = MeshDB("database/example_database.json")
db.provisioners
p = Provisioner(device, db)
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #1.0")
cc = ConfigurationClient(db)
device.model_add(cc)
cc.publish_set(8, 0)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
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
p.provision(name="Light bulb #2.0")
cc.publish_set(9, 1)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[1].unicast_address, 0, mt.ModelId(0x1000)) #bind to appkey0
cc.model_subscription_add(db.nodes[1].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001

#prompt
#Provision Server Bulb #3
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #3.0")
cc.publish_set(10, 2)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[2].unicast_address, 0, mt.ModelId(0x1000)) #bind to appkey0
cc.model_subscription_add(db.nodes[2].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001

#get handle for group subscription
device.send(cmd.AddrSubscriptionAdd(0xc001))
#handle should be 3
gc_Group = GenericOnOffClient()
device.model_add(gc_Group)

#prompt
#Provision Server Bulb #4
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #4.0")
cc.publish_set(11, 4)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[3].unicast_address, 1, mt.ModelId(0x1000)) #bind to appkey1
cc.model_subscription_add(db.nodes[3].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001

#prompt
#Provision Server Bulb #5
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #5.0")
cc.publish_set(12, 5)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[4].unicast_address, 1, mt.ModelId(0x1000)) #bind to appkey1
cc.model_subscription_add(db.nodes[4].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001

#prompt
#Provision Server Bulb #6
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #6.0")
cc.publish_set(13, 6)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[5].unicast_address, 1, mt.ModelId(0x1000)) #bind to appkey1
cc.model_subscription_add(db.nodes[5].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001

#prompt
#Provision Server Bulb #7
#------------------------
p.scan_start()
p.scan_stop()
p.provision(name="Light bulb #1.1")
cc.publish_set(13, 6)
cc.composition_data_get()
cc.appkey_add(0)
cc.appkey_add(1)
cc.model_app_bind(db.nodes[6].unicast_address, 1, mt.ModelId(0x1000)) #bind to appkey1
cc.model_subscription_add(db.nodes[6].unicast_address, 0xc001, mt.ModelId(0x1000)) #Add to group 0xC001




#Move node #6 from appkey1 group to appkey0 group
cc.model_app_unbind(db.nodes[5].unicast_address, 1, mt.ModelId(0x1000)) #unbind from appkey1
cc.model_app_bind(db.nodes[5].unicast_address, 0, mt.ModelId(0x1000)) #bind to appkey0

#Test groups showing node 6 is part of appkey0 group
gc_Group.publish_set(0, 3) #second parameter from above "AddrSubscriptionAdd" and first is appkey
gc_Group.set(True)
gc_Group.set(False)
gc_Group.publish_set(1, 3) #second parameter from above "AddrSubscriptionAdd" and first is appkey
gc_Group.set(True)
gc_Group.set(False)


