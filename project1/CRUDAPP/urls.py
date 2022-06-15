from django.urls import path
from . import views

urlpatterns = [
    path('ev/', views.LaptopView, name='lapform_url'),
    path('sv/', views.showLaptopView, name='showlap_url'),
    path('uv/<int:id>/', views.updateLaptopView, name='updatelap_url'),
    path('dl/<int:id>/', views.deleteLaptopView, name='deletelap_url')
]