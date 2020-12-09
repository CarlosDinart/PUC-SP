
class Pessoa:

    ano_atual = 2019    # variavel exlusiva da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod        # Comando apra chamar o metodo de classe
    def por_ano_nascimento(cls, nome, ano_nascimento):   # metodo da classe
                                                         # nao precisa utilizar o metodo self, poque
                                                         # este exclusivo ao objeto ou instancia;
                                                         # O paramentro self e substuido pelo paramentro cls
                                                         # cls - vai ter acesso a variavel que atributo da classe
     idade = cls.ano_atual - ano_nascimento
     return cls(nome, idade)                             # O return para fazer chamar a pessoa
                                                         # da classe, atituira seus objetos;





#p1 = Pessoa("Doido", 40)
#print(p1.nome, p1.idade)



p1= Pessoa.por_ano_nascimento("Doido", 1970)      # aqui criamos um factory metodo a partir da
                                                  # construcao de uma classe metodo;
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
