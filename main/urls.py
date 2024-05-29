from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для главной страницы
    path('', views.home_page, name='home_page'),
    # Маршрут для страницы контактов
    path('contacts/', views.contacts, name='contacts'),
    # Маршрут для страницы меню
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
]
