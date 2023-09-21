import socket

s = socket.socket()
s.bind(('localhost',8080))
s.listen(1)
print("Waiting for connection...")
conn, addr = s.accept()
print("Connected to ",addr)
filename = input("Enter the filname to transfer: ")
file = open(filename,'rb')
conn.send(file.read())
conn.close()
print("File has send")