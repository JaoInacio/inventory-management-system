"""Sistema de gerenciamento de Inventario"""
# Contem modulo
import pprint

# Contem as variaveis do sistema
done = False
store = {}
pp = pprint.PrettyPrinter(depth = 4)
menu_itens = """ 1- Adicionar\n 2- Remover\n 3- Atualizar\n 4- Listar\n 5- Sair"""
division = "=" * 50

# Contem o menu
def menu() :
    print(menu_itens)


# Inicializando menu
def initialize() :
    question = int(input("Qual opcao deseja?\n > "))
    print(division)
    return question


# Listando itens
def list_items() :
    for i, item in enumerate(store.values()) :
        print(f"{i+1}. {item['name']}\n quantidade em estoque ({item['descricao']})")

# Contem a logica do menu
while not done :
    print(division)
    menu()
    print(division)
    option = initialize()
    
    
    if option == 1 :
        print(f"Voce escolheu a opção {option}.")
        item_name = input("Qual item deseja adicionar? \n")
        unit = int(input("Quantas unidades? \n"))
        description = input("Descricao. \n")
        value = float(input("Valor por unidade. \n"))
        store[item_name] = {
            "name" : item_name,
            "unidades" : unit,
            "descricao" : description,
            "valor" : value
            }
        print("Item adicionado com sucesso!")
    elif option == 2 :
        print(f"Voce escolheu a opção {option}.")
        list_items()
        item_num = int(input("Informe o numero do item que deseja remover.\n"))
        if item_num <= len(store) :
            item_name = list(store.keys())[item_num - 1]
            del store[item_name]
            print("Item removido com sucesso!")
    elif option == 3 :
        question = input(f"Voce ecolheu a opção {option}, qual item deseja atualizar?\n")
        pp.pprint(store)
        item_key = store.update(item_name)
        new_item = input("Qual o nome do novo item? \n")
        pp.pprint(f"Item atualizado com sucesso!\n {store}")
        print(new_item)
    elif option == 4 :
        print(f"Voce escolheu a opção {option}.")
        list_items()
    elif option == 5 :
        print("Encerrando sistema!")
        done = True
    else :
        print(f"Voce escolheu {option} escolha um opção válida!")