#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

#Desenvolva um programa em Python que calcule e exiba a soma de todos os
# números entre dois números informados pelo usuário.

# Entrada de dados
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
# Processamento
soma = 0
for i in range(num1, num2 + 1):
    soma = soma + i
# Saída de dados
print(f"A soma dos números entre {num1} e {num2} é {soma}")
print("Fim do programa")
