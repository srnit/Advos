import socket

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while(1):
	str=raw_input();
	s.sendall(str);
	print (repr(s.recv(1024)))
s.close()
