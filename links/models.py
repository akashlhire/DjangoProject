from django.db import models
from django.core import validators
# Create your models here.


class Booktype(models.Model):
    # book_title = models.CharField(max_length=50, null = True)
    book_type = models.CharField(max_length=50)
    # book_link = models.ForeignKey(Booklink,on_delete=models.CASCADE,related_name="links")

    def link_name(self):
        return f" {self.book_type} " 


    def __str__(self):
        return self.link_name()


class Booklink(models.Model):
    book_title = models.CharField(max_length=50)
    book_link = models.CharField(max_length=200)
    book_type = models.ForeignKey(Booktype,on_delete=models.CASCADE,default=None,related_name="links")
    date = models.DateField()
 

    def __str__(self):
        return f"({self.date})------------{self.book_type } -----------{self.book_title}----------{self.book_link} "