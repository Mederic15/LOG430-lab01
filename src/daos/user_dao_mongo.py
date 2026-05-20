import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
        load_dotenv()
        mongo_uri = os.getenv('MONGO_URI')
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client['log430_lab01']
        self.collection = self.db['users']

    def select_all(self):
        users = []
        for doc in self.collection.find():
            user = User(str(doc['_id']), doc['name'], doc['email'])
            users.append(user)
        return users

    def insert(self, user):
        result = self.collection.insert_one({'name': user.name, 'email': user.email})
        return str(result.inserted_id)

    def update(self, user):
        self.collection.update_one({'_id': ObjectId(user.id)}, {'$set': {'name': user.name, 'email': user.email}})

    def delete(self, user_id):
        self.collection.delete_one({'_id': ObjectId(user_id)})