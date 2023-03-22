from django.urls import path
from . import views


app_name = 'calculators'
urlpatterns = [
    path('calculation/', views.index, name='calculation'),
    path('result/',views.result, name='result'),
]