import pandas as pd
import json
from request_headers import set_header

url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'

data = {
    'data_inicial' : '01/06/2022',
    'data_final' : '30/06/2022',
    'status_pessoa_id[]' : '1'
}

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

for lead in json_data['data']:
    id = lead[0]
    nome = lead[1]
    tipo = lead[2]
    data_cadastro = lead[3]
    como_conheceu = lead[4]

    print (nome)
