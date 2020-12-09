from selenium import webdriver
from time import sleep
#from datetime import date


""" 1) HORARIOS DE PICOS DE FLUXO 

1.1) Case Comercial = Shopping Iguatemi São Paulo:

Para esta coleta fou utlizada a metrica de dados disponivel pelo google,
na ferramenta de picos de horarios de fluxo por estabelecimento,
usando como case o Shopping Iguatemi São Paulo;

site: https://www.google.com/search?q=shopping%20em%20sao%20paulo&rlz=1C1GCEU_pt-BRBR912BR912&oq=shopping+em+sao+pualo&aqs=chrome..69i57j0i13l7.21875j0j9&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=ALeKk01_vI-tg-jRwX_aNuf40njm_y2Brw:1605185807725&rflfq=1&num=10&rldimm=27017677071829166&lqi=ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw&phdesc=xjSQ_Ggt0jc&ved=2ahUKEwieuPiOh_3sAhX9IrkGHZrBCvIQvS4wAXoECBMQNQ&rlst=f#rlfi=hd:;si:7794189795737318250,l,ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw,y,v_bFKvprZrk;mv:[[-23.5058072,-46.4565457],[-23.6879732,-46.7196989]]

1.2) Metricas Observadas: Fluxo de Contagem de Pessoas

O case comercial, possuir uma area 93 mil m², com fluxo de pessoas 85 mil pessoas por dia;
fonte: https://diariodonordeste.verdesmares.com.br/negocios/iguatemi-projeta-faturar-r-1-3-bilhao-em-um-ano-1.1258351


1.2.1) Metricas Observadas: PICOS DOS HORARIOS, E classificacões:

--- Metricas Observadas -----------------> Classificacões  ------------> Indice de Ocupaçao:

1) Geralmente não é movimentado  ------- > para não aglomeracao -------> [ > 0% , 15 %]
2) Normalmente não muito movimentado ----> para não aglomeracao -------> [ > 15% , 35 %]
3) Não muito movimentado ----------------> para não aglomeracao -------> [ > 15% , 35 %]
4) Um pouco movimentado; ----------------> para média aglomeracao -----> [ > 35% , 65 %]
5) Geralmente um pouco movimentado ------> para média aglomeracao -----> [ > 35% , 65 %]
6) Tão movimentado como de costume ------> Para intensa aglomeracao ---> [ > 65% [
7) muito movimentado; -------------------> Para intensa aglomeracao ---> [ > 65% [
8) mais movimentado; --------------------> Para intensa aglomeracao ---> [ > 65% [



1.2.2) Metricas Observadas: INDICES DE OCUPACAO E FLUXOS DE CONTAGEM DE PESSOAS COM QUANTIDADES:

Aplicando oponto medio para cada inidice de opupacao do intervalo do resultado, aoplincando a distribuicao proporcional
para cada amostra de acordo com o ponto medio da da frequencia diaria de fluxo, teremos como resultado a estimativa 
media por diario de fluxo de pessoas por dia considerados a distribuicao de acordo com os picos de horarios;

Indice de Ocupaçao:  -------------------> FLUXOS DE CONTAGEM DE PESSOAS -----------> Qt. Fantasmas
                                          E PICOS DE HORARIOS                        Qt x potencia
 
1) [ > 0% , 15 %] ----------------------> 10.000 ----------------------------------> 10 (.10(4))
2) [ > 15% , 35 %] ---------------------> 30.000 ----------------------------------> 30 (.10(4)) *
3) [ > 35% , 65 %] ---------------------> 60.000 ----------------------------------> 60 (.10(4)) *
4) [ > 65% [ ---------------------------> 80.000 ----------------------------------> 80 (.10(4)) *




       2) DEFINIR AS INSTRUCOES"""


# 2) FUNCAO DE ACESSO  E USO DA FERRAMENTA - PICO DE HORARIO:


# 2.1) definir uma funcao para acessar a ferramenta de horario de pico de horario

