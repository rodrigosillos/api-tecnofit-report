import pandas as pd
import json
import xlsxwriter
from includes.request_headers import set_header
from includes.request_headers_auth import set_header_auth
from includes.unidades import array_unidades

workbook = xlsxwriter.Workbook('Tecnofit_Faixa_Etaria.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Contrato')
worksheet.write('B1', 'Ticket Medio')
worksheet.write('C1', 'Unidade')

campo = 1

for unidade in array_unidades:

    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)

    data = {
        'status[]' : '1',
        'sexo' : 'A',
    }

    url = 'https://app.tecnofit.com.br/relatorio/faixaEtaria/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

    for lead in json_data['data']:
        contrato = lead[0]
        ticket_medio = lead[1]

        campo += 1

        worksheet.write('A' + str(campo), contrato)
        worksheet.write('B' + str(campo), ticket_medio)
        worksheet.write('C' + str(campo), unidade[2])

workbook.close()
