from django.db import models
from django.contrib.auth.models import User
from customercorner.models import Product

class ExpertCorner(models.Model):
    posted_by = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    Product = models.ForeignKey(Product)
    Description = models.CharField(max_length = 1500)
    Technique_name = models.CharField(max_length = 150)

    def __str__(self):
        self.Technique_name
