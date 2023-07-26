from django.urls import path
from . import views

app_name = 'helloApp'
urlpatterns = [
    path('greet/', views.hello_function, name='greet'),
]
