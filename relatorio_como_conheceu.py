import requests

auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOTAzMjAwLCJlbXByZXNhX2lkIjo0MDAzLCJpc3MiOiJUZWNub2ZpdCIsImV4cCI6MTgwOTI4Mzg2MCwic3ViIjoiIiwiYXVkIjoiIn0.ty2L_f4K53VSMg50yLwqFNkskM2qqUTDYHtPDdhuK2w'

# hed = {'Authorization': 'Bearer ' + auth_token}

hed = {
    'Host': 'app.tecnofit.com.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    # 'X-NewRelic-ID': 'XAADUlVUGwcDVVVaAgUCVQ==',
    #cle'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiIzZWE4YjNiZWY4MDgzNWU0IiwidHIiOiJkMzhjZGZlNjYwNjJlN2JiYzk4MTkxZmQ5M2QzYWZjNCIsInRpIjoxNjUxNTE4MjY2NTIwfX0=',
    'traceparent': '00-d38cdfe66062e7bbc98191fd93d3afc4-3ea8b3bef80835e4-01',
    'tracestate': '864337@nr=0-1-864337-431486236-3ea8b3bef80835e4----1651518266520',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Content-type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '56',
    'Origin': 'https://app.tecnofit.com.br',
    'Connection': 'keep-alive',
    'Referer': 'https://app.tecnofit.com.br/relatorio/statuscliente',
    'Cookie': '_ga=GA1.3.2042638173.1650650835; _hjSessionUser_1292435=eyJpZCI6ImIwN2RjZDE0LTk4OTAtNTQxZC04NDQ1LWM4YjMxNzRmNWNiYiIsImNyZWF0ZWQiOjE2NTA2NTA4MzUwMjgsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1650650854080; _fw_crm_v=4deea7cd-78f6-4234-82a1-c5448fea63c7; _gid=GA1.3.1976918264.1651517491; PHPSESSID=dj48bubce0at50m4ng05gj24fn; _hjSession_1292435=eyJpZCI6ImU2ZWJjY2MyLThiYjEtNDdmZS04Nzc2LWUxZmI4MTJjYzhhOSIsImNyZWF0ZWQiOjE2NTE1MTc0OTE0NDQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_UA-52493754-1=1; _gat=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

data = {
    'data_inicial' : '01/04/2022',
    'data_final' : '30/04/2022',
    'grafico' : '1',
    'status_pessoa_id[]' : '1',
}

url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'
response = requests.post(url, json=data, headers=hed)
# print(response)
print(response.json())
