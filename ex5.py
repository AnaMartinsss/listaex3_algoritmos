from random import randint
'''
5. Elevar números ao quadrado e ordenar (com map e sorted) 
Crie uma função que eleve ao quadrado todos os números de uma lista, utilizando 
map, e depois retorne a lista ordenada. 
Exemplo de entrada: [3, 1, 4, 2] 
Exemplo de saída: [1, 4, 9, 16] 

'''
lista_numeros = [randint(50, 200) for _ in range(10)]
quadrado = sorted(map(lambda x: x ** 2, lista_numeros))
print(quadrado)