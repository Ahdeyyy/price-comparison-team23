from django.urls import path , include
from .views import ProductListView , product_detail , UserView , user_login
from django.contrib.auth import views as auth_views

app_name = 'price_compare'

urlpatterns = [
    path('',ProductListView.as_view(), name='landing'),
    path('<uuid:id>/<slug:product>',product_detail, name='product_detail'),
    path('signup/',UserView,name ='signup'),
    path('login/', auth_views.LoginView.as_view(),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]