from django.shortcuts import render

# Create your views here.

def first(request):
    second_throw = request.GET.get('second_throw')

    context = {
        'second_throw' : second_throw
    }

    return render(request, 'throw_catch/first.html', context)

def second(request):
    first_throw = request.GET.get('first_throw')
    
    context = {
        'first_throw' : first_throw
    }

    return render(request, 'throw_catch/second.html', context)