from django.urls import path
from . import views

app_name = 'helloApp'
urlpatterns = [

    path('text/', views.simple_response, name='simple_response'),
    path('greet/', views.hello, name='greet'),
    path('greet/<str:name>/', views.hello_name, name='greet_with_name'),
    path('form/', views.get_name, name='form'),
]
