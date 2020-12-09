# Encapsulamento - objetivo e esconder parte do seu codigo para proteger acesso do seu codigo

#metodos: public, protected (_ ANTES DO ATRIBUTO OU METODOS),
# private (__ ANTES DO ATRIBUTO OU METODOS);

# Estes metodos nao foram aderido pela linguagem python, para utliza los foi criados metodos de
# convencoes determnando o seguinte: SE O ATRIBUTO OU METODOS QUE ESTIVER UTILIZANDO ESTIVER UM _ ANTES DELE
# RECOMENDA SE QUE VC NAO ACESSA ESTE ATRIBUTO;



# 1 Passo criar um docionario num banco de dados;

class Banco_de_Dados:

    def __init__(self):
        self.__dados = {}   #dicionario vazio e onde recebe todas as informacoes dos dados;

    def inserir_clientes(self, id, nome):  #esta funcao vai incluir os dados no dicionario vazio;
        if "clientes" not in self.__dados:   # conferir se o cliente nao esta no dicionario
            self.__dados ["clientes"] = {id: nome}              # vai incluir cliente no dicionario

        else:
            self.__dados["clientes"].update({id: nome})   # se exixtir o cliente o dicionario vai ser atualizado


    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados["clientes"] [id]




bd = Banco_de_Dados()  # este dados estao publicos para classe todas e fora dela;
bd.inserir_clientes(1, "puta")
bd.inserir_clientes(2, "doido")
bd.inserir_clientes(3, "cheira po")
bd.inserir_clientes(4, "Gostosa")
bd.__dados = "um outra coisa"   # defini a mudanca da classe assim para de fuincionar;
bd.lista_clientes()

