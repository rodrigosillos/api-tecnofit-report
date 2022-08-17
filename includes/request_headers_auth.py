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
        'cookie': '_ga=GA1.3.827632101.1650381763; _hjSessionUser_1292435=eyJpZCI6IjQ2OWVmYWJmLThkYjItNTNjYy1iNDZkLTliMWUyODFkZjNkMyIsImNyZWF0ZWQiOjE2NTAzODE3NjM0NDcsImV4aXN0aW5nIjp0cnVlfQ==; NPS_3add8e44_last_seen=1657211754841; _fw_crm_v=86780c54-0d51-4ec6-9fb0-6aba33bfa3ca; AWSALB=3H6V3/GsSL/fTf8P1hx0GDiC4wfc86DmdOBbnUHNdBU/qG1lgpzIkmTnbt0LuGbrfcqns8bhJhjyoq15RszIw9EM9j9RYgriJZLQL7FHE15eHo0wlWza5b+FHWGl; AWSALBCORS=3H6V3/GsSL/fTf8P1hx0GDiC4wfc86DmdOBbnUHNdBU/qG1lgpzIkmTnbt0LuGbrfcqns8bhJhjyoq15RszIw9EM9j9RYgriJZLQL7FHE15eHo0wlWza5b+FHWGl; _gid=GA1.3.535785240.1660677756; PHPSESSID=b8rrqg7ftdvapag74ovs5k1efa; _hjIncludedInSessionSample=0; _hjSession_1292435=eyJpZCI6ImYwNGJhZDZlLTYxZjAtNDJlOC04MDI5LThlMzc0Y2EyNDBiNyIsImNyZWF0ZWQiOjE2NjA3NDM2NzQ4NzMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; NPS_3add8e44_throttle=1660786880500; _gat=1; _gat_UA-52493754-1=1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6Ijg2NDMzNyIsImFwIjoiNDMxNDg2MjM2IiwiaWQiOiJkZjllZWNkM2U0YzhhMDM5IiwidHIiOiJhZmFiNGJkNDgyZDhmODNjOWE2MTYwMDg1MGM5NGRmNSIsInRpIjoxNjYwNjc3OTEyMzM5fX0=',
        'origin': 'https://app.tecnofit.com.br',
        'referer': 'https://app.tecnofit.com.br/cadastro/empresa/selecionarEmpresa'
    }

    resultado = requests.post(url, json=data, headers=hed)

    return resultado
