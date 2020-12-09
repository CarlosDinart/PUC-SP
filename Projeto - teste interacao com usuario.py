import datetime
from datetime import date

"""
I - METRICAS E CONSIDERACOES INCIAIS:

Considerando, que o case comercial definido foi "Shopping Sao Paulo", dado o seu horario
de funcionamento estara disponivel para usuario  nos dias da semana, e
aberto ao publico no horario comercial a seguir:

Dia da semana -------> Horário:
segunda-feira -------> 10:00–22:00
terça-feira	---------> 10:00–22:00
quarta-feira --------> 10:00–22:00
quinta-feira --------> 10:00–22:00
sexta-feira ---------> 10:00–22:00
sábado --------------> 10:00–22:00
domingo -------------> 14:00–20:00

A ferramenta "INTERACAO COM USUARIO" tem como objetivo que o programa receba dados do usuarios
recebendo seu feed de quais dias e horarios q deseja frequentar o case comercial e retornar
se o estabeleciemnto possui quais niveis de aglomeracao;

"""

# 1)  FERRAMENTA INRACAO COM USUARIO;

# 1.1) Função entrada de dados do usuario;

""" Esta un funcao ela recebe os dados do usuario do dias e horas deseja
frequentar o estabeleciemnto comercial"""




#hj = date.today() # retornar data, mes e ano atual;
#print(hj)
#print(hj.toordinal())

#futuro = date.fromordinal(hj.toordinal()+45) # hoje + 45 dias # retornar data, mes e ano futuro;
#print(futuro)

#dia = hj.weekday() # retornar Ele retornará um número inteiro entre 0 (represendo segunda-feira)
#print(dia)         # e 6 (representando domingo).



#hj = date.today()
#dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
#print("Hoje é", dias[hj.weekday()]) # retornar o dia da semnana atual atraves do id;


#a = dias[hj.weekday()]
#print(a)


"""
#dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
#dia = input("Digite um dia da semana:")
#print(dia in dias)

"""
def interacao_dia():


    """Dada o dia e a hora inserida pelo usuario, a chamada da funcão" interacao_dia", retornar
    o dia da semana desejado pelo usuario";"""

    

    hj = date.today()
    ano = hj.year
    mes = hj.month
    day = int(input("Digite uma data da visita: "))
    data = date(ano, mes, day)
    print(data)

    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    indice_da_semana = data.weekday()
    print(indice_da_semana)

    dia_da_semana = dias[indice_da_semana]
    print(dia_da_semana)

    numero_do_dia_da_semana = data.isoweekday()
    print(numero_do_dia_da_semana)


def interacao_hora():





def interacao_hora_alerta():

    hora_atual = datetime.now()

    hr_usuario = input("Digite Hora da Visita (hh:mm): ")
    hora = int(hr_usuario.split(':')[0])
    minuto = int(hr_usuario.split(':')[1])

    if hora_atual.hour == hora and hora_atual.minute == minuto:
        if hr_usuario == "BAIXA ALGOMERACAO" # INSERIR FUNCAO
            print("ALERTA!!! BAIXA AGLOMERACAO)
    # return True
    # return False

    #https://academiahopper.com.br/como-trabalhar-com-data-e-hora-em-python/



    print(hora, minuto)

    return hr_usuario










"""
hora_atuais = datetime.now()
print(hora_atuais)

"""
def main():

    interacao_dia()
    interacao_hora()

main()
