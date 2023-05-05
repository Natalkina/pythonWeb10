from django.db import models


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}'

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tag}'


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote}'

