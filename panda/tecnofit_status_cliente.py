import pandas as pd
import json
import xlsxwriter
from request_headers import set_header

data = {'mostrar_contato' : 'on'}
url = 'https://app.tecnofit.com.br/relatorio/statuscliente/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Clientes_por_Status_CRISTO4003_14062022_2226.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Codigo')
worksheet.write('B1', 'Cliente')
worksheet.write('C1', 'Nascimento')
worksheet.write('D1', 'Sexo')
worksheet.write('E1', 'Consultor')
worksheet.write('F1', 'Professor')
worksheet.write('G1', 'Último Status')
worksheet.write('H1', 'Status Cliente')
worksheet.write('I1', 'E-mail')
worksheet.write('J1', 'Contato')

campo = 1

for lead in json_data['data']:
    codigo = lead[1]
    cliente = lead[2]
    nascimento = lead[3]
    sexo = lead[4]
    consultor = lead[5]
    professor = lead[6]
    ultimo_status = lead[7]
    status_cliente = lead[8]
    email = lead[9]
    contato = lead[10]

    campo += 1

    worksheet.write('A' + str(campo), codigo)
    worksheet.write('B' + str(campo), cliente)
    worksheet.write('C' + str(campo), nascimento)
    worksheet.write('D' + str(campo), sexo)
    worksheet.write('E' + str(campo), consultor)
    worksheet.write('F' + str(campo), professor)
    worksheet.write('G' + str(campo), ultimo_status)
    worksheet.write('H' + str(campo), status_cliente)
    worksheet.write('I' + str(campo), email)
    worksheet.write('J' + str(campo), contato)

workbook.close()
