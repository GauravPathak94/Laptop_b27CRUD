from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.registerView, name='register_url'),
    path('log/', views.loginView, name='loginpage_url'),
    path('lot/', views.logoutView, name='logout_url'),
    path('otp/', views.OTPview, name='otp_url')

]