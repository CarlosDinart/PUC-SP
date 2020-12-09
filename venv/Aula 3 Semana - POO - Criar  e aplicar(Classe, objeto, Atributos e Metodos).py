#1.criando uma Classe
class pessoa:

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome    #Definimos os atributos da classe;
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimemto):              # variaveis da instancias
        if self.comendo:
            print(f"{self.nome} ja esta comendo.")
            return                               # impedira que execulte a funcao de baixo

        print(f"{self.nome} esta comendo {alimemto}.")
        self.comendo = True

    def para_comer(self):               # variaveis da instancias
         if not self.comendo:
            print(f"{self.nome} nao esta comendo.")
            return


         print(f"{self.nome} esta parando de comerr!!")
         self.comendo = False

    def falar(self, assunto):           # variaveis da instancias
        if self.comendo:
            print(f"{self.nome} nao pode falar comendo.")
            return

        if self.falando:
            print(f"{self.nome} ja esta falando.")
            return

        print(f"{sel.nome} esta falando!! {assunto}")
        self.falando = True
