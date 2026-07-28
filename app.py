# Importando modulos
from modules.crud import (
    show_menu,
    get_option,
    create_item,
    delete_item,
    list_items,
    update_item
)

from modules.variables import (
    done,
    div
)

print("Sistema de gerenciamento de Inventario")



# Contem a logica do menu
while not done :
    print(div)
    show_menu()
    print(div)
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