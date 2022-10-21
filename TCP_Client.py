import socket
import sys

try:
    import tqdm
    progBarUsable = 1
except ImportError:
    print("tdqm not avaialable. No Progress bars for you :(")
    progBarUsable = 0

if(len(sys.argv) == 1):
    filename = "fileToSend.txt"
    raspberryPIP = "10.108.41.143"
    laptopIP = "10.104.147.105"
    port = 50001
else:
    filename = sys.argv[3]
    raspberryPIP = sys.argv[1]
    port = sys.argv[2]
    laptopIP = "10.104.147.105"


filename = "fileToSend.txt"
file = open(filename)

#Reading Size of file
filesize = file.read(4)#Using base 16
print(int(filesize,base=16))

#Reading File Name
fileTitle = file.read(20)
print("Sending:",fileTitle)



BUFFER_SIZE = 8192

#Create Progress Bar, if able to
if(progBarUsable):
    progress = tqdm.tqdm(range(int(filesize,base=16)), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

#Set up client and connect to server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
backlog = 1
mySock = s.connect((raspberryPIP,port))#The server

#Transfer data and update progress bar
s.sendall(filesize.encode("UTF-8"))
progress.update(4)
s.sendall(fileTitle.encode("UTF-8"))
progress.update(20)


while True:
        # read the bytes from the file
        bytes_read = file.read(BUFFER_SIZE)
        if(progBarUsable):
            progress.update(len(bytes_read))
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read.encode("UTF-8"))
        # update the progress bar
        

print("Transmission Complete!")
mySock.close()
s.close()
progress.close()
file.close()
