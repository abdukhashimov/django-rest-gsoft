from django.contrib import admin

from order.models import BaseContact, Order

admin.site.register(BaseContact)
admin.site.register(Order)
