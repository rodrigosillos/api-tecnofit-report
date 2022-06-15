import pandas as pd
import json
import xlsxwriter
from request_headers import set_header

data = {
    'data_inicial' : '01/06/2022',
    'data_final' : '30/06/2022',
    'status_pessoa_id[]' : '1'
}

url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Como_Conheceu_CRISTO4003_14062022_2347.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'ID')
worksheet.write('B1', 'Nome')
worksheet.write('C1', 'Tipo')
worksheet.write('D1', 'Data Cadastro')
worksheet.write('E1', 'Como Conheceu')

campo = 1

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

workbook.close()
