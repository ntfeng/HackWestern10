from pymongo import MongoClient
from bson import ObjectId
from typing import Dict

class Database:
    def __init__(self):
        self.db = self.connect_db()

    @staticmethod
    def connect_db():
        client = MongoClient('mongodb://appuser:appuserpassword@localhost:27017/userDB')
        db = client.userDB
        return db

    def get_user(self, user_id):
        users = self.db.users
        return users.find_one({"_id": ObjectId(user_id)})

    def create_user(self, user_data: Dict):
        users = self.db.users
        return users.insert_one(user_data).inserted_id

    def delete_user(self, user_id):
        users = self.db.users
        result = users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count

    #takes the user and application id access_level is R or W or admin (A)
    def add_user_app(self, user_id, app_id, access_level):
        user = self.get_user(user_id)
        user["app_access_list"].append({"app_id": app_id, "access_level": access_level})

    def create_application(self, app_data: Dict):
        applications = self.db.applications
        return applications.insert_one(app_data).inserted_id

    def delete_application(self, app_id):
        applications = self.db.applications
        result = applications.delete_one({"app_id": app_id})
        return result.deleted_count