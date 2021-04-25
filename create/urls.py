from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.accounts, name='accounts'),
    path('login/<int:id>',views.loginView, name="logins-view"),
    path('edit/<int:id>', views.editUser, name="edit-user"),
    path('delete/<int:id>', views.deleteUser, name="delete-user"),

]