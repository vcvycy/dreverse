import socket
addr=("127.0.0.1",80)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)
while True:
  conn,addr=s.accept()
  #print("new conn:%s" %(addr))
  print(addr)
  data=conn.recv(1024)
  print(data)
  conn.send(b"[Server] got it")
  conn.close();
