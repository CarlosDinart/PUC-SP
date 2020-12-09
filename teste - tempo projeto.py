from selenium import webdriver
from time import sleep

""" 1) HORARIOS DE PICOS DE FLUXO 

1.1) Case Comercial = Shopping São Paulo:

Para esta coleta fou utlizada a metrica de dados disponivel pelo google,
na ferramenta de picos de horarios de fluxo por estabelecimento,
usando como case o Shopping Sao Paulo;

site: https://www.google.com/search?q=shopping%20em%20sao%20paulo&rlz=1C1GCEU_pt-BRBR912BR912&oq=shopping+em+sao+pualo&aqs=chrome..69i57j0i13l7.21875j0j9&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=ALeKk01_vI-tg-jRwX_aNuf40njm_y2Brw:1605185807725&rflfq=1&num=10&rldimm=27017677071829166&lqi=ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw&phdesc=xjSQ_Ggt0jc&ved=2ahUKEwieuPiOh_3sAhX9IrkGHZrBCvIQvS4wAXoECBMQNQ&rlst=f#rlfi=hd:;si:7794189795737318250,l,ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw,y,v_bFKvprZrk;mv:[[-23.5058072,-46.4565457],[-23.6879732,-46.7196989]]

1.2) Metricas Observadas: E classificacões:

--- Metricas Observadas -----> Classificacões:
               
1) não é movimentado;  ----- > para nao aglomeracao
2) não muito movimentado; ---> para nao aglomeracao
3) um pouco movimentado; ----> para nao aglomeracao
4) Tão movimentado como de costume --> Para aglomeracao
5) muito movimentado; -------> Para aglomeracao
6) mais movimentado; --------> Para aglomeracao



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

    driver.get("https://www.google.com/search?q=shopping%20em%20sao%20paulo&rlz=1C1GCEU_pt-BRBR912BR912&oq=shopping+em+sao+pualo&aqs=chrome..69i57j0i13l7.21875j0j9&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=ALeKk01_vI-tg-jRwX_aNuf40njm_y2Brw:1605185807725&rflfq=1&num=10&rldimm=27017677071829166&lqi=ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw&phdesc=xjSQ_Ggt0jc&ved=2ahUKEwieuPiOh_3sAhX9IrkGHZrBCvIQvS4wAXoECBMQNQ&rlst=f#rlfi=hd:;si:7794189795737318250,l,ChVzaG9wcGluZyBlbSBzYW8gcGF1bG9aIQoIc2hvcHBpbmciFXNob3BwaW5nIGVtIHNhbyBwYXVsbw,y,v_bFKvprZrk;mv:[[-23.5058072,-46.4565457],[-23.6879732,-46.7196989]]")

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
    print(agora)
    sleep(5)# Esta funcao estabelece o tempo para ferramenta agora executar;

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


#2) FUNCAO DE LEITURA DA FERRAMENTA:

"""
2.1) definir a funcao ler: dia da semana, hora e resultado do paniel:
"""



#3) FUNCAO DE TEMPO E DIA DA SEMANA:

"""
3) definir uma funcao para apresentar uma paniel com hora, dia da semana e ALERTA DA METRICA DE ALERTA; 

"""

#4) FUNCAO DE METRICAS OBSERVADAS:


def classificacao_metricas_observadas(agora):

    """
    4.1) Dado os resultados das metricas observadas do item 1.2, e retornado na chamada de funcao
    "uso_ferramenta_fluxo_horario_real()", SERÁ ATRIBUITO e retornado OS CRITERIOS para cada resultado
    de acordo com a CLASSIFICAO DEFINIDAS no item 1.2

    Assim, se o resultado for:

    I) ENQUANTO, LER  = não ..., não muito ..., um pouco ..., deve ENTENDER COMO: Não aglomeracao,
    E RETORNARA AO USUARIO a MSG: PODER TRANSITAR TRANQUILO!!!,  BAIXA AGLOMERAÇÃO!!!

    II) SENÃO, LER, = muito... e mais..., deve ENTENDER COMO: aglomeracao,
    E RETORNARA AO USUARIO a MSG: 'ATENÇÃO MUITA AGLOMERACAO!!!, RECOMENDO AGUARDAR!!!'
    """

    if agora == "Agora: não é movimentado":
        print("PODER TRANSITAR TRANQUILO!!!, BAIXA AGLOMERAÇÃO!!!")

    if agora == "Agora:não muito movimentado":
        print("PODER TRANSITAR TRANQUILO!!!, BAIXA AGLOMERAÇÃO!!!")

    if agora == "Agora:um pouco movimentado":
        print("PODER TRANSITAR TRANQUILO!!!, BAIXA AGLOMERAÇÃO!!!")

    elif agora == "Agora: Tão movimentado como de costume":
        print('MUITA AGLOMERACAO!!!')
        print('RECOMENDO AGUARDAR!!!')

    elif agora == "Agora: muito movimentado":
        print('MUITA AGLOMERACAO!!!')
        print('RECOMENDO AGUARDAR!!!')


    elif agora == "Agora: Mais movimentado":
        print('MUITA AGLOMERACAO!!!')
        print('RECOMENDO AGUARDAR!!!')

    else:

        print('ALERTA! AGUARDE BAIXA A AGLOMERAÇÃO:)')



#5) FUNCAO DE AGLOMERACAO:

"""

5.1) definir funcao para enquanto a chamada da funcao (FUNCAO DE METRICAS OBSERVADAS),
retornar: Não aglomeracao, sera inserido e retornado o cenario com MENOR QUANTIDA E FLUXO DE FANTASMAS",
caso a chamada de funcao (FUNCAO DE METRICAS OBSERVADAS), retornar: aglomeracao
sera inserido e retornado o cenario com MAIOR QUANTIDA E FLUXO DE FANTASMAS"

"""



def main():

    #obter_driver()
    #iniciar_ferramenta_fluxo_horario()
    #uso_ferramenta_fluxo_horario_real()
    classificacao_metricas_observadas()

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