# Generated by Django 3.2.4 on 2021-07-07 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0011_booklinks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booklinks',
            new_name='Booklink',
        ),
    ]
