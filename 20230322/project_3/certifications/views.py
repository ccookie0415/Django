from django.shortcuts import render
import random

# Create your views here.

def index(request):
    ages = range(25,31),
    grades = ['a','b','c','s']
    names = ['kim happy', 'park happy', 'lee happy']

    age = random.choice(ages)
    grade = random.choice(grades)

    context = {
        'age' : age,
        'grade' : grade,
        'name' : name,
    }
    
    return render(request, 'certifications/index.html', context)
