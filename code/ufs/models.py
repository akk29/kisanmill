from django.db import models
from django.contrib.auth.models import User
from kisanmill.settings import MEDIA_ROOT

from customercorner.models import Product


class Message(models.Model):
    title = models.CharField(max_length = 15)
    # created_by = models.ForeignKey(User)
    effected_crop = models.ForeignKey(Product)
    Description = models.CharField(max_length = 1500 , null = False , blank = False)
    Images = models.CharField(max_length = 300 , default = '')
    # First_seen = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.effected_crop) + " " + str(self.title)

    class Meta:
        ordering = ['-timestamp']
