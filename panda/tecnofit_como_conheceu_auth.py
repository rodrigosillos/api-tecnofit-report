import pandas as pd
import json
import xlsxwriter
from request_headers import set_header
from request_headers_auth import set_header_auth

# SuperForce Cristo 4003 58D7B066A6BAD7C3F84CBF88770F5CE05E1BFC07A8ED6F6A574FD63A0D86FF32
# SUPERFORCE CROSSFIT TRES FIGUEIRAS 4117 8617597dceea7278ed31b7fda9adbc13ec068f85f4539f8c112bbd966e75f686
# Superforce Canoas 10840 2a86c127c068a8f82867de890129d9270a693dfe9d5211f216e05d524b2069df
# SuperForce Petrópolis 11344 f951c7049159fe39ba8eafb25dd0155a198dee12a1a7cfe909a30256ea7d826a
# SuperForce Menino Deus 11345 b4bfe708ecfe0c1211bafca5bc96e9b768690e5169f83cc826323b67be76f40b
# SFRC Santa Cruz do Sul 13803 d9ee0a7b4516ae5730e68a86ca6d6b3c0e788814991ccb0bff3aeeab028031f5
# SFRC - BOM FIM 13883 8c1e2d71365777ab6527e6963f6dcdff167c726eb103639ee427f2dbdc15e691
# Superforce Crossfit Cachoeira 18726 37867682f37d4d7b90f52d74e21e918dbcdb73a197aa1689fbb7564750df80c0
# SRFC CACHOEIRINHA 26340 d332101203e4bec2ceeb52b0c579e4b2e885a69bddf67ebf325cc5ae40f4f1f8
# SuperForce Caxias 33259 5BE855829B6256A819FA0A5AA74091C4CEF71F0C8F40AB220106DAADE3A80DF4
# SuperForce Guaiba 56711 07f43a2870ada97df99c667a1e7734ceb4e33c22f1ed34424e745b404d069894

data_auth = {"token":"2a86c127c068a8f82867de890129d9270a693dfe9d5211f216e05d524b2069df","goto":"https://api.tecnofit.com.br/ng/dashboard"}
url_auth = 'https://app.tecnofit.com.br/util/empresa/mudarEmpresa'

set_header_auth(url_auth, data_auth)

data = {
    'data_inicial' : '01/07/2022',
    'data_final' : '31/07/2022',
    'status_pessoa_id[]' : '1'
}

url = 'https://app.tecnofit.com.br/relatorio/comoConheceu/listar'

table_MN = pd.read_html(set_header(url, data).text)
json_data = json.loads(table_MN[0].to_json(orient="split"))

workbook = xlsxwriter.Workbook('Tecnofit_Como_Conheceu_10840.xlsx')
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
