#Atividade

#Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos.
#Crie uma função para calcular a multa, se aplicável.


def calcular_multa(peso_total):
    limite = 100  # Limite de peso em quilos
    taxa_multa = 10  # Taxa da multa por quilo excedente

    if peso_total > limite:
        excesso = peso_total - limite
        multa = excesso * taxa_multa
        return multa
    else:
        return 0  # Sem multa

# Exemplo de uso
peso_pescado = 120  # Peso total dos peixes em quilos
multa = calcular_multa(peso_pescado)

if multa > 0:
    print(f"O pescador deve pagar uma multa de R$ {multa:.2f}")
else:
    print("O pescador não deve pagar multa.")

PS C:\Users\unidade.copacabana\Documents\BigDataSenac> & "C:/Program Files/Python311/python.exe" c:/Users/unidade.copacabana/Documents/BigDataSenac/Aula08_161020248.py
O pescador deve pagar uma multa de R$ 200.00
PS C:\Users\unidade.copacabana\Documents\BigDataSenac> 


