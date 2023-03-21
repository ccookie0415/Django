from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # path('throw/', views.throw, name='throw'),
    # path('catch/', views.catch, name='catch'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
