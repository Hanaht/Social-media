
#urls.py
from django.contrib import admin  
from django.urls import path  
from calculatorapp import views  
from django.conf.urls import url
 
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    
    url(r'^create$', views.create, name='create'),
     ] 
