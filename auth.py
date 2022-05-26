import requests
import json
import pprint

url = 'https://api.tecnofit.com.br/auth'
# url = 'https://app.tecnofit.com.br/login/main/login'
# url = 'https://app.tecnofit.com.br/relatorio/statuscliente/listar'

data = {"email":"contato@superforcecrossfit.com","password":"Superforce380*","goTo": ''}
# data = {"mostrar_contato":"on"}
# params = {'PHPSESSID': '14q51a55vi6mh04cklpe8cfjrn'}
params = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOTAzMjAwLCJlbXByZXNhX2lkIjo0MDAzLCJpc3MiOiJUZWNub2ZpdCIsImV4cCI6MTgwODk0MTkyMCwic3ViIjoiIiwiYXVkIjoiIn0.9yendWa7p9vwJ_PWORBCxaUanOE6DzHkI5f2LDvNln4'}
headers = {'Content-type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

pprint.pprint(response.json())
