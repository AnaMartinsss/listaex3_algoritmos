from random import randint
'''
9. Filtrar tuplas com média maior que 5 
Escreva uma função que receba uma lista de tuplas, onde cada tupla contém 
números inteiros. Utilize map e filter para filtrar as tuplas cuja média dos valores 
seja maior que 5. 
Exemplo de entrada: [(2, 8), (4, 5, 6), (1, 2)] 
Exemplo de saída: [(2, 8), (4, 5, 6)] 

'''
lista_tuplas = [(randint(1, 10), randint(1, 10), randint(1, 10)) for _ in range(10)]
resultado = list(filter(lambda tupla: sum(tupla) / len(tupla) > 5, lista_tuplas))
print(resultado)
