from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return render(response, 'index.html', {
        "index": "index",
        "header_message": "This page is actually 127.0.0.1:8000/home/index.html"})
