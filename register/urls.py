from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path("register",views.register,name="register_"),
    path("login",views.login,name="login_"),
    path('logout',views.logout,name="logout_")
]