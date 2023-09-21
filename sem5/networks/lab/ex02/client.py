import socket

s=socket.socket()

s.connect(("localhost",9999))

s.send("Hello world!".encode())

data = s.recv(1024).decode()

print("received",data)

s.close()