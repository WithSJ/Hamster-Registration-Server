from database import *
from hashlib import sha256
# user=Signup("sj@haam.com","Sandeep JAdam","withsj",sha256(b"qwerty1234").hexdigest())
# print(user.create_account())
user=Login("withsj","qwerty1234","")
print(user.create_account())