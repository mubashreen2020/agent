#!/usr/bin/env python3

import os
import sys
import glob

def check_duplicate_sections():
    """
    Checks for duplicate Netplan sections in Linux.
    """
    netplan_files = glob.glob("/etc/netplan/*.yaml")
    sections = {}

    for file in netplan_files:
        with open(file, "r") as f:
            lines = f.readlines()

            for i in range(len(lines)):
                if lines[i].startswith("  "):
                    section_name = lines[i-1].strip().replace(":", "")
                    if section_name in sections:
                        print("Duplicate section found in {}:".format(file))
                        print("  {}".format(section_name))
                        sys.exit(1)
                    else:
                        sections[section_name] = True

if __name__ == "__main__":
    check_duplicate_sections()
    print("No duplicate sections found.")
