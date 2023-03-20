from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):

    name = 'hyejin'

    return HttpResponse(f"hi {name}!")

def greeting(request):
    
    foods = ['apple','banana','coconut']
    info = {
        'name' : 'hyejin'
    }
    context = {
        'foods' : foods,
        'info' : info,
    }


    return render(request, 'myapp/greeting.html', context)

def dinner(request):
    foods = ['족발','햄버거','치킨','초밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }

    return render(request, 'myapp/dinner.html', context)

