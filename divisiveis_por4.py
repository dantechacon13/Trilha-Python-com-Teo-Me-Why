# Quais números são 
# divisíveis por 4 no intervalo 4-100?

#trabalhando com while:
# você usa while em comparações lógicas, baseadas em condições lógicas
count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count)
    count += 1

# trabalhando com for:
# você utiliza quando deseja percorrer pelos elementos de um objeto - string ou não
for i in range(4,101): # i poderia ser qualquer outra variável
    if i % 4 == 0:
        print(i)
