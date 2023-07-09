from django.db import models

# Create your models here. 
# DataBase is here.

class Users(models.Model):
    # user_id = models.BigAutoField()
    name = models.CharField(max_length=25)
    email = models.EmailField()
    # Cart = models.TextField()
    # password = models.IntegerField()
    # confPassword = models.IntegerField()
    # usr_image = models.FileField()

class Product(models.Model):
    product_id = models.IntegerField(models.ForeignKey(Users, on_delete=models.CASCADE))
    Product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_image = models.ImageField()

