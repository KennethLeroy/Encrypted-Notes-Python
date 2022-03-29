import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def getEncryptedContents():
    return "test"


def generateKey(password):
    password = bytes(password, "utf-8")
    # salt = os.urandom(16)
    salt = b'9\xc7\xee\x7fPU\xc6\xb1Y\xfa\x82\x0c\x87dc\xaf'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f


class Note:

    def __init__(self, title, content, password) -> None:
        self.title = title
        key = generateKey(password)
        print(type(content))
        if type(content) == bytes:
            self.content = content
        else:
            self.content = key.encrypt(bytes(content, "utf-8"))

    # def pushToDb(self):
    #     # push the contents of the note to row corresponding to title name
    #     pass

    # def fetchNote(self):
    #     # find the note from the title in the db
    #     # decode the note and get password
    #     pass

    def decode(self, password):
        salt = b'9\xc7\xee\x7fPU\xc6\xb1Y\xfa\x82\x0c\x87dc\xaf'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password, "utf-8")))
        f = Fernet(key)
        try:
            return f.decrypt(self.content)
        except:
            return None

    # def getClearText(self, password):
    #     # returns the cleartext if password is right, else returns null
    #     cleartext = None
    #     # decode(password)
    #     return cleartext
