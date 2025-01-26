from random import randint
'''
2. Filtrar números pares de uma lista (com filter) 
Escreva uma função que, utilizando filter e uma função lambda, receba uma lista 
de números inteiros e retorne apenas os números pares. 
Exemplo de entrada: [1, 2, 3, 4, 5] 
Exemplo de saída: [2, 4] 

'''

lista_num = [randint(50,8000) for _ in range(50)] 
retorno = list(filter(lambda x: x % 2 == 0, lista_num))
print(retorno)
