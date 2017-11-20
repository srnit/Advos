import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname();
port=12345;
s.bind((host,port));
s.listen(1);
addrclient,addr=s.accept();
while True:
	data=addrclient.recv(1024);
	if not data:
		break;
	addrclient.sendall(data);
addrclient.close();
s.close()
