from django.urls import path
from . import views

urlpatterns = [
    # Маршрут для главной страницы
    path('', views.home_page, name='home_page'),
    # Маршрут для страницы контактов
    path('contacts/', views.contacts, name='contacts'),
]
