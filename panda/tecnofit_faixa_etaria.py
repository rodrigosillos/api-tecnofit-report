import pandas as pd
import json
import xlsxwriter
from request_headers import set_header

data = {
    'status[]' : '1',
    'sexo' : 'A',
}

url = 'https://app.tecnofit.com.br/relatorio/faixaEtaria/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Faixa_Etaria_CRISTO4003_15062022_0057.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Contrato')
worksheet.write('B1', 'Ticket Medio')

campo = 1

for lead in json_data['data']:
    contrato = lead[0]
    ticket_medio = lead[1]

    campo += 1

    worksheet.write('A' + str(campo), contrato)
    worksheet.write('B' + str(campo), ticket_medio)

workbook.close()
