import poplib
import string
import sys
import os
import time

def server():

 port = 8888
 host =''
 server=socket.socket()
 server.bind((host,port))
 server.listen(5)



if len(sys.argv)==3:
 maxTime = int (sys.argv[2])*60
else:
 maxTime=20*60


print('Connecting with port number {}: {}'.format(host,port))


user='raihanaummu@gmail.com'
password='abc123'
email= ['Paypal: You have received 10$ from Emma']
msglength=0
delmsg=[]

for message in email:
	msglength +=len(message)
while TRUE:

 client, adrress = server.accept()
 print ('Receiving a connection from client {}:{}'.format(address[0], address[1]))
 client.send ('Hi! Welcome to POP')

while TRUE:

	try:
		client.settimeout(maxTime)
		cmdclient=client.recv(1024).decode('utf-8')

	if cmdclient == 'USER':
		if cmdclient==user:

		client.send('Authorised user{}'.format(user).encode())
	else: 
		client.send(' Unauthorised user, please try again'.encode())
	
	else if cmdclient[0:4]=='PASS':
		if cmdclient[5:]== password:
		client.send('{} successfully logged in'.format(user).encode())
	else:
		client.send('wrong password'.encode())
	
	else if cmdclient =='STAT':
		client.send('{} {}'.format(len(email), msglength).encode())
	
	else if =='LIST':
		list (client, cmdclient, email)
	
	else if cmdclient == 'RETR'and len(cmdclient)>5:
		retrieve (client,cmdclient,email)
	
	else if cmdclient == "RSET":
		for message in delmsg:
	
		email.append(message)
		msglength += len(message)
		delmsg=[]
		client.send("You have {} messages ({} octets)'.format(len(email), msglength). encode())
	else if cmdclient =='QUIT':
		if msglength==0:
		client.send('{}Exiting pop server(no messages)'.format(user).encode())
	else 
		client.send(' {} Exiting pop server ({} messages)'.format(user,len(email)).encode())
	break

else
	client.send( Wrong command entered'.encode())
except socket.timeout:
print ('Inactive user')
client.send('Timeout')
break

client.close()

