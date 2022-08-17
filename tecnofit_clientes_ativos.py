import pandas as pd
import json
import xlsxwriter
from includes.request_headers import set_header
from includes.request_headers_auth import set_header_auth
from includes.unidades import array_unidades

workbook = xlsxwriter.Workbook('Tecnofit_Clientes_Ativos.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Codigo')
worksheet.write('B1', 'Cliente')
worksheet.write('C1', 'Status Cliente')
worksheet.write('D1', 'Contrato')
worksheet.write('E1', 'Status Contrato')
worksheet.write('F1', 'Valor')
worksheet.write('G1', 'Inicio')
worksheet.write('H1', 'Vencimento')
worksheet.write('I1', 'Email')
worksheet.write('J1', 'CPF')
worksheet.write('K1', 'Contato')
worksheet.write('L1', 'Endereço')
worksheet.write('M1', 'Número')
worksheet.write('N1', 'Complemento')
worksheet.write('O1', 'Bairro')
worksheet.write('P1', 'Cidade')
worksheet.write('Q1', 'UF')
worksheet.write('R1', 'CEP')
worksheet.write('S1', 'Unidade')

campo = 1

for unidade in array_unidades:

    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)
    
    data = {
        'mostrar_contato' : 'on'
    }

    url = 'https://app.tecnofit.com.br/relatorio/clienteAtivo/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

    for lead in json_data['data']:
        codigo = lead[0]
        cliente = lead[1]
        status_cliente = lead[2]
        contrato = lead[4]
        status_contrato = lead[5]
        valor = lead[6]
        inicio = lead[7]
        vencimento = lead[8]
        email = lead[9]
        cpf = lead[10]
        contato = lead[11]
        endereco = lead[12]
        numero = lead[13]
        complemento = lead[14]
        bairro = lead[15]
        cidade = lead[16]
        uf = lead[17]
        cep = lead[18]

        campo += 1

        worksheet.write('A' + str(campo), codigo)
        worksheet.write('B' + str(campo), cliente)
        worksheet.write('C' + str(campo), status_cliente)
        worksheet.write('D' + str(campo), contrato)
        worksheet.write('E' + str(campo), status_contrato)
        worksheet.write('F' + str(campo), valor)
        worksheet.write('G' + str(campo), inicio)
        worksheet.write('H' + str(campo), vencimento)
        worksheet.write('I' + str(campo), email)
        worksheet.write('J' + str(campo), cpf)
        worksheet.write('K' + str(campo), contato)
        worksheet.write('L' + str(campo), endereco)
        worksheet.write('M' + str(campo), numero)
        worksheet.write('N' + str(campo), complemento)
        worksheet.write('O' + str(campo), bairro)
        worksheet.write('P' + str(campo), cidade)                   
        worksheet.write('Q' + str(campo), uf)
        worksheet.write('R' + str(campo), cep)
        worksheet.write('S' + str(campo), unidade[2])

workbook.close()
