import json

from bson import ObjectId
from pymongo import MongoClient


client = MongoClient("mongodb://localhost")

db = client.web10

with open('quotes.json', 'r', encoding='utf8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quote.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })

