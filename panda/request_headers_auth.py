import requests

def set_header_auth(url, data):
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
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOTAzMjAwLCJlbXByZXNhX2lkIjoxODcyNiwiaXNzIjoiVGVjbm9maXQiLCJleHAiOjE2NTcyMjYzNTQsInN1YiI6IiIsImF1ZCI6IiJ9.WCICPHjaF76PqKspvbo-DCXshA9P2TXziLa_7JY2WQ4',
        'Cookie': '_ga=GA1.3.827632101.1650381763; PHPSESSID=0j1gr7kaftqec6lmb6n1mritrt; _gid=GA1.3.644531199.1657211722; _hjSessionUser_1292435=eyJpZCI6IjQ2OWVmYWJmLThkYjItNTNjYy1iNDZkLTliMWUyODFkZjNkMyIsImNyZWF0ZWQiOjE2NTAzODE3NjM0NDcsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; _hjSession_1292435=eyJpZCI6ImY2ZGNjMWVkLTJjNTQtNGRlZS04NzEwLWU1YTI3NDYzZmE0YSIsImNyZWF0ZWQiOjE2NTcyMTE3MjIwNzEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; NPS_3add8e44_last_seen=1657211754841; _fw_crm_v=86780c54-0d51-4ec6-9fb0-6aba33bfa3ca; NPS_3add8e44_throttle=1657255041299; _gat_UA-52493754-1=1; _gat=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
