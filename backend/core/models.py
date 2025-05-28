from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from customercorner.models import Product

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = (('Farmer','Farmer'),('Firm','Firm'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length = 15 , blank = False)
    Last_name = models.CharField(max_length = 15 , blank = False)
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length = 15 , choices = CATEGORY_CHOICES)


class MyProducts(models.Model):
    id = models.AutoField(primary_key=True)
    products_list = models.ManyToManyField(Product)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
