from django.urls import path
from . import views
urlpatterns = [

    path('suburl/',views.Suburl),
    path('',views.HomePage),
]