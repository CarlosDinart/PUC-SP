#Introducao Numeros Aleatorios - Modulo Random:

# O modulo ramdom gera numeros aleatorios: tipos:
# random.random() - Gera um numero aleatorio entre 0,1; Nao e usado quando tem um intervalo definido;
# random.choice([]) - Gera um numero aleatorio dentro de uma lista, podendo ser uma string ou numero
# random.radiante() - Gera um numeros alatorios interios, onde possui inicio e fim;  Nao e usado quamdo tenho uma lista;
# random.sample() - Gera mais de um numero aleatorio de uma lista;
# random.shuffle() - Gera um emabalharamento da sequencia de uma lista;




import random



# 1 - teste radint
s= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
for i in range(5):
    d= random.randint(0,19)
    print(d)
    c = type(d)
    print(c)
# resultado gera apenas 5 numeros aleatorios tipo inteiros sem ser definido na lista;

# 2 - teste choice

"""s= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]
for i in range(5):
    d= random.choice([s])
    print(d)
    c = type(d)
    print(c)"""

# resultado gera 5 tipo lista com a mesma quantidade da lista original, sem aleatoriadade;

