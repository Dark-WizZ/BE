import socket

s = socket.socket()

s.connect(('localhost',1234))

data = input("->")

while data!='bye':
  s.send(data.encode())
  data = s.recv(1024).decode()
  print("server: ",data)
  data = input("->")
s.close()