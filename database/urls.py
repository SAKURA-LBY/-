from django.conf.urls import url,include
from django.contrib import admin
from .import views
urlpatterns = [
    url(r'^django/$', views.UpdateDb.as_view()),
    url(r'^book/$',views.book),
    url(r'^hero/$',views.hero),
    url(r'^select/$',views.select),
]
