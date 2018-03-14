import thread
import time
from subprocess import Popen,PIPE

def ping_check(ip):
    check = Popen(['/bin/bash','-c','ping -c 2 '+ip],stdin=PIPE,stdout=PIPE)
    data = check.stdout.read()

    if 'ttl' in data:
        print '%s is up' %ip

def main():

    for i in range(1,255):
        
        ip = "61.135.169."+str(i)

        #ping_check(ip)
        thread.start_new_thread(ping_check,(ip,))
        time.sleep(0.1)
        #print ip


if __name__ == '__main__':
    main()
