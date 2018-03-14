#!/usr/bin/python

from socket import *

HOST = ''
PORT = 2333
BUFSIZE = 1024

ADDR = (HOST,PORT)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
	print "waiting for connection..."
	tcpClient,addr = tcpServer.accept()
	print '...connected from :'&addr
	while True:
		data = tcpClient.re
		if not data:
			break
		tcpClient.send('%s,')