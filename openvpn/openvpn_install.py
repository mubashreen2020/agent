import os
def config():
  os.system(f"sudo mv -v /etc/openvpn/server/server.conf /etc/openvpn/server/server.conf.backup")
  print("enter remote ip for openvpn connection")
  remote_address = input()
  print("enter local ip for openvpn connection")
  local_address = input()
  print("enter tunnel name")
  tunnel_name = input()
  print("enter local tunnel ip")
  local_tunnel_ip = input()
  print("enter remote tunnel ip")
  peer_tunnel_ip = input()
  print("enter file name of psk")
  key_name = input()
  with open("/etc/openvpn/server/server.conf","w") as f
    f.write(f"proto udp \nmode p2p \nremote {remote_address} \nlocal {local_address} \nport 1194 \ndev-type tun \ntun-ipv6 \nresolv-retry infinite \ndev {tunnel_name} \ncomp-lzo \npersist-key \npersist-tun \ncipher AES-256-CBC \nifconfig {local_tunnel_ip} {peer_tunnel_ip} \nsecret /etc/openvpn/server/{key_name}.key \nlog /var/log/openvpn/openvpn.log")
  os.system(f"chmod 777 /etc/openvpn/server/server.conf")
  os.system(f"sudo rm -r /etc/openvpn/server/server.key")
  os.system(f"openvpn --genkey --secret /etc/openvpn/server/{key_name}.key")
  os.system(f"chmod 777 /etc/openvpn/server/{key_name}.key")
  print(os.system(f"sudo ufw allow 1194/udp"))
  print(os.system(f"openvpn --config /etc/openvpn/server/server.conf"))
  print(os.system(f"sudo service openvpn restart server"))
  print(os.system(f"sudo service openvpn status server"))

state = os.system(f"pidof openvpn")
st = int(state)
if st != 256 :
    print("Already openvpn is insatlled")
    print("if you want to configure again type yes")
    reconfig = input()
    if reconfig == "yes":
       config()
    else:   
      exit()
else:   
  print(os.system(f"sudo apt update"))
  print(os.system(f"sudo apt upgrade"))
  print(os.system(f"sudo apt-get install git"))
  print(os.system(f"git clone https://github.com/Nyr/openvpn-install.git"))
  os.system(f"chmod +x openvpn-install/openvpn-install.sh")
  os.system(f"./openvpn-install/openvpn-install.sh")
  config()
