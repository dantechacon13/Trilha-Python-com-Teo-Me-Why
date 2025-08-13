# Faça um programa que venda uma garrafa de água:
# Se o cliente escolher mineral natural, será cobrado R$1.50
# Se o cliente escolher mineral com gás, será cobrado R$2.50

# 3 aspas duplas (""") permitem criar uma string de várias linhas (bloco de texto)
texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""

# input() → solicita uma entrada do usuário
# a variável 'opcao' irá armazenar a escolha feita
opcao = input(texto)

# atribuição (=) → define que 'conta' começa com o valor 0
conta = 0

# if → condicional que executa um bloco se a expressão for verdadeira
# '==' → operador de igualdade (compara valores)
# aspas duplas ("1") → indicam que a comparação é com uma string
if opcao == "1":
    conta = 1.5   # atribuição (=) → define o valor de conta como 1.5 se a condição for verdadeira
   
# elif → "else if" (senão se), outra condição que será testada apenas se a primeira falhar
elif opcao == "2": 
    conta = 2.5   # atribui 2.5 a conta caso a condição seja verdadeira

# novo if → verifica se 'conta' continua valendo 0
# isso significa que nenhuma das opções anteriores foi escolhida corretamente
if conta == 0:
    # print() → exibe mensagem ao usuário
    print("Entre com a opção correta, por favor")

# else → executa este bloco se o if anterior for falso
else:
    # vírgula dentro do print separa argumentos, e o Python insere um espaço automaticamente
    print("Sua conta é: R$", conta)
