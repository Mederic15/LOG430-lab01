"""Product DAO (Data Access Object)
SPDX - License - Identifier: LGPL-3.0-or-later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId


class ProductDAO:
    def __init__(self):
        load_dotenv()
        mongo_uri = os.getenv("MONGO_URI")
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client["log430_lab01"]
        self.collection = self.db["products"]

    def select_all(self):
        """Select all products from MongoDB."""
        products = list(self.collection.find())
        return [
            (str(product["_id"]), product["name"], product["brand"], product["price"])
            for product in products
        ]

    def insert(self, product):
        """Insert given product into MongoDB."""
        self.collection.insert_one(
            {"name": product.name, "brand": product.brand, "price": product.price}
        )

    def update(self, product):
        """Update given product in MongoDB."""
        self.collection.update_one(
            {"_id": ObjectId(product.id)},
            {
                "$set": {
                    "name": product.name,
                    "brand": product.brand,
                    "price": product.price,
                }
            },
        )

    def delete(self, product_id):
        """Delete product from MongoDB with given product ID."""
        self.collection.delete_one({"_id": ObjectId(product_id)})

    def delete_all(self):
        """Empty products collection in MongoDB."""
        self.collection.delete_many({})

    def close(self):
        self.client.close()
