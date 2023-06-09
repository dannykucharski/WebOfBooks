# Generated by Django 4.1.7 on 2023-03-11 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0010_books_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksByAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webofbooks.authors')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webofbooks.books')),
            ],
        ),
    ]
