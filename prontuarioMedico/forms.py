from django import forms
from django.core import validators
from django.utils.datetime_safe import datetime

choices_profissional = (
    ('n', 'Nao Profissional'),
    ('p', 'Profissional')
)

choices_estado  = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

class CuidadorForm(forms.Form):
    cpf_cuidador = forms.CharField(
        label='CPF',
        widget=forms.TextInput(attrs={'id': 'cpf' }),
        error_messages={
            'required': 'Digite o CPF',
            'invalid': 'CPF invalido'
        },
        help_text='Digite o CPF.'
    )
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite o nome do cuidador.',
            'invalid': 'Nome invalido'
        },
        help_text='Digite o nome do cuidador.'
    )
    tipoCuidador = forms.ChoiceField(
        choices=choices_profissional,
        required=False,
        error_messages={
            'required': 'Campo obrigatório.',
            'invalid': 'Tipo invalido'
        }
    )
    datanascimento = forms.CharField(
        widget=forms.TextInput(),
        required=True,
        error_messages={
            'required': 'Insira a data de nascimento.',
            'invalid': 'Data de nascimento invalida'
        },
        help_text='Insira a data de nascimento.'
    )
    logradouro = forms.CharField(
        label='Nome',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite o logradouro.',
            'invalid': 'Logradouro invalido'
        },
        help_text='Digite o logradouro.'
    )
    numero = forms.CharField(
        label='Numero',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite o Numero.',
            'invalid': 'Numero de end invalido'
        },
        help_text='Digite o Numero.'
    )
    bairro = forms.CharField(
        label='Bairro',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite o Bairro.',
            'invalid': 'Bairro invalido'
        },
        help_text='Digite o Bairro.'
    )
    complemento = forms.CharField(
        label='Complemento',
        widget=forms.TextInput(),
        required=False,
        help_text='Digite o Complemento.'
    )
    cidade = forms.CharField(
        label='Cidade',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite a Cidade.',
            'invalid': 'Cidade invalida'
        },
        help_text='Digite a Cidade.'
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=choices_estado,
        help_text='Selecione o Estado'
    )
    cep = forms.CharField(
        label='CEP',
        widget=forms.TextInput(),
        error_messages={
            'required': 'Digite o CEP.',
            'invalid': 'CEP invalido'
        },
        help_text='Digite o CEP.'
    )
    rg = forms.CharField(
        label='RG',
        required=False,
        widget=forms.TextInput(),
        help_text='Digite o RG.'
    )

class NameForm(forms.Form):
    nome_paciente = forms.CharField(label='nome_paciente', max_length=100)