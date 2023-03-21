from django.shortcuts import render

# Create your views here.

def foods(request,food,cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    if food in product_price:
        total = product_price.get(food) * cnt

    else:
        total = None

    context = {
        'food' : food,
        'cnt' : cnt,
        'total' : total
    }

    return render(request, 'prices/index.html', context)