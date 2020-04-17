import sqlite3,os

def connect_database():
    """connect to database """
    try:
        conn = sqlite3.connect("Database//database.db")
        config_database(conn)

    except sqlite3.OperationalError :
        os.system("mkdir Database")
        connect_database()
        print("Database successfully created")

def config_database(conn):
    try:   
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE Accounts(
            Username VARCHAR(25) PRIMARY KEY,
            Email VARCHAR(120) NOT NULL ,
            Fullname VARCHAR(25) NOT NULL ,
            Password VARCHAR(256) NOT NULL
            )""")
        
        cur.execute("""
            CREATE TABLE Logins(
            Username VARCHAR(25) PRIMARY KEY,
            Login_Key VARCHAR(256) NOT NULL,
            IP_Address VARCHAR(256) NOT NULL
            )""")
        
        conn.close()

    except  sqlite3.OperationalError :
        print("Database already exits")

if __name__ == "__main__":
    connect_database()