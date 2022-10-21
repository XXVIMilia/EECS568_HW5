import socket

try:
    import tqdm
    progBarUsable = 1
except ImportError:
    print("tdqm not avaialable. No Progress bars for you :(")
    progBarUsable = 0

filename = "fileToSend.txt"
file = open(filename)

#Reading Size of file
filesize = int(file.read(4),base=16)#Using base 16
print(filesize)

#Reading File Name
fileTitle = file.read(20)
print("Sending:",fileTitle)



BUFFER_SIZE = 8192

#Create Progress Bar, if able to
if(progBarUsable):
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

#Set up client and connect to server
desktopIP = "10.104.242.163"
laptopIP = "10.104.147.105"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
backlog = 1
mySock = s.connect((desktopIP,50001))#The server

#Transfer data and update progress bar
s.sendall(filesize)
progress.update(4)
s.sendall(fileTitle)
progress.update(20)


while True:
        # read the bytes from the file
        bytes_read = file.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        if(progBarUsable):
            progress.update(len(bytes_read))

print("Transmission Complete!")
mySock.close()
s.shutdown(socket.SHUT_RDWR)
progress.close()
