from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts', views.accounts, name='accounts'),
    path('login/<int:id>',views.loginView, name="logins-view"),
    path('edit/<int:id>', views.editLogin, name="edit-task"),

]