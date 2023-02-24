import socket

def check_wifi_connectivity():
    # Try to connect to a well-known hostname or IP address on the Internet
    try:
        socket.create_connection(("8.8.8.8", 53))
        print("WiFi connectivity is available")
    except OSError:
        print("WiFi connectivity is not available")

if __name__ == '__main__':
    check_wifi_connectivity()
