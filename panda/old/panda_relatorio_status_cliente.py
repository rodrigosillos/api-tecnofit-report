import pandas as pd
import requests
import json

hed = {
    'Host': 'app.tecnofit.com.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'traceparent': '00-d38cdfe66062e7bbc98191fd93d3afc4-3ea8b3bef80835e4-01',
    'tracestate': '864337@nr=0-1-864337-431486236-3ea8b3bef80835e4----1651518266520',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '56',
    'Origin': 'https://app.tecnofit.com.br',
    'Connection': 'keep-alive',
    'Referer': 'https://app.tecnofit.com.br/relatorio/statuscliente',
    'Cookie': '_ga=GA1.3.2042638173.1650650835; _hjSessionUser_1292435=eyJpZCI6ImIwN2RjZDE0LTk4OTAtNTQxZC04NDQ1LWM4YjMxNzRmNWNiYiIsImNyZWF0ZWQiOjE2NTA2NTA4MzUwMjgsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1650650854080; _fw_crm_v=4deea7cd-78f6-4234-82a1-c5448fea63c7; _gcl_au=1.1.1634836036.1652110427; _ga_1HNXM65J3Z=GS1.1.1652110427.1.0.1652110441.46; _ga_DM66BBR3WS=GS1.1.1652110427.1.0.1652110441.0; _uetvid=6b49b590cfad11eca387fb4100a9d87f; _fbp=fb.2.1652110429214.473566132; __hstc=217517065.3e170c767eedd704aadd0cd9b9843e98.1652110430171.1652110430171.1652110430171.1; hubspotutk=3e170c767eedd704aadd0cd9b9843e98; messagesUtk=c77a71358d954f048b46f5b4f09b25d1; PHPSESSID=9bm4ceur1ag27ls0df7256ajmg; _gid=GA1.3.924003814.1655133721; _gat=1; _hjIncludedInSessionSample=0; _hjSession_1292435=eyJpZCI6ImI5ODQyOTgyLWRkZmMtNGZmZS05NjQ5LWRmZTQ3OWJmZTAzZiIsImNyZWF0ZWQiOjE2NTUxMzM3MjEyMTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gat_UA-52493754-1=1; NPS_3add8e44_throttle=1655176943021',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

data = {'mostrar_contato' : 'on'}
url = 'https://app.tecnofit.com.br/relatorio/statuscliente/listar'

r = requests.post(url, json=data, headers=hed)

table_MN = pd.read_html(r.text)

resultado = table_MN[0].to_json(orient="split")
json_data = json.loads(resultado)

for lead in json_data['data']:
    codigo = lead[1]
    cliente = lead[2]
    nascimento = lead[3]
    sexo = lead[4]
    consultor = lead[5]
    professor = lead[6]
    ultimo_status = lead[7]
    status_cliente = lead[8]
    email = lead[9]
    contato = lead[10]

    print(contato)