import requests
from lxml import etree

auth_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOTAzMjAwLCJlbXByZXNhX2lkIjo0MDAzLCJpc3MiOiJUZWNub2ZpdCIsImV4cCI6MTgwOTI4Mzg2MCwic3ViIjoiIiwiYXVkIjoiIn0.ty2L_f4K53VSMg50yLwqFNkskM2qqUTDYHtPDdhuK2w'

# hed = {'Authorization': 'Bearer ' + auth_token}

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
    'Cookie': 'ga=GA1.3.2042638173.1650650835; _hjSessionUser_1292435=eyJpZCI6ImIwN2RjZDE0LTk4OTAtNTQxZC04NDQ1LWM4YjMxNzRmNWNiYiIsImNyZWF0ZWQiOjE2NTA2NTA4MzUwMjgsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1650650854080; _fw_crm_v=4deea7cd-78f6-4234-82a1-c5448fea63c7; _gid=GA1.3.1976918264.1651517491; PHPSESSID=dj48bubce0at50m4ng05gj24fn; _gat_UA-52493754-1=1; _gat=1; _hjAbsoluteSessionInProgress=1; _hjSession_1292435=eyJpZCI6IjY4N2MyN2RlLTIxOTQtNDgwZi1hZmM4LTZhYzJhZTc4Y2QxOCIsImNyZWF0ZWQiOjE2NTE1OTI1MzA4MjQsImluU2FtcGxlIjpmYWxzZX0=; NPS_3add8e44_throttle=1651635736943',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
}

data = {'mostrar_contato' : 'on'}
url = 'https://app.tecnofit.com.br/relatorio/statuscliente/listar'

r = requests.post(url, json=data, headers=hed)

s = """<table>
  <tr><th>Event</th><th>Start Date</th><th>End Date</th></tr>
  <tr><td>a</td><td>b</td><td>c</td></tr>
  <tr><td>d</td><td>e</td><td>f</td></tr>
  <tr><td>g</td><td>h</td><td>i</td></tr>
</table>
"""

x = """"<div class="portlet light">
<table id="tblLista" class="table table-striped table-bordered small table-hover display nowrap" style="width:100%">
  <tr><th>Event</th><th>Start Date</th><th>End Date</th></tr>
  <tr><td>a</td><td>b</td><td>c</td></tr>
  <tr><td>d</td><td>e</td><td>f</td></tr>
  <tr><td>g</td><td>h</td><td>i</td></tr>
</table>
"""

# print(r.text)
# print(r)
# print(r.json())

x.replace('<div class="portlet light">', '')

table = etree.HTML(x).find("body/table")
rows = iter(table)
headers = [col.text for col in next(rows)]

for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))
