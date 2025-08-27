from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Mongo Client cluster
mongo_client = MongoClient(os.getenv("MONGO_URI"))

# Access Database
task_manager_db = mongo_client["task_manager_db"]

# Pick a collection to operate on
tasks = task_manager_db["tasks"]