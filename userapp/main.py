def login():
    username = input("Username : ")
    password = input(" Password : ")

def signup():
    fullname = input("Fullname : ")
    username = input("Username : ")
    password = input(" Password : ")

while 1:
    print("|1| Log in")
    print("|2| Sign up")
    enter=input(">>>")
    if enter == '1':
        login()
    if enter == '2':
        signup()        
