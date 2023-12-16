import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI") + "/?retryWrites=true&w=majority"
connection = MongoClient(MONGODB_URI)
try:
    connection.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = connection["swavalambanam"]