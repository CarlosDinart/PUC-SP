# 1 criar a classe
class carrinho_compra:
    def __init__(self):
        self.produtos = []          #cria uma lista vazia onde vai receber os produtos, onde todas as informcaoes
                                    # dos produtos estao agragados ao atributo (lista) produtos, e se exluir
                                    # as agregacoes a classe produto permanecera existindo;

#2. definir a agregacao:

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total



class produto:                                  # esta classe produto nao depende de nada para sua existecia
    def __init__(self, nome, valor):            # da classe carrinho de compras
        self.nome = nome
        self.valor = valor

