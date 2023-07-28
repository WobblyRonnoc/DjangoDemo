from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm


def simple_response(request):
    return HttpResponse("Hello, world!, this is just a text response...not html")


def hello(request):
    return render(request, 'greet.html')


def hello_name(request, name=None):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'greet.html', {'name': name})
    elif request.method == 'GET':
        if not name:
            name = request.GET.get('name')  # http:// ... /greet/?name=John
        return render(request, 'greet.html', {'name': name})


def get_name(request, name=None):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'greet.html', {'name': name})
    else:
        form = MyForm(initial={'name': name}) if name else MyForm()

    return render(request, 'form.html', {'form': form})
