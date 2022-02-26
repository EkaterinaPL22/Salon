from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make-order', views.make_order, name='make-order'),
]