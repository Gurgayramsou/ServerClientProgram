import socket
sock_=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9990
sock_.connect((host,port))
print('-'*20)
rcv=sock_.recv(1024).decode("utf-8")
print(rcv,"\n")
while(1):
    rcv=sock_.recv(1024).decode("utf-8")
    print(rcv)
    msg=input("enter the messege to be sent:\n")
    sock_.sendall(msg.encode("utf-8"))


