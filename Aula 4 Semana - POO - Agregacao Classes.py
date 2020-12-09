from classes import carrinho_compra, produto


carrinho = carrinho_compra()
p1 = produto("camisinha", 50)
p2 = produto("aifone", 10000)
p3 = produto("caneca", 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)

carrinho.lista_produtos()
print(carrinho.soma_total())