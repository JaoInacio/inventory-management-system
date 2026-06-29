"""Sistema de gerenciamento de Inventario"""

# Contem as variaveis do sistema
item_list = []
option= 0

# Contem o menu
print("====Menu====")
print("1- Adicionar")
print("2- Remover")
print("3- Atualizar")
print("4- Listar")
print("5- Sair")
print("================")

# Contem a logica do menu
while option != 5 :
    option = int(input("Escolha uma opcao:  "))
    if option == 1:
        print("Voce escolheu a opcao 1.")
        item_name = input("Qual item deseja adicionar? \n")
        item_list.append(item_name)
    elif option == 2 :
        print("Voce escolheu a opcao 2.")
        item_name = input("Qual item deseja remover ? \n")
        item_list.remove(item_name)
        print(item_list)
    elif option == 3 :
        question = input(f"Voce ecolheu opcao 3, qual iten deseja atualizar? \n {item_list} \n")
        item_index = item_list.index(question)
        new_item = input("Qual o nome do novo item? \n")
        item_list[item_index] = new_item
        print(f"Item atualizado com sucesso!\n {item_list}")
    elif option == 4 :
        print("Voce escolheu a opcao 4.")
        print(item_list)
    else :
        print("Saindo do sistema.")

