import requests
import json
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.bnmp
mandados_mongoDB = db.mandados

cabeçalho = {
    'Host': 'www.cnj.jus.br',
    'Connection': 'keep-alive',
    'Content-Length': '213',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'http://www.cnj.jus.br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Referer': 'http://www.cnj.jus.br/bnmp/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6'
}

import time


def faz_req(url, payload, headers):
    requests.adapters.DEFAULT_RETRIES = 100
    while True:
        try:
            p = requests.post(url, data=payload, headers=headers)
            return p.text  # return significa que vou devolver o que está depois para quem chamou// no faz_req, há 3 chamadas: pág, mandados, detalhe. pra cada um, devolvo o texto que o servidor do cnj me devolveu. nele, consigo pegar e transformar num dicionário e, sabendo os campos, pegar a info que eu quero
        except:
            print('Conexão caiu')
            time.sleep(10)


pesquisa = 'http://www.cnj.jus.br/bnmp/rest/pesquisar'
detalhes = 'http://www.cnj.jus.br/bnmp/rest/detalhar'


def bnmp(UF):
    payload_ini = '''{"criterio":{"orgaoJulgador":{"uf":"%s",
        "municipio":"","descricao":""},"orgaoJTR":{},
        "parte":{"documentos":[{"identificacao":null}]}},
        "paginador":{},"fonetica":"true","ordenacao":{"porNome":false,"porData":false}}''' % UF

    print('Baixando %s' % UF)
    resp = faz_req(pesquisa, payload_ini, cabeçalho)
    dic = json.loads(resp)
    n_paginas = dic['paginador']['totalPaginas']
    print(n_paginas)

    for k in range(1, n_paginas + 1):
        print(f'Página {k}/{n_paginas}')
        s = open('sem_permisso_%s.txt' % UF, 'a')
        payload_pag = '''{"criterio":{"orgaoJulgador":{"uf":"%s",
            "municipio":"","descricao":""},"orgaoJTR":{},
            "parte":{"documentos":[{"identificacao":null}]}},
            "paginador":{"paginaAtual":"%d"},"fonetica":"true","ordenacao":{"porNome":false,"porData":false}}''' % (
        UF, k)

        # o que vem abaixo, diz respeito à "url" no network de *detalhes*
        resp = faz_req(pesquisa, payload_pag, cabeçalho)
        if resp == None or len(resp) == 0: continue
        dic = json.loads(resp)
        mandados = dic['mandados']
        if mandados == None: continue
        cabeçalho['Content-Lenght'] = '13'
        # para o detalhamento o tamanho é só para enviar o id
        for m in mandados:
            payload_d = '{"id": %d}' % m['id']
            resp = faz_req(detalhes, payload_d, cabeçalho)
            if resp == None or len(resp) == 0: continue
            dic = json.loads(resp)
            if dic['sucesso'] == False:  # sem permissão
                print('Sem permissão', m['id'])
                s.write(str(m['id']) + '\n')
                continue  # significa "volte pro começo pra pegar o próximo"
            campos = dic['mandado']
            mandados_mongoDB.insert(dic['mandado'])
        s.close()
        # agora que pegou os detalhes, volta para o cabeçalho geral
        cabeçalho['Content-Lenght'] = '213'


ufs = '''AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI
         RJ RN RS RO RR SC SP SE TO'''.split()
ufs = '''RR SC SP SE TO'''.split()
for uf in ufs:
    bnmp(uf)