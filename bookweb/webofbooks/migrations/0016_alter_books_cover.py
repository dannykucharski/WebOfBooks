# Generated by Django 4.1.7 on 2023-03-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0015_alter_books_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='static/'),
        ),
    ]
