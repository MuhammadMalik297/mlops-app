from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client.mydb
users = db.users

def find_user_by_email(email):
    return users.find_one({'email': email})

def create_user(email, hashed_pw):
    users.insert_one({'email': email, 'password': hashed_pw})
