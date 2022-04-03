from django.contrib import admin
from links.models import Booklink, Booktype

# Register your models here
admin.site.register(Booklink)
admin.site.register(Booktype)