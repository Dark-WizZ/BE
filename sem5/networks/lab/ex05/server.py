import socket

ips = ['198.43.1.8','198.43.1.9','198.43.2.1']
macs = ['D3:34:55:A2','A1:98:0B:6F','C2:66:9B:F0']

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',8090))
data, addr = s.recvfrom(1024)
ip = data.decode()

if ip in ips:
    print('IP Address: ',ip)
    print('MAC Address: ',macs[ips.index(ip)])
else:
    print("IP Address not found!")