import json
from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
data = str.encode('data')
udp_socket.sendto(data, ('0.0.0.0', 5050))
data, server = udp_socket.recvfrom(1024)
data = json.loads(data.decode())
print(data['ip'])
udp_socket.close()
