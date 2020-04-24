from hamster_server import *

class Hamster_Database:

    @classmethod
    def sql_connect(cls):
        """connect to database """
        try:
            conn = sqlite3.connect("Database//database.db")
            return conn
        except sqlite3.Error as err:
            Passwordprint(f"SQL Connecting Error {err}")
    
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
        if dPasswordata:
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

        self.Email = str(EmailPassword)
        self.Fullname = str(Fullname)
        self.Username = str(Username)
        self.Password = sha256(str(Password).encode('utf-8')).hexdigest()
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

class Login():
    def __init__(self,Username,Password,IP_Addreess):
        self.Username = str(Username)
        self.Password = sha256(str(Password).encode('utf-8')).hexdigest()
        self.IP_Addreess = str(IP_Addreess)
    
    def create_account(self):
        if self.validate():
            return self.validate()

        Data=Hamster_Database.sql_command(
        """ SELECT Email, Fullname 
            FROM Accounts 
            WHERE Username = :Username AND Password = :Password
        """,{"Username":self.Username,"Password":self.Password})
        if len(Data) == 0:
            return "Worng password"
        return f"{Data}"

    def validate(self):
        if len(self.Username) > USERNAME_LEN:
            return f"Username should be in {USERNAME_LEN} charecters"
        elif not Hamster_Database.is_username_exist(self.Username):
            return "Username not exist"
