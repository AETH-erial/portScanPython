###PYTHON 3.9###

from asyncio.windows_utils import BUFSIZE
from curses.ascii import ACK, SYN
from re import S
import socket
import sys

ports = list()
ports.__add__(20, 21, 22) #etc

def serverUp():
    hostname = socket.gethostname()
    server = socket.create_server(hostname, family=socket.AF_INET, dualstack_ipv6=True)
    
class socket:
    def __init__(self, sock=None):
        if sock is None:
            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))
        
    def listen(self, s):
        self.sock.listen(s)
        
    



def portScan(port, ip):
    
    for port in ports:
        sock = socket
        s = sock.connect((ip, port))
        sock.listen(s)
        buff, flag = s.recv(BUFSIZE, sys.flags)
        if flag == SYN:
            s.send(16[ACK])
        else:
            print("ERROR CREATING CONNECTION TO PORT", port)
                
