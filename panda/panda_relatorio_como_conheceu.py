import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from unicodedata import normalize

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
    'Referer': 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar',
    'Cookie': '_ga=GA1.3.2042638173.1650650835; _hjSessionUser_1292435=eyJpZCI6ImIwN2RjZDE0LTk4OTAtNTQxZC04NDQ1LWM4YjMxNzRmNWNiYiIsImNyZWF0ZWQiOjE2NTA2NTA4MzUwMjgsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1650650854080; _fw_crm_v=4deea7cd-78f6-4234-82a1-c5448fea63c7; _gcl_au=1.1.1634836036.1652110427; _ga_1HNXM65J3Z=GS1.1.1652110427.1.0.1652110441.46; _ga_DM66BBR3WS=GS1.1.1652110427.1.0.1652110441.0; _uetsid=6b49ab30cfad11ec815655ccf127f051; _uetvid=6b49b590cfad11eca387fb4100a9d87f; _fbp=fb.2.1652110429214.473566132; __hstc=217517065.3e170c767eedd704aadd0cd9b9843e98.1652110430171.1652110430171.1652110430171.1; hubspotutk=3e170c767eedd704aadd0cd9b9843e98; __hssrc=1; messagesUtk=c77a71358d954f048b46f5b4f09b25d1; PHPSESSID=slnsom5slfplm5lf1qekb3gu31; _gid=GA1.3.516891763.1652110446; NPS_3add8e44_throttle=1652153653333; _gat=1; _gat_UA-52493754-1=1; _hjAbsoluteSessionInProgress=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

data = {
    'data_inicial' : '01/04/2022',
    'data_final' : '30/04/2022',
    'status_pessoa_id[]' : '1'
}

url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'

r = requests.post(url, json=data, headers=hed)

# table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='Election results from statewide races')
table_MN = pd.read_html(r.text)

df = table_MN[0]

result = df.to_json(orient="split")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))

# print(df.head())
# print(df.info())
# print(df['Status Cliente'])
