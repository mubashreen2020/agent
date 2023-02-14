import os

def check_rules():
    # Run the command to get the list of firewall rules
    output = os.popen("iptables -L").read()

    # Check if the desired rules are present in the output
    if "your_rule_1" in output and "your_rule_2" in output:
        print("Rules are enabled")
    else:
        print("Rules are not enabled")

# Call the check_rules function
check_rules()
