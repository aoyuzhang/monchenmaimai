from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('', views.home, name="home"),
    path('', views.sales, name = "sales"),
    path('', views.tools, name = "tools"),
    path('', views.news, name ="news"),
]

