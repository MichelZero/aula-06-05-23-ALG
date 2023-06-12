#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# 6.	Escreva um programa que verifica se um número é 
# múltiplo de 3 ou de 5 ou de 
# ambos e imprime a mensagem correspondente.

# Entrada de dados
num = int(input("Digite um número inteiro: "))
# Processamento
if num % 3 == 0 and num % 5 == 0:
    print(f"O número {num} é múltiplo de 3 e de 5")
elif num % 3 == 0:
    print(f"O número {num} é múltiplo de 3")
elif num % 5 == 0:
    print(f"O número {num} é múltiplo de 5")
else:
    print(f"O número {num} não é múltiplo de 3 e nem de 5")

# Saída de dados
print("Fim do programa")