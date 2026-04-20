from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [

    path('suburl/',views.Suburl),
    path('',views.HomePage),
    path('temp/',views.myView),
    path('db/',views.IndexView.as_view(),name='db'),
    path('db/<int:pk>',views.FoodDetailView.as_view(),name='detail'),
    path('add/',views.createView.as_view()),
    path('db/update/<int:pk>/',views.itemUpdateView.as_view(),name='update_item'),
    path('delete/<int:pk>',views.Item_DeleteView.as_view(),name='delete_item')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)