def obter_driver():

    """" Foi utilizado para navegador o Chrome Veresao 86, e seus respectivo Driver instalado no python,
     criado o driver como biblioteca e salvo na pasta "Chrome Driver" e classe ("chromedriver.exe")

     """

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    return driver


def iniciar_ferramenta_fluxo_horario(driver):
    """" Dado a integracao com site do case comercial, a chamada de funcao (iniciar_ferramenta_fluxo_horario)
    iniciar a interacao com o estabelecimento comercial e retornar acessao ao web site do case;

    """
    # Foi utilizado o metodo get da biblioteca selenio:

    #driver.get("https://www.google.com/search?q=shopping%20em%20sao%20paulo&rlz=1C1GCEU_pt-BRBR912BR912&oq=shopping+em+sao+pualo&aqs=chrome..69i57j0i13l7.21875j0j9&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=ALeKk01_vI-tg-jRwX_aNuf40njm_y2Brw:1605185807725&rflfq=1&num=10&rldimm=27017677071829166&lqi=ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw&phdesc=xjSQ_Ggt0jc&ved=2ahUKEwieuPiOh_3sAhX9IrkGHZrBCvIQvS4wAXoECBMQNQ&rlst=f#rlfi=hd:;si:7794189795737318250,l,ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw,y,v_bFKvprZrk;mv:[[-23.5058072,-46.4565457],[-23.6879732,-46.7196989]]")
    driver.get("https://www.google.com/search?rlz=1C1GCEU_pt-BRBR912BR912&sxsrf=ALeKk01IjtydkA-vB_mCNePTR5woQlm3jA%3A1606856203153&ei=C67GX67iCNfE5OUPjeqEiAk&q=shopping+iguatemi+sao+paulo&oq=s&gs_lcp=CgZwc3ktYWIQARgAMgQIIxAnMgQIIxAnMgQIIxAnMgQIABBDMgUIABCxAzIICC4QsQMQgwEyBAgAEEMyCAguELEDEIMBMgUIABCxAzIICC4QsQMQgwE6BwgjEOoCECc6BwgAELEDEEM6AggAUO0uWLpEYOVQaANwAHgEgAGMAogBgw-SAQMyLTiYAQCgAQGgAQKqAQdnd3Mtd2l6sAEKwAEB&sclient=psy-ab")
    driver.implicitly_wait(20)

def uso_ferramenta_fluxo_horario_real(driver):
    """"
    Chamnando a função (uso_ferramenta_fluxo_horario_real), retornar a leitura do fluxo de movimento atual e real
    do case comercial classificando de acordo com as metricas observada no item 1.2

    """
    # METODO DE LOCALIZACAO POR CLASSE DA BIBLIOTECA SELENIUN - https://selenium-python.readthedocs.io/locating-elements.html
    # Para agora foi utizado o metodo de localizacao por classe atraves "dafind_element_by_class_name().text"
    # onde INDENTIFICANDO PELO INSPENCAO A TAG DA CLASSE "ujewvc" -
    # do monitoramento do tempo real e agora do case comercial;


    agora = driver.find_element_by_class_name("ujewvc").text
    sleep(5)  # Esta funcao estabelece o tempo para ferramenta agora executar;
    print(agora)

    return agora

    # METODO DE LOCALIZACAO POR ID:
    # sit2 = driver.find_element_by_xpath("//*[@id=akp_tsuid10]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[11]/c-wiz/div/div[2]/div[2]/div/div[1]/div")


def finalizar_ferramenta_fluxo_horario_real(driver):

    # Esta funcao finaliza o uso da ferramenta da chamanda de funcao (uso_ferramenta_fluxo_horario_real);
    driver.quit()


"""def monitorando_uso_ferramenta_fluxo_horario_real(agora):

    Esta chamada de funcao monitora monitora em tempo real os resultados da chamada (uso_ferramenta_fluxo_horario_real)
    atualizando a cada 5 segundos...  



    for agora in range(10, 0, -1):
        sleep(5)
        print(agora)

    """

# 2) FUNCAO DE LEITURA DA FERRAMENTA:

