from re import S
import socket

try:
    import tqdm
    progBarUsable = 1
except ImportError:
    print("tdqm not avaialable. No Progress bars for you :(")
    progBarUsable = 0

filename = "fileToSendUDP.txt"
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

#Set up client
raspberryPIP = "10.108.41.143"
laptopIP = "10.104.147.105"
port = 50001
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.sendto(filesize.encode("UTF-8"), (raspberryPIP, port))

#Transfer data and update progress bar
s.sendto(filesize.encode("UTF-8"), (raspberryPIP, port))
progress.update(4)
s.sendto(filename.encode("UTF-8"), (raspberryPIP, port))
progress.update(20)


while True:
        bytes_read = file.read(BUFFER_SIZE)
        if(progBarUsable):
            progress.update(len(bytes_read))
        if not bytes_read:
            break
        s.sendto(bytes_read.encode("UTF-8"), (raspberryPIP, port))
        # update the progress bar
        

print("Transmission Complete!")

s.close()
progress.close()
file.close()