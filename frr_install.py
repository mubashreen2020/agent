import os

#************install dependencies****************

print(os.system(f"sudo apt-get install git libgnutls28-dev autoconf automake libtool make cmake libreadline-dev texinfo pkg-config libpam0g-dev libjson-c-dev bison flex libc-ares-dev python3-dev python3-sphinx install-info build-essential libsnmp-dev perl libcap-dev libelf-dev libunwind-dev libpcre2-dev libsystemd-dev -y"))
q='"'
print("if no error type yes else no")
cont=input()
if(cont=='yes'):
#************install libyang****************************

  print(os.system(f"git clone https://github.com/CESNET/libyang.git"))
  os.chdir('libyang')
  print(os.system(f"git checkout v2.0.0"))
  print(os.system(f"mkdir build"))
  os.chdir('build')
  print(os.system(f"cmake -D CMAKE_INSTALL_PREFIX:PATH=/usr -D CMAKE_BUILD_TYPE:String={q}Release{q} .."))
  print(os.system(f"make"))
  print(os.system(f"sudo make install"))
  os.chdir('..')
  os.chdir('..')
  #*************install protobuf-c-compiler*************************
  print("if no error type yes else no")
  cont1=input()
  if(cont1=='yes'):
    print(os.system(f"sudo apt-get install protobuf-c-compiler libprotobuf-c-dev -y"))

#********************install ZeroMQ**************************

    print(os.system(f"sudo apt-get install libzmq5 libzmq3-dev -y"))

#************************Creating groups & users for frr*********************

    print(os.system(f"sudo groupadd -r -g 92 frr"))
    print(os.system(f"sudo groupadd -r -g 85 frrvty"))
    print(os.system(f"sudo adduser --system --ingroup frr --home /var/run/frr/ --gecos {q}FRR suite{q} --shell /sbin/nologin frr"))
    print(os.system(f"sudo usermod -a -G frrvty frr"))

#*******************install FRR ***************************

    print(os.system(f"git clone https://github.com/frrouting/frr.git frr"))
    os.chdir('frr')
    print(os.system(f"sudo ./bootstrap.sh"))
    print(os.system(f"sudo ./configure --prefix=/usr --includedir=/usr/include --bindir=/usr/bin --sbindir=/usr/lib/frr --libdir=/usr/lib/frr --libexecdir=/usr/lib/frr --localstatedir=/var/run/frr --sysconfdir=/etc/frr --with-moduledir=/usr/lib/frr/modules --with-libyang-pluginsdir=/usr/lib/frr/libyang_plugins --enable-configfile-mask=0640 --enable-logfile-mask=0640 --enable-snmp=agentx --enable-multipath=64 --enable-user=frr --enable-group=frr --enable-vty-group=frrvty --with-pkg-git-version --with-pkg-extra-version=-MyOwnFRRVersion"))
    print("if no error type yes else no")
    cont2=input()
    if(cont2=='yes'):
      print(os.system(f"make"))
      print(os.system(f"sudo make install"))

#******************Install FRR configuration files*************

      print(os.system(f"sudo install -m 775 -o frr -g frr -d /var/log/frr"))
      print(os.system(f"sudo install -m 775 -o frr -g frrvty -d /etc/frr"))
      print(os.system(f"sudo install -m 640 -o frr -g frrvty tools/etc/frr/vtysh.conf /etc/frr/vtysh.conf"))
      print(os.system(f"sudo install -m 640 -o frr -g frr tools/etc/frr/frr.conf /etc/frr/frr.conf"))
      print(os.system(f"sudo install -m 640 -o frr -g frr tools/etc/frr/daemons.conf /etc/frr/daemons.conf"))
      print(os.system(f"sudo install -m 640 -o frr -g frr tools/etc/frr/daemons /etc/frr/daemons"))

#*****************8Tweak sysctls*********************

      with open("/etc/sysctl.conf","a") as f:
        f.write(f"\nnet.ipv4.ip_forward=1\nnet.ipv6.conf.all.forwarding=1\n")
      print(os.system(f"sysctl -p"))

#*****************Add MPLS kernel modules*************

      with open("/etc/modules-load.d/modules.conf","a") as f:
        f.write(f"\nmpls_router\nmpls_iptunnel")
      print(os.system(f"sudo modprobe mpls-router mpls-iptunnel"))

#**************Enable MPLS Forwarding*************************

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

  else:
    exit()
else:
  exit()   
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
