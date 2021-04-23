from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('accounts', views.accounts, name='accounts'),
    path('/task/<int:id>',views.loginview, name="login-view"),
]