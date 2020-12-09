from  random import randint


class Pessoa:

    ano_atual = 2019    # variavel exlusiva da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
     idade = cls.ano_atual - ano_nascimento
     return cls(nome, idade)


    @staticmethod                       #staticmethod -para utlizar nao preciso da instancia (self)
    def gera_id():                      # e nem da classe (cls), porem tem ser inserido dentro da classe;
        rand = randint(10000, 19999)    # Funciona como funcao normal;
        return rand                     # ()- dentro dos parentes podera receber paramentos se quiser
                                        # nome, idade e etc;
                                        # Podemos criar variaveis dentro do metodo e so servira para ela;
                                        


p1= Pessoa("DOIDO", 49)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())                        # o metodo estatico pode ser chamado pela classe;
print(p1.gera_id())                            # ou pela instancia (objeto)
