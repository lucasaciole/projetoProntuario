from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pacientes/$', views.paciente_index, name='paciente_index'),
    url(r'^medicos/$', views.medico_index, name='medico_index'),
    url(r'^cuidadores/$', views.cuidador_index, name='cuidador_index'),
    url(r'^cuidador/(?P<id>\d+)/$', views.cuidador_detalhes, name='cuidador_detalhes'),
    url(r'^cuidador/contratos/$', views.cuidador_contratos, name='cuidador_contratos'),
    url(r'^cuidador/contrato/(?P<id>\d+)/$', views.cuidador_contrato_detalhes, name='contrato_detalhes'),
    url(r'^cuidador/contrato/novo/$', views.cuidador_contrato_novo, name='contrato_novo'),
    url(r'^cuidador/novo/$', views.cuidador_novo, name='cuidador_novo'),
    url(r'^cuidador/atendimentos/$', views.cuidador_atendimentos, name='cuidador_atendimentos'),
    url(r'^cuidador/planos/$', views.cuidador_planos, name='cuidador_planos'),
    url(r'^cuidador/plano/(?P<id>\d+)/$', views.cuidador_planos_detalhes, name='plano_detalhes'),
    url(r'^cuidador/plano/novo/$', views.cuidador_planos_novo, name='plano_novo'),
    url(r'^cuidador/plano/novo/atividade/(?P<id>\d+)/$', views.cuidador_atividades_novo, name='atividade_novo'),
    url(r'^cuidador/atendimento/(?P<id>\d+)/$', views.cuidador_atendimentos_detalhes,
        name='cuidador_atendimentos_detalhes'),
    url(r'^cuidador/atendimento/(?P<id>\d+)/nova_intercorrencia$', views.atendimento_nova_intercorrencia,
        name='nova_intercorrencia'),
    url(r'^cuidador/atendimento/(?P<id>\d+)/nova_atividade$', views.atendimento_nova_atividade,
        name='nova_atividade'),
    url(r'^cuidador/atendimento/(?P<id_atendimento>\d+)/atividade/(?P<id_atividade>\d+)/nova_medida/$', views.atendimento_nova_medida,
        name='nova_medida'),
    url(r'^cuidador/atendimento/novo$', views.novo_atendimento, name='novo_atendimento'),
    url(r'^responsabilidades/$', views.responsavel_responsabilidades, name='responsabilidades'),
    url(r'^admin/$', views.admin_index, name='admin')
]
