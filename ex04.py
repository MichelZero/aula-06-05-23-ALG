#
#
# autores: Michel
#
# data: 06-06-2023

# 4.	Faça um programa que leia um número inteiro e verifique se ele é um número primo.

# Entrada de dados
num = int(input("Digite um número inteiro: "))
# Processamento para verificar se o número é primo
# atentar para o uso do else no laço FOR 
# https://docs.python.org/pt-br/3/tutorial/controlflow.html
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_operators.asp
# nos links acima, procure por "break" e "else"

if num > 1: # Números primos são maiores que 1
    for i in range(2, num): # Números primos são divisíveis por 1 e por ele mesmo apenas (2, num) = 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., num
        if (num % i) == 0: # Se o resto da divisão do número por i for igual a zero, o número não é primo e o laço é interrompido 
            print(f"O número {num} não é primo") 
            break # Interrompe o laço for 
    else: # Se o laço for concluído sem interrupção, o número é primo 
        print(f"O número {num} é primo")
else:  # Se o número for menor ou igual a 1, ele não é primo
    print(f"O número {num} não é primo")
    
# Saída de dados
print("Fim do programa")
  