# Importando modulo
from modules.variables import (
    store,
    div
)
import modules.variables as variables
import json

# Contem o menu
def show_menu() :
    menu_itens = " 1 - Adicionar\n 2 - Remover\n 3 - Atualizar\n 4 - Listar\n 5 - Consultar Estoque\n 6 - Carregar Dados\n 7 - Salvar Dados\n 8 - Sair"
    print(menu_itens)


# Inicializando menu
def get_option() :
    try :
        question = int(input("Qual opcao deseja?\n > "))
        print(div)
        return question
    except ValueError:
        print("Digite apenas números.")

# Salvando arquivos Json
def save_file(file_name:str) :
    if ".json" not in file_name :
        file_name = f"{file_name}.json"
    
    with open(file_name, "w", encoding = "utf-8") as arquivo :
        arquivo.write(json.dumps(store, indent = 4, ensure_ascii = False))

# Criando metodo para salvar
def saving() :
    question = input("Deseja salvar em um novo arquivo?\n > ")
    if "S" in question.upper() :
        variables.file_name = input("Qual nome do arquivo deseja criar?\n > ")
        save_file(variables.file_name)
    else :
        save_file(variables.file_name)
        print("Arquivo salvo com sucesso!")



# Carregando arquivos .json
def load_file() :
    file_name = input("Qual o nome do arquivo deseja carregar?\n > ")
    
    if ".json" not in file_name :
        file_name = f"{file_name}.json"
    
    with open(file_name, "r", encoding = "utf-8") as file :
        content = json.load(file)
        
        
        store.clear()
        store.update(content)
        
        print("Carregado com sucesso!")

# Criando itens
def create_item() :
    item_name = input("Qual nome do item?\n > ")
    unit = get_int("Quantas unidades?\n > ")
    description = input("Descrição.\n > ")
    value = get_float("Valor por unidade.\n> ")
    store[item_name] = {
        "nome" : item_name,
        "unidades" : unit,
        "descricao" : description,
        "valor" : value
    }

# Deletando itens
def delete_item() :
    item_num = get_int("Informe o numero do item que deseja remover.\n> ")
    while True :
        if 1 <= item_num <= len(store) :
            item_name =list(store.keys()) [item_num - 1]
            del store[item_name]
            print("Item removido com sucesso!")
            break
        else :
            print(f"O item {item_num} não consta na lista.")
            item_num = get_int("Informe o numero do item que deseja remover.\n> ")


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
    item_num = get_int("Informe o numero do item que deseja atualizar.\n > ")
    while True :
        if 1 <= item_num <= len(store) :
            item_name = list(store.keys()) [item_num - 1]
            del store[item_name]
            create_item()
            print("Item atualizado com sucesso!")
            break
        else :
            print(f"O item {item_num} não consta na lista.")
            item_num = get_int("Informe o numero do item que deseja atualizar.\n > ")



# Funções para tratemento de erro
def get_float(message) :
    while True :
        try :
            return float(input(message))
        except ValueError :
            print("Digite um numero válido e com a separação decimal por ponto(.)")

def get_int(message) : 
    while True :
        try :
            return int(input(message))
        except ValueError :
            print("Digite um valor númerico.")
