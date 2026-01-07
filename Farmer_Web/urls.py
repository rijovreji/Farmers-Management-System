from django.urls import path
from Farmer_Web import views

urlpatterns = [
    path('Home_Farmers/', views.Home_Farmers, name='Home_Farmers'),
    ]