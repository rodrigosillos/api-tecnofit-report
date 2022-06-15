import pandas as pd
import json
import xlsxwriter
from request_headers import set_header

data = {
    'data_inicial' : '01/06/2022',
    'data_final' : '30/06/2022',
}

url = 'https://app.tecnofit.com.br/relatorio/novasMatriculas/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Conversao_de_Clientes_+Convertidos_CRISTO4003_15062022_0030.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Nome')
worksheet.write('B1', 'Consultor')
worksheet.write('C1', 'Data Cadastro')
worksheet.write('D1', 'Status Atual')
worksheet.write('E1', 'Agendamentos')
worksheet.write('F1', 'Contatos')
worksheet.write('G1', 'Turmas')
worksheet.write('H1', 'Tipo Visita')

campo = 1

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
    worksheet.write('E' + str(campo), contatos)
    worksheet.write('E' + str(campo), turmas)
    worksheet.write('E' + str(campo), tipo_visita)

workbook.close()
