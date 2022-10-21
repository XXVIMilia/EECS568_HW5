import socket


raspberryPIP = "10.108.41.143"
laptopIP = "10.104.147.105"

port = 50001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
backlog = 1


s.bind((raspberryPIP,50001))
s.listen(backlog)

BUFFER_SIZE = 8192

try:
    print("Waiting For Coneection")
    mySock, address = s.accept()#The client connected
    print("Client joined: " + address[0])
except OSError:
    print("Something Goofed, try again")
    mySock.close()
    s.shutdown(socket.SHUT_RDWR)

file = open("receivedFile.txt",mode='w')
while(True):
    received = mySock.recv(BUFFER_SIZE).decode()
    
    if not received:
        break

    file.write(received)
    

mySock.close()
s.close()
file.close()