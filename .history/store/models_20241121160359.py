from django.db import models
from storages.backends import s3boto3
from uuid import uuid4


# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price=models.DecimalField( max_digits=5, decimal_places=2)
    last_update=models.DateTimeField(auto_now=True,)
    
    def __str__(self) :
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    product = models.ForeignKey("product", related_name="category", on_delete=models.CASCADE)

    
    
    def __str__(self) :
        return self.title
    


class ProductMedia(models.Model):
    title = models.CharField(max_length=255)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField()
    
    def __str__(self) :
        return self.title   



