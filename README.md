# inventory-management-system

## Evolução do projeto (Inventory Management)

### 1) Adicionando funções para exibir o menu e inicializar o sistema
- Commit: `35bccac`
- O que foi feito:
  - Estrutura do menu em uma função `menu()`
  - Inicialização da opção do usuário com `initialize()`
  - Loop principal controlando o fluxo das opções (1 a 4)

### 2) Atualiza `item_name` que recebia uma lista vazia em um dicionário contido na variável `store`
- Commit: `fa7bdcc`
- O que foi feito:
  - Padronização do modelo de dados para o `store` funcionar como um dicionário.
  - Agora os itens ficam salvos assim:
    - `store[item_name] = { "unidades": ..., "descricao": ..., "valor": ... }`
  - Isso garante que o `item_name` seja uma chave usada para inserir/atualizar/remover itens do inventário.

    ### Estrutura dos dados
- `store` (dict): dicionário que guarda os itens do inventário
- Chave: `item_name` (nome do item)
- Valor: outro dict com:
  - `unidades`
  - `descricao`
  - `valor`