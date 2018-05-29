import socket
addr=("127.0.0.1",80)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(addr)
s.send(b"[client]hello,world")
print(s.recv(100));
