from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.


def lost_item_image_path(instance, filename):
    return os.path.join('lost_images', filename)

def found_item_image_path(instance, filename):
    return os.path.join('found_images', filename)

class Found_Item(models.Model):
    status = (
        ('not_received', 'Not Received'),
        ('received', 'Received'),
    )
    name = models.CharField(max_length=100, blank=True)
    enrollment_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, blank=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to=found_item_image_path)
    location = models.TextField(max_length=100)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=status, default='not_submitted')
    completed = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Lost_Item(models.Model):
    status = (
        ('not_received', 'Not Received'),
        ('received', 'Received'),
    )
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to=lost_item_image_path)
    location = models.TextField(max_length=100)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=status, default='not_recieved')
    completed = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




