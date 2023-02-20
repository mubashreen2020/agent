import os
status = os.system(f"sudo service openvpn status server")
print(status)
#logs = os.popen("openvpn --status /var/log/openvpn/openvpn.log").read()
#print(logs)
#lines = logs.split("\n")
#print(lines)
with open(r'/var/log/openvpn/openvpn.log','r') as f:
  lines = f.readlines()
  for row in  lines:
    if row.find("remote address:") !=-1:
      print(row)
      remote_address=row
    if row.find("local") !=-1:
      local = row
      print(local)
      out = local.split()
      print(out)
      
      
