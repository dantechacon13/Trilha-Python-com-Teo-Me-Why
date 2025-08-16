# Faça um programa que receba 4 alturas usando um
# laço de repetição e realize a soma dessas alturas

# trabalhando com while:
soma = 0 # valor final
qtd_entradas = 4 # contador de inputs
while qtd_entradas > 0:
    altura = input("Entre com a sua altura")
    altura = float(altura)
    soma += altura
    qtd_entradas -= 1

soma = float(soma)
print("A soma das alturas é:", soma)

# trabalhando com for:

soma = 0
qtd_entradas = 4

# mesma coisa que range(0,qtd_entradas)
for i in range(qtd_entradas): 
    altura = input("Entre com a altura:")
    altura = float(altura)
    soma += altura

print("A soma das alturas é:", soma)
