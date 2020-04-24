from database import *
from hashlib import sha256
user=Signup("sj@haam.com","Sandeep JAdam","witj",sha256(b"qwerty1234").hexdigest())

print(user.create_account())
