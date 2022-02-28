from django.urls import path
from src.sells import views

urlpatterns = [
    path('', views.index),
    path('delete_sell/<int:sell_id>', views.delete_sell),
    path('create_sell', views.create_sell),
    path('update_sell/<int:sell_id>', views.update_sell),
    ]