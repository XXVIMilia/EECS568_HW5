import socket
import sys

if(len(sys.argv) == 1):
    filename = "receivedFile.txt"
    raspberryPIP = "10.108.41.143"
    laptopIP = "10.104.147.105"
    port = 50001
else:
    filename = "receivedFile.txt"
    raspberryPIP = "10.108.41.143"
    laptopIP = "10.104.147.105"
    port = sys.argv[1]

port = 50001
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((raspberryPIP,port))

BUFFER_SIZE = 8192

file = open("receivedFileUDP.txt",mode='w')
while(True):
    received, addr = s.recvfrom(BUFFER_SIZE)
    
    if received.decode() == "eof":
        break

    file.write(received.decode())
    

s.close()
file.close()