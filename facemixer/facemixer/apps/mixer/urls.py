from django.urls import path
from . import views

urlpatterns = [
    path('addCat/', views.index, name='index'),
    path('mixer/', views.mix, name='mix'),
    path('top/', views.top, name='top'),
]

