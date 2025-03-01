from random import randint
'''
6. Dicionário de números pares e ímpares 
Escreva uma função que receba uma lista de números inteiros e utilize lambda e 
filter para dividir a lista em números pares e ímpares. Retorne um dicionário com 
duas chaves: "pares" e "ímpares". 
Exemplo de entrada: [1, 2, 3, 4, 5, 6] 
Exemplo de saída: {"pares": [2, 4, 6], "ímpares": [1, 3, 5]} 

'''
lista_numeros = [randint(50, 200) for _ in range(20)]
impares = list(filter(lambda x: x % 2 != 0, lista_numeros))
pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
resultado = { 'pares': pares, 'impares': impares}
print(resultado)