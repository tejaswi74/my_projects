from django.urls import path
from . import views
urlpatterns = [
    path('greet/', views.greet, name='greet'),
    path('', views.myapp_home, name='myapp_home'), 
]
