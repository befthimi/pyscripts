#!/usr/bin/env python3.6
'''
Write a script that takes in an IPv4 address a vrf name and forms a ping command.
'''
from __future__ import print_function, unicode_literals
import time
import socket
import sys
import getpass

try:
    ip_addr = raw_input("IP address: ")
except NameError:
    ip_addr = input("IP address: ")
ip_addr = ip_addr.strip()
vrf = input("VRF: ")
password = getpass.getpass()

print ("\n\n")
print ("ping {} vrf {}".format(ip_addr,vrf))
print ("\n\n")
