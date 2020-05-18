import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codegram
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        uid = self.Users.insert({'username': data.username, 'name': data.name, 'password': hashed, 'email': data.email})
        print("userId is", uid)

    def check_username(self, username=""):
        check = self.Users.find_one({"username": username})
        if check:
            return False
        return True

