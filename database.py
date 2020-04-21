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


class SignUP():

    def __init__(self,Email,Fullname,Username,Password):

        self.Email = Email
        self.Fullname = Fullname
        self.Username = Username
        self.Password = Password
        
        sql_command("""
            INSERT INTO Accounts()
        """)


