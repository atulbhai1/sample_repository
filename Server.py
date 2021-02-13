import socket
s = socket.socket()
s.bind(('localhost', 9999))
s.listen(1)
c, addr = s.accept()
while True:
    mess = input('Message: ')
    if mess == 'close':
        c.close()
        print('closed')
    c.send(bytes(mess, 'utf-8'))
    print(c.recv(1024).decode())
    c.close()


