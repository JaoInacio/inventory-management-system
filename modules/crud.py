# Importando modulo
from modules.variables import (
    store,
    div
)


# Contem o menu
def show_menu() :
    menu_itens = " 1 - Adicionar\n 2 - Remover\n 3 - Atualizar\n 4 - Listar\n 5 - Consultar Estoque\n 6 - Sair"
    print(menu_itens)


# Inicializando menu
def get_option() :
    question = int(input("Qual opcao deseja?\n > "))
    print(div)
    return question


# Criando itens
def create_item() :
    item_name = input("Qual nome do item? \n")
    unit = int(input("Quantas unidades? \n"))
    description = input("Descrição. \n")
    value = float(input("Valor por unidade. \n"))
    store[item_name] = {
        "nome" : item_name,
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
    for i, item_name in enumerate(store.keys()) :
        print(f"{i+1}. {item_name}")

# Consultando estoque
def check_stock() :
    for i, item in enumerate(store.values()) :
        print(f"{i+1}. {item['nome']}\n (quantidade em estoque {item['descricao']})")



# Atualizando item
def update_item() :
    item_num = int(input("Informe o numero do item que deseja atualizar.\n > "))
    if item_num <= len(store) :
        item_name = list(store.keys()) [item_num - 1]
        del store[item_name]
        create_item()
        print("Item atualizado com sucesso!")
