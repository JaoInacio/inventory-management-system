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
menu()

# Inicializando menu
def initialize() :
    question = int(input("Qual opcao deseja?\n > "))
    print(division)
    return question
option = initialize()

# Listando itens
def list_items() :
    for i, item in enumerate(store.values()) :
        print(f"{i+1}. {item['name']}\n quantidade em estoque ({item['descricao']})")

# Contem a logica do menu
while not done :
    if option == 1 :
        print("Voce escolheu a opcao 1.")
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
        pp.pprint(f"Item adicionado com sucesso!\n {store}")
    elif option == 2 :
        print("Voce escolheu a opcao 2.")
        item_name = input("Qual item deseja remover? \n")
        store.pop(item_name)
        print(store)
    elif option == 3 :
        question = input(f"Voce ecolheu opcao 3, qual item deseja atualizar?\n")
        pp.pprint(store)
        item_key = store.update(item_name)
        new_item = input("Qual o nome do novo item? \n")
        pp.pprint(f"Item atualizado com sucesso!\n {store}")
        print(new_item)
    elif option == 4 :
        print("Voce escolheu a opcao 4.")
        list_items()
    print(division)
    menu()
    print(division)
    option = initialize()