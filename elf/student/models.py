from django.db import models
import os
# Create your models here.


def lost_item_image_path(instance, filename):
    return os.path.join('lost_images', filename)

def found_item_image_path(instance, filename):
    return os.path.join('found_images', filename)

class Found_Item(models.Model):
    status = {
        'submitted': 'submitted',
        'not_submitted': 'not_submitted'
    }
    name = models.CharField(max_length=100, blank=True)
    enrollment_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, blank=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to=found_item_image_path)
    location = models.TextField(max_length=100)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=status, default='not_submitted')


class Lost_Item(models.Model):
    status = {
        'recieved': 'recieved',
        'not_recieved': 'not_recieved'
    }
    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to=lost_item_image_path)
    location = models.TextField(max_length=100)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=status, default='not_recieved')




