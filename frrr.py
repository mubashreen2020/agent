import os
print("enter total number of interface do you have")
no_interface=input()
no_int=int(no_interface)
for i in range(0,no_int):
   print(f"enter your interface name[{i}]")
   interface_name=input()
    with open("/etc/sysctl.conf","a") as f:
       f.write(f"\nnet.mpls.conf.{interface_name}.input=1")
with open("/etc/sysctl.conf","a") as f:
         f.write(f"\nnet.mpls.platform_labels=100000")
  
#***************Install service files*****************
print(os.system(f"sudo install -m 644 tools/frr.service /etc/systemd/system/frr.service"))
print(os.system(f"sudo systemctl enable frr"))

  
#*******************edit daemons********************
fin=open("/etc/frr/daemons","rt")
data=fin.read()
data=data.replace('=no','=yes')
fin.close()
fin=open("/etc/frr/daemons","wt")
fin.write(data)
fin.close()
with open("/etc/frr/daemons","a") as f:
  f.write("\nwatchfrr_enable=yes")

#*************start frr service*******************
print(os.system(f"sudo systemctl start frr"))
print(os.system(f"sudo systemctl status frr"))
