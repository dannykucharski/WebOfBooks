# Generated by Django 4.1.7 on 2023-03-09 18:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webofbooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 19, 19, 7, 996107)),
        ),
        migrations.AddField(
            model_name='authors',
            name='date_of_death',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 19, 19, 7, 996107)),
        ),
        migrations.AddField(
            model_name='books',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 9, 19, 19, 7, 997134)),
        ),
        migrations.AlterField(
            model_name='booksinterested',
            name='used_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booksread',
            name='used_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]