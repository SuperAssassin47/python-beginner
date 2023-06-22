import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('192.168.27.36', 100))
if result == 100:
    print('PORT IS OPEN')
else:
    print('NO PORTS ARE OPEN')
