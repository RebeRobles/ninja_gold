from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('process_money', views.process_money, name = 'process_money'),
    path('play_again',views.play_again, name = 'play_again'),
    
]