from django.contrib import admin
from django.urls import path
from webofbooks.models import Authors, Categories, Countries, Books, BooksRead, BooksInterested


# Register your models here.
#admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(Countries)
#admin.site.register(Books)
admin.site.register(BooksRead)
admin.site.register(BooksInterested)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_id', 'category_id')
    ordering = ('title',)
    search_fields = ('title',)

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    fields = (('name', 'surname'), 'date_of_birth', 'date_of_death', 'country')
    list_display = ('surname', 'name')
    ordering = ('surname',)
    search_fields = ('name', 'surname')
    list_filter = ('country',)