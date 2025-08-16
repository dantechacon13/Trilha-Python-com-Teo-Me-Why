# Faça um programa que receba uma quantidade indefinida
# de valores correspondentes a "saldo em conta", mas
# quando o usuários apertar "enter" sem digitar valor
# algum, o programa para de receber valores, e exibe 
# a soma de todos os valores anteriores

# trabalhando com while:
saldo_total = 0 # valor final
while True:
    saldo = input("Digite o saldo em conta")

    if saldo == "":
        break #maneira de forçar a saída do laço while
    
    saldo_total += float(saldo)
    
print(saldo_total)

# trabalhando com for:
# precisaríamos de um input que defina a qtd, para
# criar um for finito

saldo_total = 0

qtd = int(input("Quantos saldos você quer informar? "))

for i in range(qtd):
    saldo = input(f"Digite o saldo {i+1}: ")

    if saldo == "":
        break
    saldo_total += float(saldo)

print(saldo_total)

