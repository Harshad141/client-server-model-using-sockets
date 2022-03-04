from multiprocessing import connection
import socket
from sqlite3 import connect
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= '127.0.0.1'
port= 1255
s.bind((host,port))
s.listen()
socketclient, address=s.accept()
print("got connection",address)
connection = True
while connection:
 sent_data=input('Server:')
 socketclient.send(bytes(sent_data,'utf-8'))
 msgg=socketclient.recv(1024)
 msgg=msgg.decode("utf-8")
 print("Client:",msgg)
 if(msgg=="quit"):
     s.close()
