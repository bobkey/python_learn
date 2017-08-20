#!/usr/bin/python
import socket
def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return



def checkVulns(banner):
	if 'SSH-2.0-OpenSSH_7.3p1 Debian-1' in banner:
		print '[+] SSH-2.0-OpenSSH_7.3p1 Debian-1 is vulnerable.'

	elif 'bbbbbbb' in banner:
		print 'find a vulnerable'

	else:
		print '[-] not found vulnerable.'

	return		

def main():
	portList = [21,22,25,80,110,443]
#	for x in range(1, 255):	
	ip ='192.168.128.135'
	for port in portList:
		banner = retBanner(ip,port)
		if banner:
			print '[+]' + ip + ': ' + banner
			checkVulns(banner)

if __name__ == '__main__':
	main()

