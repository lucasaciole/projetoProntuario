from django import forms
from django.core import validators
from django.utils.datetime_safe import datetime

numeric = validators.RegexValidator(r'^[0-9]*$', 'Apenas numeros são permitidos')
alphabetic = validators.RegexValidator(r'^[a-zA-z]*$', 'Apenas letras são permitidos')
alphanumeric = validators.RegexValidator(r'^[0-9a-zA-Z]*$', 'Apenas letras e numeros são permitidos')

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
        validators=[numeric],
        widget=forms.TextInput(attrs={'id': 'cpf', 'placeholder': 'CPF' }),
        error_messages={
            'required': 'Digite o CPF'
        },
        help_text='Digite o CPF.'
    )
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={'placeholder': 'Nome'}),
        validators=[alphabetic],
        error_messages={
            'required': 'Digite o nome do cuidador.'
        },
        help_text='Digite o nome do cuidador.'
    )
    tipoCuidador = forms.ChoiceField(
        choices=choices_profissional,
        # widget=forms.RadioSelect(),
        required=False,
        error_messages={
            'required': 'Campo obrigatório.'
        }
    )
    datanascimento = forms.DateField(
        initial=datetime.today(),
        error_messages={
            'required': 'Insira a data de nascimento.'
        },
        help_text='Insira a data de nascimento.'
    )
    logradouro = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={'placeholder': 'Logradouro'}),
        error_messages={
            'required': 'Digite o logradouro.'
        },
        help_text='Digite o logradouro.'
    )
    numero = forms.CharField(
        label='Numero',
        widget=forms.TextInput(attrs={'placeholder': 'Numero'}),
        validators=[alphanumeric],
        error_messages={
            'required': 'Digite o Numero.'
        },
        help_text='Digite o Numero.'
    )
    bairro = forms.CharField(
        label='Bairro',
        widget=forms.TextInput(attrs={'placeholder': 'Bairro'}),
        error_messages={
            'required': 'Digite o Bairro.'
        },
        help_text='Digite o Bairro.'
    )
    complemento = forms.CharField(
        label='Complemento',
        widget=forms.TextInput(attrs={'placeholder': 'Complemento'}),
        help_text='Digite o Complemento.'
    )
    cidade = forms.CharField(
        label='Cidade',
        widget=forms.TextInput(attrs={'placeholder': 'Cidade'}),
        error_messages={
            'required': 'Digite a Cidade.'
        },
        help_text='Digite a Cidade.'
    )
    estado = forms.ChoiceField(
        label='Estado',
        choices=choices_estado,
        #widget=forms.RadioSelect(),
        help_text='Selecione o Estado'
    )
    cep = forms.CharField(
        label='CEP',
        widget=forms.TextInput(attrs={'placeholder': 'CEP'}),
        error_messages={
            'required': 'Digite o CEP.'
        },
        help_text='Digite o CEP.'
    )
    rg = forms.CharField(
        label='RG',
        widget=forms.TextInput(attrs={'placeholder': 'RG'}),
        help_text='Digite o RG.'
    )
