from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# def throw(request):
#     return render(request, 'articles/throw.html')

# def catch(request):
#     message = request.GET.get('message')

#     context = {
#         'message' : message
#     }
#     print(message)
#     return render(request, 'articles/catch.html', context)

def index(request):
    articles = Article.objects.all()

    context ={
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)

def detail(request,id):
    article = Article.objects.get(id=id)

    context ={
        'article' : article,
    }
    return render(request, 'articles/detail.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')