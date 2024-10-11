### Estruturas de Repetição###

# FOR: sabemos a quantidade de vezes que o laço de repetição foi executado.

for i in range(5):
    # o (i é um comando do python , ele lê a lista,seja ela qual for 
    #(o in é seguinifica que algo que eu estou vericando está dentro),
    #(o range siguinifica corrrida,comprimento))
    numero=int(input("Digite um número"))
    print(f"Dobro:{numero*2}")


# WHILE: queremos a repetição quando a condição for verdadeira.
# O WHILE 
    
contador=0
while contador <5: 
    numero=int (input("Digite um número"))
    print(f"Triplo:{numero*3}")
    contador=contador+1

# WHILE: queremos a repetição quando a condição for verdadeira.

# similar ao "WHILE", mas garante que o bloco seja lido ao menos
# antes da verificação da condição