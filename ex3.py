from random import randint
from functools import reduce
'''
3. Somar os números de uma lista (com reduce) 
Crie uma função que, utilizando reduce e uma função lambda, receba uma lista de 
números inteiros e retorne a soma total dos números. 
Exemplo de entrada: [1, 2, 3, 4] 
Exemplo de saída: 10

'''

'''
lista_num = [randint(50,8000) for _ in range(50)] 
soma = reduce(lambda x, y: x + y, lista_num)
print(soma) 
'''
def soma(lista = list[int]):
    return reduce(lambda x,y: x + y, lista)

lista = [randint(50,8000) for _ in range(50)] 
resultado = soma(lista)
print(resultado)
