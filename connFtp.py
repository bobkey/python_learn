import socket
def reBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	ip1='192.168.1.1'
	ip2='192.168.1.106'
	port = 21
	banner1 = retBanner(ip1,port)
	if banner1:
		print '[+]' + ip1 + ': ' + banner1
	
