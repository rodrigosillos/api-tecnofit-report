import requests

def set_header(url, data):

    hed = {
        'authority': 'app.tecnofit.com.br',
        'method': 'POST',
        'path': '/relatorio/clienteAtivo/listar',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '88',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.3.1012669217.1664550735; NPS_3add8e44_last_seen=1664551585731; _hjSessionUser_1292435=eyJpZCI6IjVlMTYwM2FkLTZlOWEtNTk1Yy05ZDk1LTQ2YWViZjQ5MjZkOSIsImNyZWF0ZWQiOjE2NjQ1NTA3MzUyNDksImV4aXN0aW5nIjp0cnVlfQ==; _fw_crm_v=107114ff-c99a-4b4b-8595-0db5b4b95a95; _gid=GA1.3.1200363104.1664889152; NPS_3add8e44_throttle=1664932484012; PHPSESSID=n8o9fqg777nqq75n8dj2dcic7f',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiIzMmU0OTVjYTY1YmFiYmEwIiwidHIiOiJhM2QyYTM0Y2NmMWM3YmE4ZDVlY2U5ZmQ5OGRlYWRlOSIsInRpIjoxNjY0ODkyOTg4NTI4fX0=',
        'origin': 'https://app.tecnofit.com.br',
        'referer': 'https://app.tecnofit.com.br/relatorio/clienteAtivo'
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
