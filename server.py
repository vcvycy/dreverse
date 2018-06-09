import socket                                                                   
addr=("127.0.0.1",8080)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr)
s.listen(1)
resp=b"HTTP/1.1 200 OK\r\n\
       Content-Length: 16\r\n\
       Connection: close\r\n\
       Content-Type: text/html;charset=UTF-8\r\n\r\n\
	   <h1>success</h1>"
while True:
  conn,addr=s.accept()
  print("[*]New")
  print(conn.recv(1024))
  conn.send(resp)
  """
  conn.send(b"HTTP/1.1 200 OK\r\n\
              Content-Type: text/html\r\n\
              Content-Length: 5\r\n\
	    	 \r\n\
		     hello") 
			 """
  conn.close()
