from django.db import models
from customercorner.models import Product
from django.contrib.auth.models import User


class Auction(models.Model):
    created_by = models.ForeignKey(User)
    Product = models.ForeignKey(Product)
    Price = models.IntegerField()
    Quality = models.CharField(max_length = 150)
    image = models.CharField(max_length = 500)
    Description = models.CharField(max_length = 150)
    Min_order = models.PositiveIntegerField()
    Address = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.Product) + str(self.Price)

    def all_bidding(self):
        return self.bidding_set.all()

class Bidding(models.Model):
    Auction = models.ForeignKey(Auction,on_delete=models.CASCADE)
    bid_by = models.ForeignKey(User)
    Bidding_Price = models.IntegerField()
    sample = models.BooleanField()
    Query = models.CharField(max_length = 150)

    def __str__(self):
        return str(self.Auction)

    def userwithprice(self):
        return str(self.bid_by) + ' bid ' + str(self.Bidding_Price) + 'Rs/- on your product'


class Services(models.Model):
    Company_Name = models.CharField(max_length = 150)
    Service_name = models.CharField(max_length = 200)
    Price = models.IntegerField()
    Product = models.ManyToManyField(Product)
    Description = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(auto_now_add=True)
    images = models.CharField(max_length = 500)

    def __str__(self):
        return self.Company_Name
