
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://atlas-sample-dataset-load-67f9af4b78ed99383057ded8:<db_password>@cluster0.x6zawbv.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
