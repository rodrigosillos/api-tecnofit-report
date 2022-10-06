import requests

def set_header_auth(url, data):

    hed = {
        'authority': 'app.tecnofit.com.br',
        'method': 'POST',
        'path': '/util/empresa/mudarEmpresa',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '140',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.3.1012669217.1664550735; NPS_3add8e44_last_seen=1664551585731; _hjSessionUser_1292435=eyJpZCI6IjVlMTYwM2FkLTZlOWEtNTk1Yy05ZDk1LTQ2YWViZjQ5MjZkOSIsImNyZWF0ZWQiOjE2NjQ1NTA3MzUyNDksImV4aXN0aW5nIjp0cnVlfQ==; _fw_crm_v=107114ff-c99a-4b4b-8595-0db5b4b95a95; _gid=GA1.3.1200363104.1664889152; PHPSESSID=sgo2v76miafkp0j55huhal2bhv; _hjAbsoluteSessionInProgress=0; NPS_3add8e44_throttle=1665098030013; _gat_UA-52493754-1=1; _hjIncludedInSessionSample=0; _hjSession_1292435=eyJpZCI6ImQ5Mzg1MTY3LWIzZmYtNDhmYi1iYWMwLTlkMDlkNzRlNjFjYyIsImNyZWF0ZWQiOjE2NjUwNTQ4NjMyMjQsImluU2FtcGxlIjpmYWxzZX0=',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiJmY2M1Y2VlMDY2MmQ2NjVjIiwidHIiOiIxOWZmNzVjZjVhNzkwZmZkYTlmN2ViYjkwM2MzOTE2YSIsInRpIjoxNjY0ODkzNTY5NTI3fX0=',
        'origin': 'https://app.tecnofit.com.br',
        'referer': 'https://app.tecnofit.com.br/cadastro/empresa/selecionarEmpresa'
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
