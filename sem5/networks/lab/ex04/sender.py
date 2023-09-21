import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cmd = 'notepad'
s.sendto(cmd.encode(),('localhost',8080))