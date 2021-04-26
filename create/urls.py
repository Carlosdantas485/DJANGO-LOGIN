from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.accounts, name='accounts'),
    path('idea/<int:id>',views.ideaView, name="idea-view"),
    path('edit/<int:id>', views.editUser, name="edit-idea"),
    path('delete/<int:id>', views.deleteUser, name="delete-idea"),

]