#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#include <unistd.h>

void func(int socket_desc) 
{ 
	char buff[80]; 
	int n; 
	for (;;)
        { 
		bzero(buff, 80); 

		read(socket_desc, buff, sizeof(buff)); 
		printf("Message from client: %s\t Message to client : ", buff); 
		bzero(buff, 80); 
		n = 0; 
		while ((buff[n++] = getchar()) != '\n') 
			; 

		write(socket_desc, buff, sizeof(buff)); 

		if (strncmp("exit", buff, 4) == 0) { 
			printf("Server Exit...\n"); 
			break; 
		} 
	} 
} 

int main(int argc , char *argv[]) 
{ 
	int socket_desc, connfd, len; 
	struct sockaddr_in server, client; 

	socket_desc = socket(AF_INET, SOCK_STREAM, 0); 
	if (socket_desc == -1) { 
		printf("socket creation failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully created..\n"); 
	bzero(&server, sizeof(server)); 

	server.sin_family = AF_INET; 
	server.sin_addr.s_addr = htonl(INADDR_ANY); 
	server.sin_port = htons(8888); 

	if ((bind(socket_desc, (struct sockaddr *)&server , sizeof(server))) != 0) { 
		printf("socket bind failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully binded..\n"); 

	if ((listen(socket_desc, 5)) != 0) { 
		printf("Listen failed...\n"); 
		exit(0); 
	} 
	else
		printf("Server listening..\n"); 
	len = sizeof(client); 

	connfd = accept(socket_desc, (struct sockaddr *)&client, &len); 
	if (connfd < 0) { 
		printf("server acccept failed...\n"); 
		exit(0); 
	} 
	else
		printf("server acccept the client...\n"); 

	func(connfd); 

	close(socket_desc); 
} 

