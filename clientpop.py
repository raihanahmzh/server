import socket
import sys

host = '192.168.54.4'
port = 8995
popclient = socket.socket()

popclient.connect((host,port))
print(popclient.recv(1024).decode())

while True:
	print("Please enter a  command(USER | PASS | STAT | LIST | RETR | DELE | QUIT) : ")
	command = input('')
	popclient.send(command.encode())
	
	response = popclient.recv(1024).decode('utf-8')
	print(response)
	if command == "QUIT":
		break

popclient.close()
