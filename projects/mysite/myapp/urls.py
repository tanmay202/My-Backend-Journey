from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [

    path('suburl/',views.Suburl),
    path('',views.HomePage),
    path('temp/',views.myView),
    path('db/',views.DataBase,name='db'),
    path('db/<int:id>',views.detail,name='detail'),
    path('add/',views.create_item),
    path('db/update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>',views.delete_item,name='delete_item')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)