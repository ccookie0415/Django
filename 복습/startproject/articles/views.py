from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def hello(request,name):
    context = {
        'name' : name,
    }

    return render(request, 'articles/hello.html', context)