from encodings import utf_8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port= 1255
s.connect((host,port))
connection=True
while connection:
  msg=input("enter msg:")
  s.send(msg.encode("utf-8"))
  
  if msg=="quit":
      s.close()
