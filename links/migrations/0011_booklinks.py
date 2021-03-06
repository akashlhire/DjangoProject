# Generated by Django 3.2.4 on 2021-07-07 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0010_delete_booklink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booklinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_link', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('book_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='links.booktype')),
            ],
        ),
    ]
