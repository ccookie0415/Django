from django.shortcuts import render, redirect

# Create your views here.

def first(request):
    third_thing = request.GET.get('third_thing')

    context = {
        'third_thing' : third_thing
    }

    return render(request,'throw_loops/first.html', context)

def second(request):
    first_thing = request.GET.get('first_thing')

    context = {
        'first_thing' : first_thing
    }

    
    return render(request,'throw_loops/second.html', context)

def third(request):
    second_thing = []
    second_thing.append(request.GET.get('second_thing_1'))
    second_thing.append(request.GET.get('second_thing_2'))

    context = {
        'second_thing' : second_thing
    }
    return render(request, 'throw_loops/third.html', context)