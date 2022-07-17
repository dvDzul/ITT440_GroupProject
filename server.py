# import socket programming library
import socket
 
# import thread module
from _thread import *
import threading
 
print_lock = threading.Lock()
 
# thread function
def threaded(c):
	while True:

		# receiving highscore info from client and store in file
		dataFromClient = c.recv(1024)
		hisc=open("highscore.txt","w+")
		highscore=hisc.read()
		highscore_in_no=int(highscore)
		if (dataFromClient == clientConnected.recv(1024)) > highscore_in_no:
			hisc.write(str(dataFromClient = clientConnected.recv(1024)))
			highscore_in_no = dataFromClient = clientConnected.recv(1024)
		hisc.close()

 
		# connection closed
		c.close()
 
 
def Main():
    host = ""
 
    # reserve a port
    port = 8880
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        # establish connection with client
        c, addr = s.accept()
 
        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()
