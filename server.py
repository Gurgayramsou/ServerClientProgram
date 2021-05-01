import socket
sock_=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
sock_.bind((host,9990))
sock_.listen(1)
print("\n server started...")
conn,adrs=sock_.accept()
print("connectin esteblished with_",str(adrs))
conn.sendall("Enter 'q' to quit at any time\n".encode('utf-8'))
while(1):
    msg=input("enter the messege to be sent:\n")
    conn.send(msg.encode("utf-8"))
    rcvd=conn.recv(1024).decode("utf-8")
    print(rcvd)





