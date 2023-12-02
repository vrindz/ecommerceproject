from django.db import models

# Create your models here.
class Product(models.Model) :

    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_list')

    def __str__(self):
        return self.name