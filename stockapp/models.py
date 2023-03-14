from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_cust = models.BooleanField(default=False)

class Customer_Registration(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='customer',null=True)
    name=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    phone=models.IntegerField()
    age= models.IntegerField()

    def __str__(self):
        return self.name


class Stock(models.Model):

    stock_name = models.CharField(max_length=200)
    stock_id= models.CharField(max_length=25)
    quantity=models.IntegerField()
    price=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
