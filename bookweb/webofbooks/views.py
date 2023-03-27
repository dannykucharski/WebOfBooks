from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.models import User


from webofbooks.forms import CountryForm, AuthorForm, CategoryForm, BookForm, BooksReadForm, BooksInterestedForm
from webofbooks.models import Countries, Authors, Categories, Books, BooksRead, BooksInterested


class CountriesView(ListView):
    template_name = 'webofbooks/countries_list.html'
    model = Countries

class CountryCreateView(CreateView):
    template_name = 'webofbooks/countries_create_form.html'
    form_class = CountryForm
    success_url = reverse_lazy('webofbooks:countries_list')

class CountryUpdateView(UpdateView):
    template_name = 'webofbooks/countries_update_form.html'
    model = Countries
    success_url = reverse_lazy('webofbooks:countries_list')
    fields = ['name']

class CountryDeleteView(DeleteView):
  template_name = 'webofbooks/countries_delete_form.html'
  model = Countries
  success_url = reverse_lazy('webofbooks:countries_list')

class CountryDetailView(DetailView):
    def get(self, request, pk):
        return render(request,
                      'webofbooks/countries_detail.html',
                      context={
                          "country_authors": Authors.objects.filter(country_id=pk).all(),
                          "country": Countries.objects.filter(id=pk).all(),
                      })

class AuthorsView(ListView):
    template_name = 'webofbooks/authors_list.html'
    model = Authors

class AuthorCreateView(CreateView):
    template_name = 'webofbooks/authors_create_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('webofbooks:authors_list')

class AuthorUpdateView(UpdateView):
    template_name = 'webofbooks/authors_update_form.html'
    model = Authors
    success_url = reverse_lazy('webofbooks:authors_list')
    fields = ['name', 'surname', 'date_of_birth', 'date_of_death', 'country']

class AuthorDetailView(View):
    def get(self, request, pk):
        return render(request,
                      'webofbooks/authors_detail.html',
                      context={
                          "author_books": Books.objects.filter(author_id=pk).all(),
                          "author": Authors.objects.filter(id=pk).all(),
                      })

class AuthorDeleteView(DeleteView):
  template_name = 'webofbooks/authors_delete_form.html'
  model = Authors
  success_url = reverse_lazy('webofbooks:authors_list')

class CategoryView(ListView):
    template_name = 'webofbooks/categories_list.html'
    model = Categories

class CategoryCreateView(CreateView):
    template_name = 'webofbooks/categories_create_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('webofbooks:categories_list')

class CategoryUpdateView(UpdateView):
    template_name = 'webofbooks/categories_update_form.html'
    model = Categories
    success_url = reverse_lazy('webofbooks:categories_list')
    fields = ['name']

class CategoryDeleteView(DeleteView):
  template_name = 'webofbooks/categories_delete_form.html'
  model = Categories
  success_url = reverse_lazy('webofbooks:categories_list')

class CategoryDetailView(View):
    def get(self, request, pk):
        return render(request,
                      'webofbooks/categories_detail.html',
                      context={
                          "categories_books": Books.objects.filter(category_id=pk).all(),
                          "category": Categories.objects.filter(id=pk).all(),
                      })

class BookView(ListView):
    template_name = 'webofbooks/books_list.html'
    model = Books

class BookCreateView(CreateView):
    template_name = 'webofbooks/books_create_form.html'
    form_class = BookForm
    success_url = reverse_lazy('webofbooks:books_list')

def update_book(request, pk):
    this_book = Books.objects.get(id=pk)
    form = BookForm(request.POST or None, request.FILES or None, instance=this_book)
    if form.is_valid():
        form.save()
        return redirect('webofbooks:books_list')
    return render(request, 'webofbooks/books_update_form.html', context={
        "this_book": this_book,
        "form": form
    })

class BookDeleteView(DeleteView):
  template_name = 'webofbooks/books_delete_form.html'
  model = Books
  success_url = reverse_lazy('webofbooks:books_list')

class BookDetailView(DetailView):
    model = Books

class HomeView(View):
    def get(self, request):
        return render(request,
                      'webofbooks/webofbooks.html',
                      context={
                          "new_books": Books.objects.order_by('-date_added').all(),
                      })

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books_searched = Books.objects.filter(title__contains=searched)
        author_searched = Authors.objects.filter(Q(name__contains=searched) | Q(surname__contains=searched))

        return render(request,
                  'webofbooks/search.html',
                  context={'searched': searched,
                           'books_searched': books_searched,
                           'author_searched': author_searched})
    else:
        return render(request,
                  'webofbooks/search.html',
                  context={})

class BooksReadView(View):
    def get(self, request):
        username = request.user
        books_read = BooksRead.objects.filter(user_id=username).all()
        return render(request,
                      'webofbooks/user_booksread_list.html',
                      context={
                          "books_read": books_read,
                      })

class BooksReadDeleteView(DeleteView):
  template_name = 'webofbooks/user_booksread_delete_form.html'
  model = BooksRead
  success_url = reverse_lazy('webofbooks:booksread_list')


def booksreadadd(request, pk):
    this_book = Books.objects.get(id=pk)
    username = request.user
    data = {"user_id": username, "book_id": this_book}
    form = BooksReadForm(data)
    if form.is_valid():
        form.save()
        return redirect('webofbooks:booksread_list')
    return render(request, 'webofbooks/user_booksread_add_form.html', context={
        "book_id": this_book,
        "user_id": username,
        "form": form
    })

class BooksInterestedView(View):
    def get(self, request):
        username = request.user
        books_interested = BooksInterested.objects.filter(user_id=username).all()
        return render(request,
                      'webofbooks/user_booksinterested_list.html',
                      context={
                          "books_interested": books_interested,
                      })

class BooksInterestedDeleteView(DeleteView):
  template_name = 'webofbooks/user_booksinterested_delete_form.html'
  model = BooksInterested
  success_url = reverse_lazy('webofbooks:booksinterested_list')

def booksinterestedadd(request, pk):
    this_book = Books.objects.get(id=pk)
    username = request.user
    data = {"user_id": username, "book_id": this_book}
    form = BooksInterestedForm(data)
    if form.is_valid():
        form.save()
        return redirect('webofbooks:booksinterested_list')
    return render(request, 'webofbooks/user_interested_add_form.html', context={
        "book_id": this_book,
        "user_id": username,
        "form": form
    })