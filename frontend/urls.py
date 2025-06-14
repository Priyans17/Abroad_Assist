from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard , name="dashboard"),
    path('otpverification', views.otpvery , name="otp"),
    path("login",views.log , name="login"),
    path('registration', views.register , name="registration"),
    path("forgotpassword",views.forpass , name="forgotpassword"),
    path("logout",views.logot , name="logout"),
    path("pages/<str:page>",views.router , name="logout"),
    
    
    
]