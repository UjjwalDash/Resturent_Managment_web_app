from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.book,name='index'),
    path('add.html',views.add,name='add'),
    path('success', views.success, name = 'success'),
    path('update_price.html',views.update_price,name='update_price'),
    path('update_image.html',views.update_image,name='update_image'),
    path('delete.html',views.delete,name='delete'),
    path('show.html',views.show,name='show'),
    path('index.html',views.book,name='index'),
    path('insert',views.insert,name='insert')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)