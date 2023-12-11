"""
Questão 02

• Escreva um programa que, recebe uma palavra e uma frase, crie uma função que verifique se as letras da palavra aparecem na frase, e quantas vezes aparecem. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: você deve validar se a frase tem pelo menos 25 caracteres

Exemplos do resultado:
    palavra = "pato" 
    frase = "a capa do livro velho"
    P aparece 1 vez
    A aparece 3 vezes
    T não aparece
    O aparece três vezes
"""
def verificar (palavra, frase):
    if len(palavra) < 3:
        print('A palavra deve ter tres ou mais letras.')
        return
    if len(frase) < 25:
        print('A frase deve ter no minimo 25 caractere')
        return
    for letras in set (palavra):
        set(frase)
        if letras in palavra and letras in frase:
            indice_palavra = palavra.index(letras)
            indice_frase = frase.index(letras)
            print(f"'{letras} aparece '{indice_frase + indice_palavra}' vezes")

palavra = input('Informe uma palavra:')
frase =input('Digite uma frase com no minimo 25 caracteres:')

verificar (palavra, frase)