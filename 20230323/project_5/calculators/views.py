from django.shortcuts import render

# Create your views here.

def index(request,num1,num2):

    num1 = num1
    num2 = num2
    minus = num1 - num2
    gob = num1 * num2

    if num2 != 0:
        div = num1 / num2
    else:
        div = '계산할 수 없습니다'
    

    context = {

        'num1' : num1,
        'num2' : num2,
        'minus' : minus,
        'gob' : gob,
        'div' : div,

    }

    return render(request, 'calculators/index.html', context)