import requests

def set_header_auth(url, data):

    hed = {
        'authority': 'app.tecnofit.com.br',
        'method': 'POST',
        'path': '/util/empresa/mudarEmpresa',
        'scheme': 'https',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '140',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.3.1012669217.1664550735; _gid=GA1.3.928097642.1664550735; _hjFirstSeen=1; _hjSession_1292435=eyJpZCI6ImYzNTI1NGM5LWUwM2QtNDBjZi05OWI1LTAyMDI4NjMwNDEzZiIsImNyZWF0ZWQiOjE2NjQ1NTA3MzYwMzUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; NPS_3add8e44_last_seen=1664551585731; NPS_3add8e44_throttle=1664594786162; _hjSessionUser_1292435=eyJpZCI6IjVlMTYwM2FkLTZlOWEtNTk1Yy05ZDk1LTQ2YWViZjQ5MjZkOSIsImNyZWF0ZWQiOjE2NjQ1NTA3MzUyNDksImV4aXN0aW5nIjp0cnVlfQ==; _fw_crm_v=107114ff-c99a-4b4b-8595-0db5b4b95a95; _hjIncludedInSessionSample=0; PHPSESSID=o68kdud9tkgl4na91aflsa59jl; _gat=1; _gat_UA-52493754-1=1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiJkZjllZWNkM2U0YzhhMDM5IiwidHIiOiJhZmFiNGJkNDgyZDhmODNjOWE2MTYwMDg1MGM5NGRmNSIsInRpIjoxNjYwNjc3OTEyMzM5fX0=',
        'origin': 'https://app.tecnofit.com.br',
        'referer': 'https://app.tecnofit.com.br/cadastro/empresa/selecionarEmpresa'
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
