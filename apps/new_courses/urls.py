from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^confirm$', views.confirm),
    url(r'^deletecourse$', views.deletecourse),
    url(r'^comments$', views.comments),
    url(r'^newcomment$', views.newcomment)
]
