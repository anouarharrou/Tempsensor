from . import views   
from . import api        
from django.urls import path

#URL Conf

urlpatterns=[
    
    path('', views.welcome, name='welcome'),
    path('home/', views.welcome1, name='welcome1'),
    path('tempsensor/',views.mydb1,name='mydb1'),
    path('temp/', views.mydb2, name='mydb2'),
    path('tuto/', views.tutorial, name='tutorial'),
    path('api/', api.Dlist, name='Dlist'),
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
    
    
]
