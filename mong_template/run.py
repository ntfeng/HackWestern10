from pymongo import MongoClient
from datetime import datetime

def connect_db():
    client = MongoClient('mongodb://appuser:appuserpassword@localhost:27017/userDB')
    db = client.userDB
    return db

def create_user(db, user_data):
    users = db.users
    return users.insert_one(user_data).inserted_id

def main():
    db = connect_db()
    new_user = {
        "userid": 12345,
        "app_access_list": [
            {"app_id": 1, "access_level": "R"},
            {"app_id": 2, "access_level": "W"}
        ],
        "password": "securepassword123",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "creation_date": datetime.now()
    }
    user_id = create_user(db, new_user)
    print(f"User created with ID: {user_id}")

if __name__ == "__main__":
    main()
