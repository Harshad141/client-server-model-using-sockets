from multiprocessing import connection
import socket
from sqlite3 import connect
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= '127.0.0.1'
port= 1255
s.bind((host,port))
s.listen(5)
socketclient, address=s.accept()
print("got connection",address)
connection = True
while connection:
 msgg=socketclient.recv(1024)
 msgg=msgg.decode("utf-8")
 print(msgg)
 if(msgg=="quit"):
     s.close()
