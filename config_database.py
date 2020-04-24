from hamster_server import *
 
class Config_Hamster_Database():
   
    def __init__(self):
        self.connect_database()

    def connect_database(self):
        """ Connect to Database.
            Create database folder and file if file not exist
        """
        try:
            conn = sqlite3.connect("Database//database.db")
            self.config_database(conn)

        except sqlite3.OperationalError :
            os.system("mkdir Database")
            self.connect_database()
            print("Database successfully created")

    def config_database(self,conn):
        """ Create Tables and data fields that required
            Accounts Table - Email, Fullname, Username, Password_Hash
            Logins Table - Username, Login_key, IP_Address
        """
        try:   
            cur = conn.cursor()
            cur.execute(f"""
                CREATE TABLE Accounts(
                Email VARCHAR({EMAIL_LEN}) NOT NULL UNIQUE ,
                Fullname VARCHAR({FULLNAME_LEN}) NOT NULL ,
                Username VARCHAR({USERNAME_LEN}) PRIMARY KEY UNIQUE,
                Password VARCHAR({PASSWORD_LEN}) NOT NULL
                )""")
            
            cur.execute(f"""
                CREATE TABLE Logins(
                Username VARCHAR({USERNAME_LEN}) PRIMARY KEY UNIQUE,
                Login_Key VARCHAR({LOGIN_KEY_LEN}) NOT NULL UNIQUE,
                IP_Address VARCHAR({IP_ADDRESS_LEN}) NOT NULL UNIQUE
                )""")
            
            conn.close()

        except  sqlite3.OperationalError :
            print("Database already exits")

if __name__ == "__main__":
    Config_Hamster_Database()