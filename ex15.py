#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# Elabore um programa em Python, utilizando 
# estrutura de repetição, que exibe 
# em tela todos os números ímpares entre
# o número um e um certo 
# número inteiro positivo informado pelo usuário.

# Entrada de dados
num = int(input("Digite um número inteiro positivo: "))
# Processamento
if num >= 1:  
  for i in range(1, num + 1):
      if i % 2 != 0:
          print(i)
else:
  print(f"{num} não é positivo!")
# Saída de dados
print("Fim do programa")