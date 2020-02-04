from django.urls import path

from .views import OrderCreateView, BaseContactCreateView

urlpatterns = [
    path('order/', OrderCreateView.as_view(), name='order-create'),
    path('contact/', BaseContactCreateView.as_view(), name='contact-create')
]
