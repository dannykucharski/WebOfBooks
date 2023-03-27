# Generated by Django 4.1.7 on 2023-03-14 21:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0011_booksbyauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='authors',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='books',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webofbooks.authors'),
        ),
        migrations.DeleteModel(
            name='BooksByAuthor',
        ),
    ]
