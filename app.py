import json, sys
from textwrap import indent

config = {
    "pathToKeystore": "~/dev/keystores/",
    "defaultUser": "ubuntu",
    "generatedConfigs": "output/"
}

with open('aws.json') as f:
    vms = json.loads(f.read())

for vm in vms['Reservations']:
    vm_instances = vm['Instances']
    
    for instance in vm_instances: 
        # print(instance["Tags"])
        
        # for tag in instance["Tags"]:
        #     if tag['Key'] == 'Name':
        #        print(f'Instance: {tag["Value"]}') 
        
        # get/set InstanceId:
        instanceID = instance["InstanceId"]
        print(f'\n\ninstanceID')

        # get/set Host:
        try:
            hostObject = next((item for item in instance["Tags"] if item["Key"] == "Name"), None)
            hostFor = hostObject["Value"]
        except:
            hostFor = "EHostFor"
        finally:
            print(f'hostFor: {hostFor}')
            
        try:   
            hostObject2 = next((item for item in instance["Tags"] if item["Key"] == "nick"), None)
            if hostObject2 == None:
                hostObject2 = hostObject
            host = hostObject2["Value"]
        except:
            host = "EHost"
        finally:
            print(host)

        # get/set HostName:
        try:
            hostName = instance["PublicIpAddress"]
        except:
            hostName = None
        finally:
            print(hostName)

        # networkInterfaces = instance["NetworkInterfaces"]
        # associations = next((item for item in instance["NetworkInterfaces"] if item["Association"]), None)
        # hostName = associations['Association']["PublicIp"]
        print(hostName)

        # derive User:
        user = config["defaultUser"]
        print(user)

        # set IdentityFile
        try:
            keyName = f'{instance["KeyName"]}.pem'
        except:
            keyName = None
        finally:
            print(keyName)


        # set any other param

        # write to config  
        with open(f'{config["generatedConfigs"]}sshd.conf', 'a') as f:
            f.write(f'\n# For: {host}')
            f.write(f'\nHost {host}')
            f.write(f'\n  HostName {hostName}')
            f.write(f'\n  User {user}')
            f.write(f'\n  IdentityFile {config["pathToKeystore"]}{keyName}\n')

    # sys.exit()