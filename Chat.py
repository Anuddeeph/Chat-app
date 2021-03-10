import socket 
from threading import *

def receive(ip,port):
    myp = socket.SOCK_DGRAM 
    afn = socket.AF_INET 
    s = socket.socket(afn,myp) 
    s.bind((ip,port)) 
    while True:
        x = s.recvfrom(1024) 
        print("\t\t\tReceived Message: ",x[0].decode())
        
def send(ip,port):
    myp = socket.SOCK_DGRAM 
    afn = socket.AF_INET 
    s = socket.socket(afn,myp) 
    while True:
        msg = input() 
        s.sendto(msg.encode(), (ip,port))

WinIP = input("Enter your IP: ") 
WinPort = int(input("Enter your Port: ")) 
LinIP = input("Enter target IP: ") 
LinPort = int(input("Enter target Port: "))

print("-----------Welcome to Python Chat------------")

receiveThread = Thread( target = receive , args = (WinIP,WinPort)) 
senderThread = Thread( target = send , args = (LinIP,LinPort))

receiveThread.start()
senderThread.start()
