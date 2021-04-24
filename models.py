from django.db import models

class productModel(models.Model):
    no=models.AutoField(primary_key=True)
    name=models.CharField(unique=True,max_length=30)
    price=models.FloatField()
    quantity=models.IntegerField()
    photo=models.ImageField(upload_to="product_images/")
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)

