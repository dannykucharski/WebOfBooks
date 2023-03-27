from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ImageField, URLField, FileField, TextInput, DateInput, FileInput
)
from django.forms import ModelForm
from webofbooks.models import Countries, Authors, Categories, Books, BooksRead, BooksInterested
from datetime import date
from django.contrib.auth.models import User


class CountryForm(ModelForm):

  class Meta:
    model = Countries
    fields = '__all__'

    name = CharField(label="Nazwa", max_length=300)
    widgets = {
    'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Podaj nazwę kraju'}),
    }

class AuthorForm(ModelForm):
  class Meta:
    model = Authors
    fields = '__all__'

    name = CharField(max_length=100)
    surname = CharField(max_length=100)
    date_of_birth = DateField(label="Data urodzenia:")
    date_of_death = DateField(label="Data śmierci:", required=False)
    labels = {
    'name': 'Imię:',
    'surname': 'Nazwisko:',
    'date_of_birth': 'Data urodzenia:',
    'date_of_death': 'Data śmierci:'
    }
    widgets = {
    'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię autora'}),
    'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko autora'}),
    'date_of_birth': DateInput(attrs={'class': 'form-control', 'placeholder': '(rrrr-mm-dd)'}),
    'date_of_death': DateInput(attrs={'class': 'form-control', 'placeholder': '(rrrr-mm-dd)'}),
    }

class CategoryForm(ModelForm):

  class Meta:
    model = Categories
    fields = '__all__'
    name = CharField(label="Nazwa kategorii", max_length=100)
    labels = {
    'name': 'Kategoria:',
    }
    widgets = {
    'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa kategorii'}),
    }


class BookForm(ModelForm):
  class Meta:
    model = Books
    fields = '__all__'

    title = CharField(max_length=300)
    issue_date = DateField()
    cover = ImageField(required=False)
    labels = {
    'title': 'Tytuł:',
    'issue_date': 'Data wydania:',
    'cover': 'Okładka:',
    }
    widgets = {
    'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Podaj tytuł książki'}),
    'issue_date': DateInput(attrs={'class': 'form-control', 'placeholder': '(rrrr-mm-dd)'}),
    'cover': FileInput(attrs={'class': 'form-control'}),
    }

class BooksReadForm(ModelForm):
  class Meta:
    model = BooksRead
    fields = '__all__'

    user_id = CharField(disabled=True)
    book_id = CharField(disabled=True)

class BooksInterestedForm(ModelForm):
  class Meta:
    model = BooksInterested
    fields = '__all__'

    user_id = CharField(disabled=True)
    book_id = CharField(disabled=True)

