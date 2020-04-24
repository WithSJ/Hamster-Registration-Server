import sqlite3,os

global EMAIL_LEN
global FULLNAME_LEN
global USERNAME_LEN
global PASSWORD_LEN
global LOGIN_KEY_LEN
global IP_ADDRESS_LEN

EMAIL_LEN = 120
FULLNAME_LEN = 25
USERNAME_LEN = 25
PASSWORD_LEN = 64
LOGIN_KEY_LEN = 256
IP_ADDRESS_LEN = 40


class Config_Hamster_Database():
    def __init__(self):
        self.connect_database()

    def connect_database(self):
        """connect to database """
        try:
            conn = sqlite3.connect("Database//database.db")
            self.config_database(conn)

        except sqlite3.OperationalError :
            os.system("mkdir Database")
            self.connect_database()
            print("Database successfully created")

    def config_database(self,conn):
        try:   
            cur = conn.cursor()
            cur.execute(f"""
                CREATE TABLE Accounts(
                Email VARCHAR({EMAIL_LEN}) NOT NULL ,
                Fullname VARCHAR({FULLNAME_LEN}) NOT NULL ,
                Username VARCHAR({USERNAME_LEN}) PRIMARY KEY,
                Password VARCHAR({PASSWORD_LEN}) NOT NULL
                )""")
            
            cur.execute(f"""
                CREATE TABLE Logins(
                Username VARCHAR({USERNAME_LEN}) PRIMARY KEY,
                Login_Key VARCHAR({LOGIN_KEY_LEN}) NOT NULL,
                IP_Address VARCHAR({IP_ADDRESS_LEN}) NOT NULL
                )""")
            
            conn.close()

        except  sqlite3.OperationalError :
            print("Database already exits")

if __name__ == "__main__":
    Config_Hamster_Database()