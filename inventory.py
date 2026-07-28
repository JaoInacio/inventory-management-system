print("Sistema de gerenciamento de Inventario")

# Contem as variaveis do sistema
done = False
store = {}
division = "=" * 50

# Contem o menu
def show_menu() :
    menu_itens = " 1 - Adicionar\n 2 - Remover\n 3 - Atualizar\n 4 - Listar\n 5 - Sair"
    print(menu_itens)


# Inicializando menu
def get_option() :
    question = int(input("Qual opcao deseja?\n > "))
    print(division)
    return question


# Criando itens
def create_item() :
    item_name = input("Qual nome do item? \n")
    unit = int(input("Quantas unidades? \n"))
    description = input("Descrição. \n")
    value = float(input("Valor por unidade. \n"))
    store[item_name] = {
        "name" : item_name,
        "unidades" : unit,
        "descricao" : description,
        "valor" : value
    }


# Deletando itens
def delete_item() :
    item_num = int(input("Informe o numero do item que deseja remover.\n"))
    if item_num <= len(store) :
        item_name =list(store.keys()) [item_num - 1]
        del store[item_name]
        print("Item removido com sucesso!")


# Listando itens
def list_items() :
    for i, item in enumerate(store.values()) :
        print(f"{i+1}. {item['name']}\n quantidade em estoque ({item['descricao']})")


# Atualizando item
def update_item() :
    item_num = int(input("Informe o numero do item que deseja atualizar.\n > "))
    if item_num <= len(store) :
        item_name = list(store.keys()) [item_num - 1]
        del store[item_name]
        create_item()
        print("Item atualizado com sucesso!")

# Contem a logica do menu
while not done :
    print(division)
    show_menu()
    print(division)
    option = get_option()
    
    if option == 1 :
        print(f"Voce escolheu a opção {option}.")
        create_item()
        print("Item adicionado com sucesso!")
    elif option == 2 :
        print(f"Voce escolheu a opção {option}.")
        list_items()
        delete_item()
    elif option == 3 :
        print(f"Voce ecolheu a opção {option}, qual item deseja atualizar?")
        list_items()
        update_item()
    elif option == 4 :
        print(f"Voce escolheu a opção {option}.")
        list_items()
    elif option == 5 :
        print("Encerrando sistema!")
        done = True
    else :
        print(f"Voce escolheu {option} escolha um opção válida!")