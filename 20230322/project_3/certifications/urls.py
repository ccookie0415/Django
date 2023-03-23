from django.urls import path
from . import views

urlpatterns = [
    path('certification1/', views.index_1),
    path('certification2/', views.index_2),
    path('certification3/', views.index_3),
]

