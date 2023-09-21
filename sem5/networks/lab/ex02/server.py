import socket

s = socket.socket()

s.bind(("localhost",9999))
s.listen(1)
conn, addr = s.accept()
print("Connected to address ",addr)

data = conn.recv(1024).decode()
print("Receiced ",data)

conn.send(data.encode())

conn.close()