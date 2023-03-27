# Generated by Django 4.1.7 on 2023-03-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0004_alter_authors_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='authors',
            name='date_of_death',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='issue_date',
            field=models.DateField(),
        ),
    ]
