import requests

def get_public_ip():
    # Make a request to a public IP address API
    response = requests.get("http://checkip.dyndns.org").text
    # Extract the public IP address from the response
    public_ip = response.split("<body>")[1].split("</body>")[0].strip()
    
    return public_ip

public_ip = get_public_ip()
print(public_ip)
