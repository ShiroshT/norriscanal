from django.conf.urls import include, url
from django.contrib import admin
from boards import views
                    

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
]