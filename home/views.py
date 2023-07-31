from django.shortcuts import render


def index(response):
    return render(response, 'index.html', {"header_message": "Welcome to the Home app!"})
