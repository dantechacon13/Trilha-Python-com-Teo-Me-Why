# Pergunte ao usuário seu nome e responde falando esse nome
# %%
nome = input("Bom dia! Qual o seu nome?")
print("Prazer,", nome, "! Fico feliz em te conhecer!")

# Crie uma história simples, adicione em um programa
# A cada parágrafo, a história deve aguardar
# o usuário apertar "enter" para continuar
# %%
# Primeira versão:
input("\nOlá! Quer ouvir uma história? Pressione enter para continuar...")
print("No alto de uma pequena colina, havia uma casa de madeira.")
input("\nPressione Enter para continuar...")
print("\nCerto dia, a casa pegou fogo.")
input("\nPressione Enter para continuar...")
print("A partir desse dia, o passarinho aparecia sempre.")
# %%
# Segunda versão:
p1 = "Olá! Quer ouvir uma história? Pressione enter para continuar..."
p2 = "No alto de uma pequena colina, havia uma casa de madeira."
p3 = "Certo dia, a casa pegou fogo"
p4 = "A partir desse dia, o passarinho aparecia sempre"
input(p1)
input(p2)
input(p3)
input(p4)
# %%
numero = int(input("Diga um número?"))
print("A raiz quadrada de", numero," é", round(pow(numero,0.5),4))
# Dê o dobro do número que o usuário inserir
# %%
numero = int(input("Diga um número?"))
dobro = numero * 2
print("O dobro de", numero, " é:", dobro)
