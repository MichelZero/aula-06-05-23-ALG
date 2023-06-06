#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# 5. Escreva um programa em Python que imprima todos os números pares de 1 a 20 que 
# são múltiplos de 3. Utilize um loop for e a estrutura IF.

# Entrada de dados
# Processamento
for i in range(1, 21):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
# Saída de dados
print("Fim do programa")
