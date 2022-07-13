from django.urls import path
from .views import home, register, login, items_register

urlpatterns = [
    path('', login, name='login'),
    path('home', home, name='home'),
    path('register', register, name='register'),
    path('items_register', items_register, name='items_register'),

]
