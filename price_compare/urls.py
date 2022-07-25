from django.urls import path
from .views import test

app_name = 'price_compare'

urlpatterns = [
    path('',test), 
]