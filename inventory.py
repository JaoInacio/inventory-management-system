"""Sistema de gerenciamento de Inventario"""

# Contem as variaveis do sistema
store= {}
option= 0

# Contem o menu
print("====Menu====")
print("1- Adicionar")
print("2- Remover")
print("3- Atualizar")
print("4- Listar")
print("5- Lista Detalhada")
print("6- Sair")
print("=" * 50)

# Contem a logica do menu
while option != 6 :
    option = int(input("Escolha uma opcao:  "))
    if option == 1:
        print("Voce escolheu a opcao 1.")
        item_name = input("Qual item deseja adicionar? \n")
        unit = int(input("Quantas unidades ? \n"))
        description = input("Descreva o item. \n")
        value = float(input("Valor por unidade ? \n"))
        store[item_name] = {
            "valor" : value, 
            "unidades" : unit,
            "descricao" : description
        }
    elif option == 2 :
        print("Voce escolheu a opcao 2.")
        item_name = input("Qual item deseja remover ? \n")
        store.remove(item_name)
        print(store)
    elif option == 3 :
        question = input(f"Voce ecolheu opcao 3, qual iten deseja atualizar? \n {store} \n")
        item_index = store.index(question)
        new_item = input("Qual o nome do novo item? \n")
        store[item_index] = new_item
        print(f"Item atualizado com sucesso!\n {store}")
    elif option == 4 :
        print("Voce escolheu a opcao 4.")
        print(store)
    else :
        print("Saindo do sistema.")