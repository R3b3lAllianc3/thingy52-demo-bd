import aci.aci_cmd as cmd
import time

def database_restore(database, device_instance):
    device_instance.send(cmd.AddrLocalUnicastSet(device_instance.local_unicast_adress_start, 1))

    for key in database.net_keys:
        device_instance.send(cmd.SubnetAdd(key.index, key.key))

    for key in database.app_keys:
        device_instance.send(cmd.AppkeyAdd(key.index, key.bound_net_key, key.key))


def provisioned_device_data_restore(database, device_instance):
     for node in database.nodes:
        device_instance.send(cmd.DevkeyAdd(node.unicast_address, 0, node.device_key))
        device_instance.send(cmd.AddrPublicationAdd(node.unicast_address))

def restore_system_at_startup(database, device_instance):
	database_restore(database, device_instance)
	time.sleep(0.5)
	provisioned_device_data_restore(database, device_instance)
	device.send(cmd.AddrPublicationAdd(address=0xC001))
	
	

	
		