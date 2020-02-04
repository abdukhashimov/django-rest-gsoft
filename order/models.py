from django.db import models
from rest_framework.test import APIClient
from django.db.models.signals import post_save
import requests


class BaseContact(models.Model):
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.phone_number

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        URL = 'https://api.telegram.org/bot856336707:AAFRfR3dP7XZLZL5MDuR2D2HitAvfUeYt94/sendMessage'
        payload = {
            "chat_id": "694902869",
            "text": 'Contact Us: ' + self.phone_number + '\n'
        }
        requests.post(URL, payload)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class Order(models.Model):
    phone_number = models.CharField(max_length=13)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.phone_number

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


def make_str(obj):
    text = 'FROM WEB SITE: \n'
    text += 'Phone Number: ' + obj.phone_number + '\n'
    text += 'First Name: ' + obj.first_name + '\n'
    text += 'Last Name: ' + obj.last_name + '\n'
    text += 'Comp Name: ' + obj.company_name + '\n'
    text += 'Comment: ' + obj.comment + '\n'
    return text


def send_orders(sender, created, **kwargs):
    if created:
        obj = kwargs['instance']
        payload = {
            "chat_id": "694902869",
            "parse_mode": "markdown",
            "text": make_str(obj)
        }
        URL = 'https://api.telegram.org/bot856336707:AAFRfR3dP7XZLZL5MDuR2D2HitAvfUeYt94/sendMessage'
        requests.post(URL, data=payload)


post_save.connect(send_orders, sender=Order)
