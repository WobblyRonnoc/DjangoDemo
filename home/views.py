from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return render(response, 'index.html', {
        "index": "index",
        "header_message": "Welcome to the Django Demo"})
