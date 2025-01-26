from functools import reduce

'''
8. Contar letras em uma lista de palavras (com map e reduce) 
Crie uma função que receba uma lista de palavras e retorne a soma total de letras 
em todas as palavras, utilizando map para contar as letras e reduce para somar. 
Exemplo de entrada: ["casa", "python", "lambda"] 
Exemplo de saída: 16

'''
lista_palavras = ["amor", "casa", "python", "lambda", "functools", "reduce", "filter" ]
contar_letras = list(map(lambda palavra: len(palavra), lista_palavras))
retorna = reduce(lambda x, y: x + y, contar_letras)
print(retorna)