from django.urls import path , include
from .views import ProductListView , product_detail , UserView

app_name = 'price_compare'

urlpatterns = [
    path('',ProductListView.as_view()),
    path('<uuid:id>/<slug:product>',product_detail, name='product_detail'),
    path('signup/',UserView,name ='signup')
]