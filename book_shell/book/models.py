from django.db import models

# Create your models here. 
# DataBase is here.


class Users(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField("date published")


class Product(models.Model):
    id_product = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    description = models.CharField(default='i am here through',max_length=200)
