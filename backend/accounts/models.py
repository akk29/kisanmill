from django.db import models
from customercorner.models import Product

class Myproducts(models.Model):
    id = models.AutoField(primary_key=True)
    my_all_products = models.ManyToManyField(Product, related_name='Myproducts')
