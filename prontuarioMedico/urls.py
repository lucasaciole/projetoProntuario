from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^paciente/$', views.paciente, name='paciente'),
    url(r'^cuidador/$', views.cuidador, name='cuidador'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^cuidador/contratos/$', views.cuidador_contratos, name='cuidador_contratos')

]
