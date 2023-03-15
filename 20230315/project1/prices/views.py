from django.shortcuts import render

# Create your views here.
def sum_num(request,food,cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    price = product_price.get('food')
    # product_price.get() -> 없는 경우 None
    # product_price[food] -> 없는 경우 에러

    # if food in product_price:
    #     계산

    context={
        'food' : food,
        'cnt':cnt,
        'product_price': product_price,
        'price':price,
        'total':price*cnt
    }
    return render(request,'prices/index.html',context)