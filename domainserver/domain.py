import socket


def Signup(fullname,username,password):
   """
      save sign up details in domain.db 
      fullname , username, password, login_key,IP address
      login_key and IP address are save in run time
   """
   with open("domain.db","a+") as database:
      database.write(f"{fullname}${username}${password}$None$None")
      database.close()
      

def Login():
   pass




def Create_Socket():
    # Set Host IP address and Port number and use IPV6 and TCP protocol
    try :
         
      global soc
      global host 
      global port 

      host = socket.gethostname() 
      port = 12345                
      soc = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)        
      print(host)
    except socket.error as Err:
        print(f"Creating Socket  {Err} ")

def Bind_Socket():
#    Bind IP address and Port in sockect 
   try:
      global soc
      global host
      global port

      soc.bind((host, port))        # Bind to the port
      soc.listen(5)                 # Now wait for client connection.
   except socket.error as Err:
      print(f"Binding Socket Error  {Err}")

# def Accept_Socket():
# #    when client send request taht accept here and that connection in conn and IPaddress and port in addr
#    conn, addr = soc.accept()     # Establish connection with client.
#    print ('Got connection from', addr)
#    Response(conn)
#    soc.close() 

# def Response(conn):
#    while True:
#       msg=input("Enter :")
#       if msg=="quit()":
#          conn.send(msg.encode('utf-8'))
#          conn.close()
#          break
#       else:
#          conn.send(msg.encode('utf-8'))
def Post_IP():
   conn, addr = soc.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   username=conn.recv(1024).decode('utf-8')
   if username == "@withsj":
      conn.send("192.11.11.11".encode('utf-8'))
   else:
      conn.send("sorry".encode('utf-8'))
   soc.close() 

if __name__ == "__main__":
   # Create_Socket()
   # Bind_Socket()
   # Post_IP()
   Signup("sandeep jadam","@withsj","qwerty")