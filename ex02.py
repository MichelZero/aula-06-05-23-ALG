#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# 2.	Faça um programa que leia dois números inteiros e verifique se o primeiro número é múltiplo do segundo número.

# Entrada de dados
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
# Processamento
if num1 % num2 == 0:
    print(f"O {num1} é múltiplo do {num2}")
else:
    print(f"O {num1} não é múltiplo do {num2}")
  
# Saída de dados
print("Fim do programa")