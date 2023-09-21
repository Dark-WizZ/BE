import wmi, socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',8080))
data,addr = s.recvfrom(1024)
cmd=data.decode()
print('opening',cmd)
conn = wmi.WMI()
conn.Win32_Process.Create(CommandLine=cmd)