import pandas as pd
import json
import xlsxwriter
from includes.request_headers import set_header
from includes.request_headers_auth import set_header_auth
from includes.unidades import array_unidades

workbook = xlsxwriter.Workbook('Tecnofit_Conversao_de_Clientes.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Nome')
worksheet.write('B1', 'Consultor')
worksheet.write('C1', 'Data Cadastro')
worksheet.write('D1', 'Status Atual')
worksheet.write('E1', 'Agendamentos')
worksheet.write('F1', 'Contatos')
worksheet.write('G1', 'Turmas')
worksheet.write('H1', 'Tipo Visita')
worksheet.write('I1', 'Unidade')

campo = 1

for unidade in array_unidades:

    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)

    data = {
        'data_inicial' : '01/01/2015',
        'data_final' : '31/10/2025',
    }

    url = 'https://app.tecnofit.com.br/relatorio/novasMatriculas/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

    for lead in json_data['data']:
        nome = lead[0]
        consultor = lead[1]
        data_cadastro = lead[2]
        status_atual = lead[3]
        agendamentos = lead[4]
        contatos = lead[5]
        turmas = lead[6]
        tipo_visita = lead[7]

        campo += 1

        worksheet.write('A' + str(campo), nome)
        worksheet.write('B' + str(campo), consultor)
        worksheet.write('C' + str(campo), data_cadastro)
        worksheet.write('D' + str(campo), status_atual)
        worksheet.write('E' + str(campo), agendamentos)
        worksheet.write('F' + str(campo), contatos)
        worksheet.write('G' + str(campo), turmas)
        worksheet.write('H' + str(campo), tipo_visita)
        worksheet.write('I' + str(campo), unidade[2])

workbook.close()
