from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^paciente/$', views.paciente, name='paciente'),
    url(r'^cuidador/$', views.cuidador_index, name='cuidador'),
    url(r'^cuidador/contratos/$', views.cuidador_contratos, name='cuidador_contratos')
]
