import os
ipsec_stat=os.system(f"pgrep ipsec")
if ipsec_stat==256:
  print(os.system(f"sudo apt install strongswan -y"))
print("enter local public ip")
local_publicip = input()
print("enter local subnet")
local_subnet = input()
print("enter remote public ip")
remote_publicip = input()
print("enter remote subnet")
remote_subnet = input()
print("enter connection name")
conn_name = input()
print("enter PSK for mutual authentication")
psk_key = input()
q='"'
with open("/etc/sysctl.conf","a") as f:
  f.write(f" net.ipv4.ip-forward = 1 \n net.ipv4.conf.all.accept_redirects = 0 \n net.ipv4.conf.all.send_redirects = 0")
with open("/etc/ipsec.secrets", "a") as f:
  f.write(f"\n{local_publicip} {remote_publicip} : PSK {q}{psk_key}{q}")
with open("f"/etc/ipsec.conf", "a") as f:
  f.write(f"config setup \n \t charondebug={q}all{q} \n \t uniqueids=yes \n \t strictcrlpolicy=no \n \n conn {conn_name} \n \t authby=secret \n \t left=%defaultroute \n \t leftid={local_publicip} \n \t leftsubnet={local_subnet} \n \t right={remote_publicip} \n \t remotesubnet={remote_subnet} \n \t ike=aes256-sha2_256-modp1024! \n \t esp=aes256-sha2_256! \n \t keyingtries=0 \n \t ikelifetime=1h \n \t lifetime=8h \n \t dpddelay=30 \n \t dpdtimeout=20 \n \t dpdaction=restart \n \t auto=start") 
print(os.system(f"sudo iptables -t nat -A POSTROUTING -s {remote_subnet} -d {local_subnet} -j MASQUERADE"))
print(os.system(f"ipsec restart"))
print(os.system(f"ipsec up {conn_name}))
print(os.system(f"ipsec status"))