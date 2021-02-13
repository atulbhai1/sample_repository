import socket
c = socket.socket()
c.connect(('localhost', 9999))
while True:
    print(c.recv(1024).decode())
    c.send(bytes(input('Message: '), 'utf-8'))


