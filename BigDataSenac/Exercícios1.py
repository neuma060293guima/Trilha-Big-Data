



# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

#variável simples- são as que calculam a entrada de dados
lampada_potencia= float(input("Digite a potência da lâmpada (watts): ")) 
comprimento_comodo=float(input("Digite o comprimento do comôdo: "))

#essa variável é para o cálculo de área e de potência
potencia_real=3*lampada_potencia
area_comodo=largura_comodo*comprimento_comodo 
potencia_real=3*lampada_potencia

#variáveis para o calcúlo de número e de lâmpadas e de bocais
numero_lampadas=int(potencia_real/lampada_potencia )
bocais=int(area_comodo/3)

#exebição das resultados (quaisquer das formatações são válidas)
# O f é para formatação de texto
print("lâmpadas:", numero_lampadas)
print(f"Número de lâmpadas necessárias:{numero_lampadas}")
print(f"Número de bocais necessários:{bocais}")



