import os
status = os.system(f"sudo service openvpn status server")
print(status)
with open(r'/var/log/openvpn/openvpn.log','r') as f:
  lines = f.readlines()

  for row in  lines:

    if row.find("remote address:") !=-1:
      out1 = row.split()
      remote_address = out1[6]
      remote = remote_address.split("]")
      remote_addr = remote[-1]
      print("remote wan ip address:", remote_addr)

    if row.find("bound") !=-1:
      out = row.split()
      local_address = out[4]
      local = local_address.split("]")
      local_addr = local[-1]
      print("local wan ip address:", local_addr)
      
    if row.find("add dev") !=-1:
      out = row.split()
      local_tun = out[6]
      print("local tunnel ip address:", local_tun)
      peer_tun = out[8]
      print("peer tunnel ip address:", peer_tun)
