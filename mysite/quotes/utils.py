from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb://localhost')
    db = client.web10
    return db

