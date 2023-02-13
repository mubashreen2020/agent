import requests

def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("https://api.ipify.org")
    public_ip = response.text
    
    return public_ip

public_ip = get_public_ip()
print(public_ip)

