"""
Questão 07

• Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade 

Ex.: [('paulo', 28), ('Jose', 23), ('Roberto', 17)] 

Ainda deve fazer:
• excluir o ultimo valor
• adicionar uma nova tupla no inicio da lista
• Crie uma cópia da lista para não utilizar o mesmo endereço de memoria

"""    #CONCLUIDO

lista_tupla = [('João', 28), ('Jose', 23), ('Anderson', 17)] 
print(lista_tupla)
del lista_tupla[2]
print(lista_tupla)
lista_tupla.insert(0, ('weslley', 23))
print(lista_tupla)
lista_copia = lista_tupla.copy()
print(lista_copia)
