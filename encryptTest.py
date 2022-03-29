import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = bytes(input("Enter password "), "utf-8")
# salt = os.urandom(16)
salt = b'9\xc7\xee\x7fPU\xc6\xb1Y\xfa\x82\x0c\x87dc\xaf'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
kdf1 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
# key = Fernet.generate_key()
# key = password
print("this is the key")
print(key)
f = Fernet(key)
# f = Fernet(key)

token = f.encrypt(b"Secret message!")
print(token)
# b'...'
key1 = base64.urlsafe_b64encode(kdf1.derive(b"password"))

f1 = Fernet(key1)
a = str(f1.decrypt(token))
print(a)
