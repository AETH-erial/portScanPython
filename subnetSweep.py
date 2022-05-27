###PYTHON 3.9###
###WORK IN PROGRESS###


import ipaddress
import socket
import subprocess, sys
from subprocess import *
hostname = socket.gethostname()
hostIP = ipaddress.IPv4Address(socket.gethostbyname(hostname))
print('{:#b}'.format(ipaddress.IPv4Address(hostIP)))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((hostIP, port))
    s.listen()
    conn, addr = s.accept()



