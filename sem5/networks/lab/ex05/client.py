import socket

ip = '198.43.1.9'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('IP -> ',ip)
s.sendto(ip.encode(),('localhost',8090))