from django.db import models

# Create your models here.
class Book(models.Model):

    #isbn
    isbn = models.CharField(max_length=128,primary_key=True)

    #タイトル
    title = models.CharField(max_length=128)

    #価格
    price = models.IntegerField()