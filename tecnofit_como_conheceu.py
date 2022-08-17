import pandas as pd
import json
import xlsxwriter
from includes.request_headers import set_header
from includes.request_headers_auth import set_header_auth
from includes.unidades import array_unidades

workbook = xlsxwriter.Workbook('Tecnofit_Como_Conheceu.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'ID')
worksheet.write('B1', 'Nome')
worksheet.write('C1', 'Tipo')
worksheet.write('D1', 'Data Cadastro')
worksheet.write('E1', 'Como Conheceu')
worksheet.write('F1', 'Unidade')

campo = 1

for unidade in array_unidades:
    
    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)

    # data = {
    #     'data_inicial': '01/07/2022',
    #     'data_final': '31/07/2022',
    #     'tipo_pessoa_id[]': '3',
    #     'como_conheceu_id[]': '20370',
    #     'status_pessoa_id[]	': '1',
    #     'grafico': '1',
    # }

    data = {
        'data_inicial': '01/08/2022',
        'data_final': '31/08/2022',
        'status_pessoa_id[]': '1'
    }

    url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

    for lead in json_data['data']:
        id = lead[0]
        nome = lead[1]
        tipo = lead[2]
        data_cadastro = lead[3]
        como_conheceu = lead[4]

        campo += 1

        worksheet.write('A' + str(campo), id)
        worksheet.write('B' + str(campo), nome)
        worksheet.write('C' + str(campo), tipo)
        worksheet.write('D' + str(campo), data_cadastro)
        worksheet.write('E' + str(campo), como_conheceu)
        worksheet.write('F' + str(campo), unidade[2])

workbook.close()
