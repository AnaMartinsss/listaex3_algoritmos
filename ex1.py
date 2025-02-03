from random import randint
'''
1. Dobrar elementos de uma lista (com map) 
Escreva uma função que, utilizando map e uma função lambda, receba uma lista 
de números inteiros e retorne uma nova lista com todos os elementos dobrados. 
Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8] 

'''

'''
lista_numeros = [randint(50,8000) for _ in range(50)]
resultado = list(map(lambda x: x * 2, lista_numeros ))
print(lista_numeros)
print(resultado)
'''

lista = [randint(50,8000) for _ in range(50)]

def dobrar_elementos(lista : list[int])-> list[int]:
        return list(map(lambda x: x * 2,lista)) 

resultado = dobrar_elementos(lista)
print(resultado)