 #Informações Aleatórias:

import random #trabalhar com dados gerados aleatóriamente

    # Crie uma função que gere dois números aleátorios dentro de um intervalo pré-definido.

def doisnum_aleatorios(qtd,numero_minimo,numero_maximo):
        for i in range(qtd):
            return random.randint(numero_minimo,numero_maximo)
        
numeros=doisnum_aleatorios(20,1,1000)
print(numeros)
