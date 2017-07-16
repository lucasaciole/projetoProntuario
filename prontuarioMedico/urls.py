from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pacientes/$', views.paciente_index, name='paciente_index'),
    url(r'^medicos/$', views.medico_index, name='medico_index'),
    url(r'^cuidadores/$', views.cuidador_index, name='cuidador_index'),
    url(r'^cuidador/contratos/$', views.cuidador_contratos, name='cuidador_contratos'),
    url(r'^cuidador/novo/$', views.cuidador_novo, name='cuidador_novo'),
    url(r'^responsabilidades/$', views.responsavel_responsabilidades, name='responsabilidades'),
    url(r'^admin/$', views.admin_index, name='admin')
]
