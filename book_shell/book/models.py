from django.db import models

# Create your models here. 
# DataBase is here.


class Users(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField("date published")


class Product(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
