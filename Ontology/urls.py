from django.conf.urls import url
from . import views

app_name = 'Ontology'

urlpatterns = [
    url(r'^$', views.index, name='index')
]