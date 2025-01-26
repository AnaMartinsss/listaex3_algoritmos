from random import randint
'''
Agrupar números em categorias (com dicionários e lambdas) 
Escreva uma função que receba uma lista de números inteiros e utilize map e filter 
para criar um dicionário que agrupe os números em três categorias: 
o "positivos" (números maiores que 0) 
o "negativos" (números menores que 0) 
o "zeros" (números iguais a 0). 
o Exemplo de entrada: [1, -2, 0, 3, -5, 0] 
o Exemplo de saída: {"positivos": [1, 3], "negativos": [-2, -5], "zeros": [0, 0]}

'''
lista_num = [randint(-100,100) for _ in range(20)]
positivos = list(filter(lambda x: x > 0, lista_num))
negativos = list(filter(lambda x: x < 0, lista_num))
zeros = list(filter(lambda x: x == 0, lista_num))
retorna = {'positivos': positivos, 'negativos': negativos, 'zeros': zeros}
print(retorna)