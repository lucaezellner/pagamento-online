from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.validators import RegexValidator
from crispy_forms.layout import Layout, Submit, Row, Column

class RecebedorForm(forms.Form):
    nome = forms.CharField()
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-mail')
    ddd = forms.CharField(label='DDD')
    telefone = forms.CharField()
    codigo_banco = forms.CharField(label='Código do Banco')
    agencia = forms.CharField(label='Agência')
    conta = forms.CharField()
    digito = forms.CharField(label='Dígito')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_action = 'criar-recebedor'
        
        self.helper.layout = Layout(
            'nome',
            'cpf',
            'email',
            Row(
                Column('ddd', css_class='form-group col-md-3 mb-0'),
                Column('telefone', css_class='form-group col-md-9 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('codigo_banco', css_class='form-group col-md-8 mb-0'),
                Column('agencia', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('conta', css_class='form-group col-md-9 mb-0'),
                Column('digito', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Criar recebedor', css_class='btn-block btn-primary')
        )

class TransacaoForm(forms.Form):
    valor = forms.FloatField(label='Valor da transação')
    recebedor_1_id = forms.CharField(label='ID do recebedor 1')
    recebedor_1_valor = forms.FloatField(label='Valor para recebedor 1')
    recebedor_2_id = forms.CharField(label='ID do recebedor 2')
    recebedor_2_valor = forms.FloatField(label='Valor para recebedor 2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_action = 'criar-transacao'
        
        self.helper.layout = Layout(
            'valor',
            Row(
                Column('recebedor_1_id', css_class='form-group col-md-6 mb-0'),
                Column('recebedor_1_valor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('recebedor_2_id', css_class='form-group col-md-6 mb-0'),
                Column('recebedor_2_valor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Realizar transação', css_class='btn-block btn-primary')
        )

class EstornoForm(forms.Form):
    transacao_id = forms.CharField(label='ID da transação')
    valor = forms.FloatField(label='Valor da transação')
    recebedor_1_id = forms.CharField(label='ID do recebedor 1')
    recebedor_1_valor = forms.FloatField(label='Valor para recebedor 1')
    split_1_id = forms.CharField(label='ID da split recebedor 1')
    recebedor_2_id = forms.CharField(label='ID do recebedor 2')
    recebedor_2_valor = forms.FloatField(label='Valor para recebedor 2')
    split_2_id = forms.CharField(label='ID da split recebedor 2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_action = 'estorno'
        
        self.helper.layout = Layout(
            Row(
                Column('transacao_id', css_class='form-group col-md-6 mb-0'),
                Column('valor', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('recebedor_1_id', css_class='form-group col-md-4 mb-0'),
                Column('recebedor_1_valor', css_class='form-group col-md-4 mb-0'),
                Column('split_1_id', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('recebedor_2_id', css_class='form-group col-md-4 mb-0'),
                Column('recebedor_2_valor', css_class='form-group col-md-4 mb-0'),
                Column('split_2_id', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Realizar estorno', css_class='btn-block btn-primary')
        )