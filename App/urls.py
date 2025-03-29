from django.urls import path
from .views import home, product_list, search_product

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('search/', search_product, name='search_product'),
]
