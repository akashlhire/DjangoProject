# Generated by Django 3.2.4 on 2021-07-07 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0009_remove_booklink_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booklink',
        ),
    ]
