import pandas as pd
import json
import xlsxwriter
from headers.request_headers import set_header
from headers.request_headers_auth import set_header_auth

array_unidades = [
    ['58D7B066A6BAD7C3F84CBF88770F5CE05E1BFC07A8ED6F6A574FD63A0D86FF32', '4003', 'Cristo'],
    ['8617597dceea7278ed31b7fda9adbc13ec068f85f4539f8c112bbd966e75f686', '4117', 'CROSSFIT TRES FIGUEIRAS'],
    ['2a86c127c068a8f82867de890129d9270a693dfe9d5211f216e05d524b2069df', '10840', 'Canoas'],
    ['f951c7049159fe39ba8eafb25dd0155a198dee12a1a7cfe909a30256ea7d826a', '11344', 'Petrópolis'],
    ['b4bfe708ecfe0c1211bafca5bc96e9b768690e5169f83cc826323b67be76f40b', '11345', 'Menino Deus'],
    ['d9ee0a7b4516ae5730e68a86ca6d6b3c0e788814991ccb0bff3aeeab028031f5', '13803', 'Santa Cruz do Sul'],
    ['8c1e2d71365777ab6527e6963f6dcdff167c726eb103639ee427f2dbdc15e691', '13883', 'BOM FIM'],
    ['37867682f37d4d7b90f52d74e21e918dbcdb73a197aa1689fbb7564750df80c0', '18726', 'Crossfit Cachoeira'],
    ['d332101203e4bec2ceeb52b0c579e4b2e885a69bddf67ebf325cc5ae40f4f1f8', '26340', 'CACHOEIRINHA'],
    ['5BE855829B6256A819FA0A5AA74091C4CEF71F0C8F40AB220106DAADE3A80DF4', '33259', 'Caxias'],
    ['07f43a2870ada97df99c667a1e7734ceb4e33c22f1ed34424e745b404d069894', '56711', 'Guaiba'],
]

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
worksheet.write('L1', 'Unidade')

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
        'data_final' : '31/07/2022',
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
        worksheet.write('L' + str(campo), unidade[2])

workbook.close()
