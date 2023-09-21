import socket

s=socket.socket()
s.bind(('localhost',1234))
# s.listen(1)
conn, addr = s.accept()
print("connection from ",addr)
while 1:
  data = conn.recv(1024).decode()
  if not data:
    break
  print("client: ",data)
  data  = input('->')
  conn.send(data.encode())
conn.close()
  