import pandas as pd
import json
import xlsxwriter
from includes.request_headers import set_header
from includes.request_headers_auth import set_header_auth
from includes.unidades import array_unidades

workbook = xlsxwriter.Workbook('Tecnofit_Clientes_por_Status.xlsx')
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
worksheet.write('K1', 'Unidade')

campo = 1

for unidade in array_unidades:

    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)

    data = {
        'sexo[]' : '',
        'mostrar_contato' : 'on',
        'data_inicial' : '01/01/2015',
        'data_final' : '30/10/2025',
    }
    url = 'https://app.tecnofit.com.br/relatorio/statuscliente/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

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
        worksheet.write('K' + str(campo), unidade[2])

workbook.close()
