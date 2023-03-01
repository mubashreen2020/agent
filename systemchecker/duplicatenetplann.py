#!/usr/bin/env python3

import os
import sys
import subprocess

def check_duplicate_sections():
    config_file = '/etc/netplan/*.yaml'
    try:
        output = subprocess.check_output(['grep', '-r', '-i', 'network:', config_file], universal_newlines=True)
        sections = {}
        for line in output.split('\n'):
            if 'network:' in line:
                filename, section = line.split(':', 1)
                section_name = section.strip().replace('network:', '').replace(' ', '')
                if section_name in sections:
                    print('Duplicate section found in file {}: {}'.format(filename, section_name))
                else:
                    sections[section_name] = filename
    except subprocess.CalledProcessError:
        print('Failed to read netplan configuration files')
        sys.exit(1)

if __name__ == '__main__':
    check_duplicate_sections()
