import os

from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")
connection = MongoClient(MONGODB_URI)