# Generated by Django 4.1.7 on 2023-03-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webofbooks', '0006_alter_authors_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
