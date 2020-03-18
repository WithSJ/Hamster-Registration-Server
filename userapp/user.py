import socket   

def Create_Socket():
    try :
         
      global soc
      global host 
      global port 

      host = socket.gethostname() 
      port = 12345                
      soc = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)        
    except socket.error as Err:
        print(f"Create Socket  {Err} ")

# def Connect_Socket():
#     try:
#         soc.connect((host, port))
#         Rec_MSG()
#     except socket.error as Err:
#         print(f"Connecting Problem  {Err}")

# def Rec_MSG():
#     while True:
#         msg=soc.recv(1024).decode('utf-8')
#         if msg == "quit()":
#             soc.close()
#             break
#         else:
#             print(msg)    

def Get_IP(username):
    Create_Socket()
    try:
        soc.connect((host, port))
        soc.send(str(username).encode('utf-8'))
        ipaddress=soc.recv(1024).decode('utf-8')
        return ipaddress
    except socket.error as Err:
        print(f"Connecting Problem  {Err}")
    
    


if __name__ == "__main__":
    Create_Socket()
    print(Get_IP('@withsj'))