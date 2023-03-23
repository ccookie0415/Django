from django.shortcuts import render
import random

# Create your views here.
ages = range(25,31)
grades = ['a','b','c','s']



def index_1(request):
    age = random.choice(ages)
    grade = random.choice(grades)
    name = 'kim happy'

    context = {
        'age' : age,
        'grade' : grade,
        'name' : name,
    }

    return render(request, 'certifications/index_1.html', context)


def index_2(request):
    age = random.choice(ages)
    grade = random.choice(grades)
    name = 'lee happy'

    context = {
        'age' : age,
        'grade' : grade,
        'name' : name,
    }

    return render(request, 'certifications/index_2.html', context)


def index_3(request):
    age = random.choice(ages)
    grade = random.choice(grades)
    name = 'park happy'

    context = {
        'age' : age,
        'grade' : grade,
        'name' : name,
    }

    return render(request, 'certifications/index_3.html', context)

