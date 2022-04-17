from django.urls import re_path

from tableApp import views

urlpatterns = [
    re_path(r'^$', views.MainPageView.as_view(), name='main')
]
