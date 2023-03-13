import requests
import json
def cepAPidados(cep):
    if cep.isdigit():
        if len(cep) == 8:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            response = requests.get(url)
            endereco = json.loads(response.text)
            dados = {'aprovado': True, 
                    'logradouro' : endereco['logradouro'],
                    'bairro' : endereco['bairro'],
                    'localidade' : endereco['localidade'],
                    'uf' : endereco['uf'],
                    'ddd' : endereco['ddd'],
                    'ibge' : endereco['ibge'],
                    'siafi' : endereco['siafi']
                        }
            return dados
    else:
        return False