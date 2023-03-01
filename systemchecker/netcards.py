import os

def get_supported_network_cards():
    supported_cards = []
    command_output = os.popen("ethtool -i $(ls /sys/class/net/)").read()
    lines = command_output.split("\n")
    for line in lines:
        if "driver" in line:
            driver = line.split(":")[1].strip()
        elif "bus-info" in line:
            bus_info = line.split(":")[1].strip()
            supported_cards.append((driver, bus_info))
    return supported_cards

if __name__ == "__main__":
    print("Supported network cards in Linux:")
    cards = get_supported_network_cards()
    for card in cards:
        print(f"{card[0]} ({card[1]})")
