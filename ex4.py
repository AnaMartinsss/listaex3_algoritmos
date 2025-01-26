'''
Nomes com mais de 5 letras (com filter) 
Escreva uma função que receba uma lista de nomes e, utilizando filter, retorne 
apenas os nomes com mais de 5 letras. 
Exemplo de entrada: ["Ana", "Lucas", "Fernanda", "João"] 
Exemplo de saída: ["Lucas", "Fernanda"]

'''
nome = ['Vinícius', 'Renata', 'Daniela', 'Rodrigo','Isabela', 'Mariana', 'Paulo', 'Gabriela', 'Bruna', 'Rafael', 'Clara', 'Carlos', 'Tiago', 'Ricardo', 'Miguel']
resultado = list(filter(lambda nome: len(nome) > 5, nome))
print(resultado)