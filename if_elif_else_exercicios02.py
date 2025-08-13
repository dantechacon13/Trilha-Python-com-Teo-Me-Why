# Altere o programa anterior para considerar a qtd de água 

# 3 aspas duplas permitem criar uma string de múltiplas linhas (bloco de texto),
# facilitando a exibição de menus formatados
texto = """
Escolha a sua água para comprar
(1) Água mineral natural -- R$1.5
(2) Água mineral com gás -- R$2.5
"""

# input() → solicita ao usuário que digite uma opção
# o texto da variável 'texto' é exibido como prompt
opcao = input(texto)

# valor_item começa em 0 → representa o preço do produto escolhido
valor_item = 0

# if → condicional para verificar se a opção foi "1"
# '==' → operador de igualdade (compara valores)
# aspas → indicam que a comparação é feita com uma string
if opcao == "1":
    valor_item = 1.5   # atribui o valor de R$1.50 se a opção for 1
elif opcao == "2":     # elif → "senão se" (testa outra condição caso o if falhe)
    valor_item = 2.5   # atribui o valor de R$2.50 se a opção for 2

# verifica se o valor_item continua 0
# isso significa que nenhuma das opções válidas foi escolhida
if valor_item == 0:
    print("Entre com a opção correta, por favor")
else:
    # int() → converte a entrada para número inteiro
    qtde = int(input("Quantas garrafas? "))
    # multiplicação (*) → calcula o valor total (preço unitário × quantidade)
    valor_total = valor_item * qtde
    # print() → exibe o valor total na tela
    print("Sua conta deu: R$", valor_total)
