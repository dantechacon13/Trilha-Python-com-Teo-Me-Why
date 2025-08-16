# trabalhando com while:
numero = 2
count = 1

while count <= 100:
    print(numero, "x",count,"=",numero * count)
    count += 1 # mesma coisa que count = count + 1

print("Acabou!")

# trabalhando com for:

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)
