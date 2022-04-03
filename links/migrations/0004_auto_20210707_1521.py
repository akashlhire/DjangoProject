# Generated by Django 3.2.4 on 2021-07-07 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_alter_booktype_book_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktype',
            name='book_link',
        ),
        migrations.AddField(
            model_name='booklink',
            name='book_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='links.booktype'),
        ),
    ]