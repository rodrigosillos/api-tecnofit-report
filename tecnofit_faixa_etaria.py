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

workbook = xlsxwriter.Workbook('Tecnofit_Faixa_Etaria.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Contrato')
worksheet.write('B1', 'Ticket Medio')
worksheet.write('C1', 'Unidade')

campo = 1

for unidade in array_unidades:

    data_auth = {
        "token": unidade[0],
        "goto": "https://api.tecnofit.com.br/ng/dashboard"
    }

    url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

    set_header_auth(url_auth, data_auth)

    data = {
        'status[]' : '1',
        'sexo' : 'A',
    }

    url = 'https://app.tecnofit.com.br/relatorio/faixaEtaria/listar'

    table_MN = pd.read_html(set_header(url, data).text)
    json_data = json.loads(table_MN[0].to_json(orient="split"))

    for lead in json_data['data']:
        contrato = lead[0]
        ticket_medio = lead[1]

        campo += 1

        worksheet.write('A' + str(campo), contrato)
        worksheet.write('B' + str(campo), ticket_medio)
        worksheet.write('C' + str(campo), unidade[2])

workbook.close()
