from django.contrib.auth.models import User
from django.db import models
from customercorner.models import Product


class Bond(models.Model):
    created_by = models.ForeignKey(User,null=True)
    # Specific_Products = models.ManyToManyField(Product,null=True)
    name = models.CharField(max_length = 15)
    investment_amount = models.IntegerField()
    expectations = models.CharField(max_length = 500)
    facilities = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def invest(self):
        return self.investment_amount
