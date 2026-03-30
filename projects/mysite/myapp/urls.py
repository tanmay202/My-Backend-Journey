from django.urls import path
from . import views
urlpatterns = [

    path('suburl/',views.Suburl),
    path('',views.HomePage),
    path('temp/',views.myView),
    path('db/',views.DataBase),
    path('db/<int:id>',views.detail),
]