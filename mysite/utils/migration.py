import os
import sys

import django
from pymongo import MongoClient

print(sys.path)
directory = os.path.dirname(os.path.realpath(__file__) + "/../../")
sys.path.append(directory)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from quotes.models import Quote, Tag, Author


client = MongoClient("mongodb://localhost")

db = client.web10

authors = db.authors.find()

for a in authors:
    Author.objects.get_or_create(
        fullname=a["fullname"],
        born_date=a["born_date"],
        born_location=a["born_location"],
        description=a["description"]
    )

quotes = db.quote.find()

for q in quotes:
    tags = []
    for tag in q["tags"]:
        t, *_ = Tag.objects.get_or_create(tag=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=q["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": q["author"]})
        a = Author.objects.get(
            fullname=author["fullname"]
        )
        quo = Quote.objects.create(
            quote=q["quote"],
            author=a
        )

        for tag in tags:
            quo.tags.add(tag)

