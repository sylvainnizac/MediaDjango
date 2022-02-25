from django.urls import path
from sells import views

urlpatterns = [
    path('', views.index),
    # path('all_products', views.all_products),
    # path('delete_product/<int:product_id>', views.delete_product),
    path('create_sell', views.create_sell),
    # path('update_product/<int:product_id>', views.update_product),
]