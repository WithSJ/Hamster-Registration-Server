"""Global imports and variables"""
import sqlite3,os,socket
from hashlib import sha256

EMAIL_LEN = 120
FULLNAME_LEN = 25
USERNAME_LEN = 25
PASSWORD_LEN = 64
LOGIN_KEY_LEN = 256
IP_ADDRESS_LEN = 40