from django.urls import path
from webofbooks.views import CountriesView, CountryCreateView, CountryUpdateView, CountryDeleteView, CountryDetailView, AuthorsView, AuthorCreateView, AuthorUpdateView, AuthorDetailView, AuthorDeleteView, CategoryView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryDetailView, BookView, BookCreateView, BookDeleteView, BookDetailView, HomeView, update_book, search, booksreadadd, BooksReadView, BooksReadDeleteView, BooksInterestedView, BooksInterestedDeleteView, booksinterestedadd
from django.urls import include

app_name = 'webofbooks'

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('countries/', CountriesView.as_view(), name='countries_list'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('countries/detail/<pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('authors/', AuthorsView.as_view(), name='authors_list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/detail/<pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('books/', BookView.as_view(), name='books_list'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', update_book, name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', search, name='search'),
    path('user/booksread/', BooksReadView.as_view(), name='booksread_list'),
    path('user/booksread/delete/<int:pk>/', BooksReadDeleteView.as_view(), name='booksread_delete'),
    path('user/booksread/add/<int:pk>/', booksreadadd, name='booksread_add'),
    path('user/booksinterested/', BooksInterestedView.as_view(), name='booksinterested_list'),
    path('user/booksinterested/delete/<int:pk>/', BooksInterestedDeleteView.as_view(), name='booksinterested_delete'),
    path('user/booksinterested/add/<int:pk>/', booksinterestedadd, name='booksinterested_add'),

]

