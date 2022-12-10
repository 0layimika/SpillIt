from django.contrib import admin
from django.urls import path,include
from blogs import views

urlpatterns = [
   path('create', views.create , name='create'),
   path('<int:Blog_id>', views.detail, name='detail'),
   path('<int:Blog_id>/like', views.like, name='like'),
]