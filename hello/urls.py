from django.urls import path
from . import views

urlpatterns = [
    path('response/', views.hello_without_template, name='hello1'),
    path('template/', views.hello_with_template, name='hello2'),
]