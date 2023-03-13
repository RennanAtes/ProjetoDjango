from django.shortcuts import render
import json
# Create your views here.
import requests

def portfolio(request):
    return render(request,'portfolio/index.html')


def cepAPI(request):
    cep = request.POST.get('CEP')
    print(cep)
    nocep = {'noCEP': False}
    if request.method == 'POST':
        cep = cep.replace("-", "")
        if cep.isdigit():
            if len(cep) == 8:
                url = f'https://viacep.com.br/ws/{cep}/json/'
                response = requests.get(url)
                endereco = json.loads(response.text)
                if not 'erro' in endereco:
                    dados = {'aprovado': True, 
                            'logradouro' : endereco['logradouro'],
                            'bairro' : endereco['bairro'],
                            'localidade' : endereco['localidade'],
                            'uf' : endereco['uf'],
                            'ddd' : endereco['ddd'],
                            'ibge' : endereco['ibge'],
                            'siafi' : endereco['siafi']
                                }
                    return render(request,'CEP/index.html',dados)
            nocep = {'noCEP': True}
            return render(request,'CEP/index.html',nocep)
    return render(request,'CEP/index.html')


    
def login(request):
    return render(request,'login/index.html')
def sendKindle(request):
    return render(request,'kindleSendPDF/index.html')