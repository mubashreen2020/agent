import requests

def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("http://checkip.dyndns.org").text
    
    # Extract the public IP address from the response
    public_ip = response.strip().split(" ")[-1]
    
    return public_ip

# Get the public IP address
public_ip = get_public_ip()

print(public_ip)
