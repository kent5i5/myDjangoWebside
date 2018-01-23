'''
Created on Aug 29, 2017

@author: kenng
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]