"""
2.1) definir a funcao ler: dia da semana, hora e resultado do paniel:

Metodo da data e dia atual:

hj = date.today() # retornar data, mes e ano;
ano = hj.year
mes = hj.month
date = hj.day
data = date(ano, month, date)
print(data)
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
dia = hj.weekday() # retornar dia da semana;
print(dia)

Metodo da hora atual:

hora_atuais = datetime.now()
print(hora_atuais)

data_e_hora_em_texto = ‘01/03/2018 12:30’
data_e_hora = datetime.strptime(data_em_texto, ‘%d/%m/%Y %H:%M’)


"""

# 3) FUNCAO DE TEMPO E DIA DA SEMANA:

"""
3) definir uma funcao para apresentar uma paniel com hora, dia da semana e ALERTA DA METRICA DE ALERTA; 




"""


# 4) FUNCAO DE METRICAS OBSERVADAS:


def classificacao_metricas_observadas(agora):
    """
    4.1) Dado os resultados das metricas observadas do item 1.2, e retornado na chamada de funcao
    "uso_ferramenta_fluxo_horario_real()", SERÁ ATRIBUITO e retornado OS CRITERIOS para cada resultado
    de acordo com a CLASSIFICAO DEFINIDAS no item 1.2

    Assim, se o resultado for:

    I) ENQUANTO OU SE LER  = não ..., não muito ..., um pouco ..., deve ENTENDER COMO: Não aglomeracao,
    E RETORNARA AO USUARIO a MSG: PODER TRANSITAR TRANQUILO!!!,  BAIXA AGLOMERAÇÃO!!!

    II) SENÃO, LER, = muito... e mais..., deve ENTENDER COMO: aglomeracao,
    E RETORNARA AO USUARIO a MSG: 'ATENÇÃO MUITA AGLOMERACAO!!!, RECOMENDO AGUARDAR!!!'
    """

    if agora == "Agora: não é movimentado":
        agora = "Nivel de aglomeração baixo"
        print(agora)
        return agora

    if agora == "Agora: Não muito movimentado":
        agora = "Nivel de aglomeração baixo"
        print(agora)
        return agora

    if agora == "Agora: Um pouco movimentado":
        agora = "Nivel de algomeração medio"
        print(agora)
        return agora

    elif agora == "Agora: Tão movimentado como de costume":
        agora = "Nivel de algomeração alto"
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return agora

    elif agora == "Agora: muito movimentado":
        agora = "Nivel de aglomeração alto"
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return agora


    elif agora == "Agora: Mais movimentado":
        agora = "Nivel de aglomeração alto"
        print(agora)
        print('RECOMENDO AGUARDAR!!!')
        return agora

    else:
        print('ALERTA! AGUARDE BAIXA A AGLOMERAÇÃO:)')



# 5) FUNCAO DE AGLOMERACAO:

"""

5.1) definir funcao para enquanto a chamada da funcao (FUNCAO DE METRICAS OBSERVADAS),
retornar: Não aglomeracao, sera inserido e retornado o cenario com MENOR QUANTIDA E FLUXO DE FANTASMAS",
caso a chamada de funcao (FUNCAO DE METRICAS OBSERVADAS), retornar: aglomeracao
sera inserido e retornado o cenario com MAIOR QUANTIDA E FLUXO DE FANTASMAS"

"""


def main():

    driver = obter_driver()
    iniciar_ferramenta_fluxo_horario(driver)
    agora = uso_ferramenta_fluxo_horario_real(driver)
    classificacao_metricas_observadas(agora)


main()

"""
[ 1 ] para nao aglomeracao
[ 2 ] Para aglomeracao (não recomendado)''')
opção = int(input('Digite a opção: '))
if opção == 1:
    for c in range(10, 0, -1):
        sleep(1)
        print(c)
    print('PODER TRANSITAR TRANQUILO!!!')
    print('SEM AGLOMERAÇÃO!!!')
elif opção == 2:
    sleep(1)
    print('MUITA AGLOMERACAO!!!')
    print('RECOMENDO AGUARDAR!!!')

else:
    print('ALERTA! SHOPPING COM BAIXA AGLOMERAÇÃO:)')

"""