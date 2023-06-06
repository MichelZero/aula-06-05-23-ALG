#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# Implemente um programa em Python que imprime em tela todos os números 
# entre 1 e 100 que são divisíveis por um determinado número informado 
# pelo usuário. Um número é divisível por outro se o resto de sua divisão 
# por este número é igual a zero. Por exemplo, 4 é divisível por 2 porque o resto da divisão 
# inteira de 4 por 2 é igual a 2 e possui resto igual a zero.

# Entrada de dados
num = int(input("Digite um número inteiro positivo: "))
# Processamento
for i in range(1, 101):
    if i % num == 0:
        print(i)
# Saída de dados
print("Fim do programa")