import pandas as pd
import json
import xlsxwriter
from request_headers import set_header

data = {
    'data_inicial' : '01/06/2022',
    'data_final' : '30/06/2022',
}

url = 'https://app.tecnofit.com.br/relatorio/ticketMedio/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Ticket_Medio_CRISTO4003_15062022_0050.xlsx')
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
