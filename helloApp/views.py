from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#
def hello_function(request):
    name = request.GET.get('name', None)
    return render(request, 'greet.html', {'name': name})
