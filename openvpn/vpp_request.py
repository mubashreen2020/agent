from vpp_papi import VppConnection, VppMsgProxy

conn = VppConnection()
conn.connect()

proxy = VppMsgProxy(conn)

# Get the current version of VPP
version = proxy.vpe_api_version()

print("VPP Version:", version.program, version.version)
