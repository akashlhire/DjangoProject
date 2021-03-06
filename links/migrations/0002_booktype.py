# Generated by Django 3.2.4 on 2021-07-07 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_type', models.CharField(max_length=50)),
                ('book_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.booklink')),
            ],
        ),
    ]
