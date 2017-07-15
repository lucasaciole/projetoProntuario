from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^paciente/$', views.paciente_index, name='paciente'),
    url(r'^medico/$', views.medico_index, name='medico'),
    url(r'^cuidador/$', views.cuidador_index, name='cuidador'),
    url(r'^cuidador/contratos/$', views.cuidador_contratos, name='cuidador_contratos'),
    url(r'^cuidador/novo/$', views.cuidador_novo, name='cuidador_novo'),
    url(r'^responsavel/$', views.responsavel_index, name='responsavel'),
    url(r'^admin/$', views.admin_index, name='admin')
]
