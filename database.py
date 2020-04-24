import sqlite3
from config_database import *

class Hamster_Database:

    @classmethod
    def sql_connect(cls):
        """connect to database """
        try:
            conn = sqlite3.connect("Database//database.db")
            return conn
        except sqlite3.Error as err:
            print(f"SQL Connecting Error {err}")
    
    @classmethod
    def sql_command(cls,command,values):
        """SQL command , values should be iterable """
        try:
            conn = cls.sql_connect()
            cur = conn.cursor()
            cur.execute(command,values)
            conn.commit()
            data = cur.fetchall()
            conn.close()
            if "SELECT" or "select" in command:
                return data

        except sqlite3.Error as err:
            print(f"SQL Insert Command Error {err}")
    
    @classmethod
    def is_email_exist(cls,Email):
        data=cls.sql_command("SELECT Email FROM Accounts WHERE Email = :Email",{"Email":Email})
        if data:
            return True
        else:
            return False

    @classmethod
    def is_username_exist(cls,Username):
        data=cls.sql_command("SELECT Username FROM Accounts WHERE Username = :Username",{"Username":Username})
        if data:
            return True
        else:
            return False
    

class Signup():

    def __init__(self,Email,Fullname,Username,Password):

        self.Email = Email
        self.Fullname = Fullname
        self.Username = Username
        self.Password = Password
        # self.create_account()

        
    def create_account(self):
            if self.validate():
                return self.validate()

            Hamster_Database.sql_command(
            """INSERT INTO Accounts VALUES(:Email,:Fullname,:Username,:Password)""",
            {"Email":self.Email,"Fullname":self.Fullname,"Username":self.Username,"Password":self.Password})
           
            return f"{self.Username} is Created"

    def validate(self):
        if len(self.Email) > EMAIL_LEN:
            return f"Email should be in {EMAIL_LEN} charecters"
        elif Hamster_Database.is_email_exist(self.Email):
            return "Email is alredy exist"
        elif len(self.Fullname) > FULLNAME_LEN:
            return f"Fullname should be in {FULLNAME_LEN} charecters"
        elif len(self.Username) > USERNAME_LEN:
            return f"Username should be in {USERNAME_LEN} charecters"
        elif Hamster_Database.is_username_exist(self.Username):
            return "Username is alredy exist"
        elif len(self.Password) != PASSWORD_LEN:
            return f"Password should be in sha{PASSWORD_LEN} hex"


# class Login():
#     def __init__(self,Username,Password):