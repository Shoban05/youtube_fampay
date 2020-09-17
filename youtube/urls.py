from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_all/', views.get_all, name='get_all'),
    url(r'^search/', views.search, name='search'),
]