# Generated by Django 4.1.7 on 2023-03-26 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0021_rename_used_id_booksread_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booksinterested',
            old_name='used_id',
            new_name='user_id',
        ),
    ]