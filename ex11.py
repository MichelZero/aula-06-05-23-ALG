#
#
# autores: Michel, Cristiano
#
# data: 12-06-2023

# 11.	Faça um programa que leia um número inteiro 
# e verifique quantos pares e impares existe de 1 até 
# esse número.

# Entrada de dados
num = int(input("Digite um número inteiro: "))

pares = 0
impares = 0
# Processamento
for i in range(1, num+1):
  if i % 2 == 0:
      pares += 1
  else:
      impares +=1

# saída
print(f"exites {pares} pares e {impares} impares!")