from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'calculators/index.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    minus = num1 - num2
    gob = num1 * num2

    if num2 != 0:
        div = num1 // num2
    else:
        div = '계산할 수 없습니다'
    

    context = {
        'num1' : num1,
        'num2' : num2,
        'munus' : minus,
        'div' : div,
        'gob' : gob,
    }

    return render(request, 'calculators/result.html', context)