from django.shortcuts import render, redirect
from .forms import RecebedorForm, TransacaoForm
import requests
import json
import os
from os.path import dirname, join
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), "../.ENV")

# Load file from the path.
load_dotenv(dotenv_path)

def home(request):
    recebedor_form = RecebedorForm
    transacao_form = TransacaoForm
    pagarme_api = os.getenv("PAGARME_API_KEY")
    return render(request, "main/home.html",{"page_title": "Pagamento Online", "recebedor_form": recebedor_form, "transacao_form": transacao_form, "pagarme_api": pagarme_api})

def criar_recebedor(request):
    if request.method == 'POST':
        form = RecebedorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf'].replace('.', '').replace('-', '')
            email = form.cleaned_data['email']
            ddd = form.cleaned_data['ddd'].replace('(', '').replace(')', '')
            telefone = form.cleaned_data['telefone'].replace('-', '')
            codigo_banco = form.cleaned_data['codigo_banco']
            agencia = form.cleaned_data['agencia']
            conta = form.cleaned_data['conta']
            digito = form.cleaned_data['digito']

            url = "https://api.pagar.me/1/recipients/?api_key=" + os.getenv("PAGARME_API_KEY")
            headers = {
                'Content-Type': 'application/json',
                'Connection' : 'keep-alive',
                'Accept': "*/*"
            }
            data = {
                "anticipatable_volume_percentage": "85", 
                "automatic_anticipation_enabled": "true",
                "transfer_day": "5", 
                "transfer_enabled": "true", 
                "transfer_interval": "weekly",
                "postback_url": "https://requestb.in/tl0092tl",
                "bank_account": {
                    "object": "bank_account",
                    "bank_code": codigo_banco,
                    "agencia": agencia,
                    "agencia_dv": "5",
                    "conta": conta,
                    "conta_dv": digito,
                    "type": "conta_corrente",
                    "document_type": "cpf",
                    "document_number": cpf,
                    "legal_name": nome,
                },
                "register_information": {
                        "type": "individual",
                        "document_number": cpf,
                        "name": nome,
                        "site_url":"http://www.site.com",
                        "email": email,
                        "phone_numbers": [{
                            "ddd": ddd,
                            "number": telefone,
                            "type": "mobile"
                    }]
                }
            }
            r = requests.post(url, data=json.dumps(data), headers=headers)
            print(r.json())
            return redirect('home')
        else:
            print('invalido')

def criar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            valor = form.cleaned_data['valor'] * 100
            recebedor_1_id = form.cleaned_data['recebedor_1_id']
            recebedor_1_valor = form.cleaned_data['recebedor_1_valor'] * 100
            recebedor_2_id = form.cleaned_data['recebedor_2_id']
            recebedor_2_valor = form.cleaned_data['recebedor_2_valor'] * 100

            url = "https://api.pagar.me/1/transactions/?api_key=" + os.getenv("PAGARME_API_KEY")
            headers = {
                'Content-Type': 'application/json',
                'Connection' : 'keep-alive',
                'Accept': "*/*"
            }
            data = {
                "amount": valor,
                "card_number": "4111111111111111",
                "card_cvv": "123",
                "card_expiration_date": "0922",
                "card_holder_name": "Morpheus Fishburne",
                "customer": {
                "external_id": "#3311",
                "name": "Morpheus Fishburne",
                "type": "individual",
                "country": "br",
                "email": "mopheus@nabucodonozor.com",
                "documents": [
                    {
                    "type": "cpf",
                    "number": "30621143049"
                    }
                ],
                "phone_numbers": ["+5511999998888", "+5511888889999"],
                "birthday": "1965-01-01"
                },
                "billing": {
                "name": "Trinity Moss",
                "address": {
                    "country": "br",
                    "state": "sp",
                    "city": "Cotia",
                    "neighborhood": "Rio Cotia",
                    "street": "Rua Matrix",
                    "street_number": "9999",
                    "zipcode": "06714360"
                }
                },
                "split_rules": [
                    {
                        "amount": recebedor_1_valor,
                        "recipient_id": recebedor_1_id
                    },
                    {
                        "amount": recebedor_2_valor,
                        "recipient_id": recebedor_2_id
                    }
                ],
                "shipping": {
                "name": "Neo Reeves",
                "fee": 1000,
                "delivery_date": "2000-12-21",
                "expedited": True,
                "address": {
                    "country": "br",
                    "state": "sp",
                    "city": "Cotia",
                    "neighborhood": "Rio Cotia",
                    "street": "Rua Matrix",
                    "street_number": "9999",
                    "zipcode": "06714360"
                }
                },
                "items": [
                {
                    "id": "r123",
                    "title": "Red pill",
                    "unit_price": 100000,
                    "quantity": 1,
                    "tangible": True
                },
                {
                    "id": "b123",
                    "title": "Blue pill",
                    "unit_price": 100000,
                    "quantity": 1,
                    "tangible": True
                }
                ]
            }

            r = requests.post(url, data=json.dumps(data), headers=headers)
            print(r.json())

            return redirect('home')
        else:
            print('invalido')


