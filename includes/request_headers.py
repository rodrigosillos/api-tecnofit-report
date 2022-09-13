import requests

def set_header(url, data):

    hed = {
        'authority': 'app.tecnofit.com.br',
        'method': 'POST',
        'path': '/relatorio/clienteAtivo/listar',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '18',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.3.827632101.1650381763; _hjSessionUser_1292435=eyJpZCI6IjQ2OWVmYWJmLThkYjItNTNjYy1iNDZkLTliMWUyODFkZjNkMyIsImNyZWF0ZWQiOjE2NTAzODE3NjM0NDcsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1657211754841; _fw_crm_v=86780c54-0d51-4ec6-9fb0-6aba33bfa3ca; _gid=GA1.3.1823908122.1663109767; _hjIncludedInSessionSample=0; _hjSession_1292435=eyJpZCI6IjliOGY3YjMxLTQ2NjctNDJjOS1hYWFjLTJiMWEwNjI2MDc3MyIsImNyZWF0ZWQiOjE2NjMxMDk3Njg1NjcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; PHPSESSID=ic0ade3m21ula5o21fajch3tjs; _gat=1; _gat_UA-52493754-1=1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiJhZjIwZTg2NDEzZTU3MTlmIiwidHIiOiI0ZDc1MDUyMjU3YjM3ZTA0ODdkYjYyODZjMWU0NzVlNyIsInRpIjoxNjYwMzE5Nzg2MTI1fX0=',
        'origin': 'https://app.tecnofit.com.br',
        'referer': 'https://app.tecnofit.com.br/relatorio/clienteAtivo'
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
