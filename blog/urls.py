from django.urls import path, include
from blog import views


urlpatterns = [

    path('', views.allblog, name='blog'),

]
