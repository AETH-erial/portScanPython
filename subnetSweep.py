###PYTHON 3.9###
###WORK IN PROGRESS###


import ipaddress
import socket
import subprocess, sys
from subprocess import *
import netifaces


##function to send binary addresses to, to convert it to a list
def stringToList(var1):
    for char in binAddr:
        binList.append(char)
    return var1

def firstAddr(var2, var3):
    while binHost.length > (binMask.index('0')):
        binHost.pop([-1])
    while binHost.length < (binMask.index('0')):
        binHost.append('0')
    binHost[-1] = '1'
    return binHost


##grabbing hostname address from local machine
hostname = socket.gethostname()

##resolve hostname to an IP address
hostIP = ipaddress.IPv4Address(socket.gethostbyname(hostname))

##grabbing a list of network interfaces from host machine 
netCards = netifaces.interfaces()

#isolating the first interface to resolve a netmask from
addr = netifaces.ifaddresses(netCards[1])

#assigning the netmask to the variable 'netmask', will be used later
##to infer how many addresses are on the host machines local network
netmask = ipaddress.IPv4Address(addr[2][0]['netmask'])


netMaskStringBin = '{:b}'.format(netmask)
hostStringBin = '{:b}'.format(hostIP)
binMask = binToList(netMaskStringBin)
binHost = binToList(hostStringBin)

hostStart = firstAddr(binHost, binMask)

hostStart.toString()
    
    
#getting the prefix length of the subnet mask, and adding


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((hostIP, port))
    s.listen()
    conn, addr = s.accept()

