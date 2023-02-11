import socket

def connect_to_frr():
    frr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    frr_socket.connect(("127.0.0.1", 2605))

    frr_socket.sendall(b"sh ip bgp\n")

    data = frr_socket.recv(4096)
    frr_socket.close()

    return data

print(connect_to_frr().decode("utf-8"))
