from django.urls import path
from .views import ProductListView , product_detail

app_name = 'price_compare'

urlpatterns = [
    path('',ProductListView.as_view()),
    path('<uuid:id>/<slug:product>',product_detail, name='product_detail')
]