import os
import json
def ip_block():
    f = open("firewallrules.json", "r")
    y = json.load(f)
    f.close
    if("bannedip" in y):
       print("yes")
       if(y["bannedip"]):
         bannedip=y["bannedip"]
         for i in bannedip:
           print(os.system(f"ufw deny from {i}"))
       else:
         print("no ip to block")
    if("bannedport" in y):
       if(y["bannedport"]):
          bannedport=y["bannedport"]
          for i in bannedport:
             
             print(os.system(f"sudo ufw deny {i}"))
       else:
          print("No port to block")

    if("allowedip" in y):
       
       if(y["allowedip"]):
         allowedip=y["allowedip"]
         for i in allowedip:
           print(os.system(f"ufw allow from {i} proto tcp to any port 22"))
       else:
         print("no ip to allow")
    
    if("allowedport" in y):
       if(y["allowedport"]):
          allowedport=y["allowedport"]
          for i in allowedport:
    
             print(os.system(f"sudo ufw deny {i}"))
       else:
          print("No port to allow")

ip_block()
