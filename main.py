from hamster_server.database import *
class Start_Hamster_Server():
    """Module use to create socket and accept connections and get request from user 
    and send response to user 
    """
    def __init__(self,host=socket.gethostname(),port=4444):
        self.host=host
        self.port=port
        
        self.create_socket()
        self.bind_socket()
        self.accept_socket()

    def create_socket(self):
        """Create socket on IP version 6 and use TCP protocol"""
        try :    
            self.soc = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        except socket.error as Err:
            print(f"Creating Socket Error {Err} ")

    def bind_socket(self):
        """Bind Host And Port"""
        try:
            self.soc.bind((self.host, self.port))
            self.soc.listen()
        except socket.error as Err:
            print(f"Binding Socket Error  {Err}")

    def accept_socket(self):
        """Accept user connection """
        while True:
            conn, addr = self.soc.accept()     # Establish connection with client.
            print ('Got connection from', addr)
            get_request(conn)
            self.soc.close()

    def get_request(self,conn):
        """Get request command from user """
        request = conn.recv(1024).decode('utf-8')
        if '@' in request:
            get_username_ip(request[1:])
        

if __name__ == "__main__":
    Start_Hamster_Server()