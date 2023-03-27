from django.db import models
from django.db.models import ForeignKey, DO_NOTHING, DateField
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse




# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f"{self.name}"

class Authors(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    country = ForeignKey(Countries, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.date_of_birth}, {self.date_of_death}, {self.country}"

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Books(models.Model):
    author_id = ForeignKey(Authors, on_delete=DO_NOTHING, null=True)
    category_id = ForeignKey(Categories, on_delete=DO_NOTHING)
    title = models.CharField(max_length=300)
    issue_date = models.DateField()
    date_added = models.DateField(default=date.today)
    cover = models.ImageField(upload_to='', default='default.jpg')

    def __str__(self):
        return f"{self.date_added}{self.author_id}, {self.category_id}, {self.title}, {self.issue_date}, {self.cover}, {self.date_added}"

class BooksRead(models.Model):
    user_id = ForeignKey(User, on_delete=DO_NOTHING)
    book_id = ForeignKey(Books, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.user_id}, {self.book_id}"

class BooksInterested(models.Model):
    user_id = ForeignKey(User, on_delete=DO_NOTHING)
    book_id = ForeignKey(Books, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.user_id}, {self.book_id}"
