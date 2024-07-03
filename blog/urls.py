from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('create/', views.create_post, name='create-post'),
]

