import socket

s = socket.socket()
s.connect(('localhost',8080))
filename = input("Enter the filename: ")
data = s.recv(1024)
file = open(filename,'wb')
file.write(data)
s.close()