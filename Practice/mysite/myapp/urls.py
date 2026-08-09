from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.First),
    path('<int:id>',views.detail,name='detail')
]


