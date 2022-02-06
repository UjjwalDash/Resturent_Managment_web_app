from django.urls import path
from . import views

urlpatterns=[
    path('',views.book,name='index'),
    path('add.html',views.add,name='add'),
    path('update_price.html',views.update_price,name='update_price'),
    path('update_image.html',views.update_image,name='update_image'),
    path('delete.html',views.delete,name='delete'),
    path('show.html',views.show,name='show'),
    path('index.html',views.book,name='index'),
    path('insert',views.insert,name='insert')
]