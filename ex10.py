#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# Crie um programa em linguagem Python, utilizando estrutura de 
# repetição, que exibe em tela a tabuada de multiplicação 
# de um determinado número.

# Entrada de dados
num = int(input("Digite um número inteiro: "))
# Processamento
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
# Saída de dados
print("Fim do programa")
