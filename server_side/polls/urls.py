from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.upload_file, name='upload_file'),
    url(r'^upload_file/', views.upload_file),
]


