import sqlite3

def sql_command(command):
    """connect to database """
    try:
        conn = sqlite3.connect("Database//database.db")
        cur = conn.cursor()
        cur.execute(command)
        conn.close()
    except sqlite3.Error as err:
        print(f"SQL Command Error {err}")

def insert_command(command,values):
    """Insert command , values should be iterable """
    try:
        conn = sqlite3.connect("Database//database.db")
        cur = conn.cursor()
        cur.execute(command,values)
        conn.commit()
        conn.close()
    except sqlite3.Error as err:
        print(f"SQL Insert Command Error {err}")



class SignUP():

    def __init__(self,Email,Fullname,Username,Password):

        self.Email = Email
        self.Fullname = Fullname
        self.Username = Username
        self.Password = Password
        
        insert_command("""
            INSERT INTO Accounts (Email,Fullname,Username,Password)
            VALUES (?,?,?,?)
        """,(self.Email,self.Fullname,self.Username,self.Password))

