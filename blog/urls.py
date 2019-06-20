from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    path('lista', views.post_list, name='post_list'),
    path('',views.index),
    url(r'^form', views.posteo),
]