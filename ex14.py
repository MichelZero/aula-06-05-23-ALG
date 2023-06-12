#
#
# autores: Michel, Cristiano
#
# data: 06-06-2023

# 6.	Escreva um programa que verifica se de 1 a 100 
# quanto múltiplo de 3 ou de 5 existem.

# Entrada de dados
quant = 0
soma = 0
# Processamento
for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print(i)
    quant +=1
    soma +=i

# Saída de dados
print(f"existe {quant} números")
print(f"a soma foi {soma}")
print("Fim do programa")