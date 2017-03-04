from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^process$', views.create),
    url(r'^success$', views.success),
    url(r'^$', views.index, name='index'),
]
