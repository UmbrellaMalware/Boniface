import json
from socket import *

from loguru import logger

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(('0.0.0.0', 5050))
while True:
    conn, addr = udp_socket.recvfrom(1024)
    logger.debug(f'connection from: {addr}')
    answer = json.dumps({
        'ip': addr[0],
        'port': addr[1]
    })

    udp_socket.sendto(answer.encode(), addr)
