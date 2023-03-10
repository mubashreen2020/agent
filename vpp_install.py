import os
print(os.system(f"sudo apt install nasm xmlto asciidoc perl python3 clang make python-cffi python-pycparser python-ply build-essential -y"))
print(os.system(f"git clone -b stable/2106 https://github.com/FDio/vpp ~/vpp.2106"))
print(os.system(f"cp -r vpp.2106 vpp"))
fin=open("vpp/src/vpp-api/python/CMakeLists.txt","rt")
data=fin.read()
data=data.replace('find_package(PythonInterp 2.7)','find_package(PythonInterp 3)')
fin.close()
fin=open("vpp/src/vpp-api/python/CMakeLists.txt","wt")
fin.write(data)
fin.close()
fin=open("vpp/src/vpp-api/python/CMakeLists.txt","rt")
data=fin.read()
fin.close()
fin=open("vpp/src/vpp-api/python/CMakeLists.txt","wt")
fin.write("list(APPEND Python_ADDITIONAL_VERSIONS 3.9 3.8 3.7 3.6)")
fin.close()
fin=open("CmakeLists.txt","a")
fin.write(data)
fin.close()
os.chdir('vpp')
print(os.system(f"sudo make"))
print(os.system(f"sudo make install-dep"))
print(os.system(f"sudo make install-ext-deps"))
print(os.system(f"sudo make build-release"))
print(os.system(f"sudo make pkg-deb"))
os.chdir('build-root')
print(os.system(f"ls *.deb"))
print(os.system(f"dpkg -i *.deb"))
print(os.system(f"systemctl status vpp"))
print(os.system(f"sudo vppctl"))
