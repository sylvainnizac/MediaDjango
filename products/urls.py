from django.urls import path
from products import views

urlpatterns = [
    path('', views.index),
    path('all_products', views.all_products),
    path('delete_product/<int:product_id>', views.delete_product),
    path('create_product', views.create_product),
    path('update_product/<int:product_id>', views.update_product),
]
