from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_without_template(request):
    return HttpResponse('Hello, Django! (without template)')

def hello_with_template(request):
    return render(request, 'hello.html')
