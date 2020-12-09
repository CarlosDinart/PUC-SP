# Metodos getters (PARA OBTER UM VALOR) e setters (PARA CONFIGURAR UM VALOR),
#que são métodos para controlar (validar) a entrada e saída de dados dos atributos
# dos nossos objetos.

class produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual / 100))

    # getter
    @property                # decorador chamado propriedade, e necessario antes de chamar getter
    def preco(self):         # temos que definir a funcao que desejamos alterar;
        return self._preco   #foi incluido o _ antes do atributo preco por convencao nao pode chamar
                             # nao gerara um loop estranho

    # setter
    @preco.setter                               # chama apos o @ o atributo (variavel) q dsejo configurar seguido de
                                                # do metodo setter
    def preco(self, valor):                     # definimos o outro metodo corrido (configurado), com novo parametro apos
        if isinstance(valor, str):              # o self , que sera o comando que recebera o valor a ser corrigido no
            valor = float(valor.replace("R$", ""))    # atributo que deseja configurar;

        self._preco = valor

    #Getter
    @property
    def nome(self):
        return self._nome


    #setter
    @nome.setter

    def nome(self, valor):
        if isinstance(valor, int):
            valor = str(valor)

        self._nome = valor

p1 = produto("camiseta", 50)
p1.desconto(10)
print(p1.nome ,p1.preco)

p2 = produto(10, "R$45.5")
p2.desconto(10)
print(p2.nome, p2.preco)

