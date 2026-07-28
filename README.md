# 📦 Inventory Management System

Um sistema de gerenciamento de inventário desenvolvido em **Python**, criado com o objetivo de praticar conceitos fundamentais da linguagem, organização de código e boas práticas de desenvolvimento.

O projeto evoluiu gradualmente durante os estudos, passando de um único arquivo para uma estrutura modular utilizando funções reutilizáveis.

---

# 🚀 Funcionalidades

- ✅ Adicionar itens ao inventário
- ✅ Listar itens cadastrados
- ✅ Atualizar itens
- ✅ Remover itens
- ✅ Menu interativo no terminal
- ✅ Código modularizado
- ✅ Organização em funções reutilizáveis

---

# 📂 Estrutura do projeto

```text
inventory-management-system/
│
├── app.py                  # Arquivo principal
├── README.md
├── .gitignore
│
└── modules/
    ├── __init__.py         # (Opcional)
    ├── crud.py             # Operações CRUD
    └── variables.py        # Variáveis globais do sistema
```

---

# 🛠 Tecnologias utilizadas

- Python 3
- Git
- GitHub

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/JaoInacio/inventory-management-system.git
```

Entre na pasta do projeto:

```bash
cd inventory-management-system
```

Execute a aplicação:

```bash
python app.py
```

---

# 📖 Funcionamento

Ao iniciar o programa, será exibido um menu interativo:

```text
1 - Adicionar
2 - Remover
3 - Atualizar
4 - Listar
5 - Sair
```

O usuário pode cadastrar produtos, visualizar todos os itens cadastrados, atualizar informações ou remover itens do inventário.

---

# 🧠 Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos importantes de Python, como:

- Funções
- Modularização
- CRUD (Create, Read, Update e Delete)
- Dicionários
- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while` e `for`)
- Organização de código
- Reutilização de funções
- Separação de responsabilidades
- Imports entre módulos
- Boas práticas de nomenclatura
- Versionamento com Git
- Publicação no GitHub

---

# 📈 Evolução do projeto

## ✅ Estrutura inicial

Primeira versão contendo:

- menu principal;
- cadastro de itens;
- listagem de itens;
- utilização de dicionários para armazenar os dados.

---

## ✅ Organização das funções

O código foi refatorado para separar responsabilidades em funções específicas, como:

- `show_menu()`
- `get_option()`
- `create_item()`
- `list_items()`
- `delete_item()`
- `update_item()`

Essa organização reduziu a repetição de código e facilitou futuras manutenções.

---

## ✅ Melhorias na estrutura de dados

Os itens passaram a ser armazenados utilizando o próprio nome como chave do dicionário.

Exemplo:

```python
store = {
    "Notebook": {
        "name": "Notebook",
        "unidades": 8,
        "descricao": "Dell Inspiron",
        "valor": 3500.00
    }
}
```

Essa abordagem tornou o gerenciamento dos itens mais simples e organizado.

---

## ✅ Implementação completa do CRUD

O projeto passou a possuir todas as operações básicas de gerenciamento de dados:

- Create
- Read
- Update
- Delete

---

## ✅ Refatoração

Durante o desenvolvimento foram realizadas diversas melhorias, como:

- eliminação de código duplicado;
- reutilização da função `create_item()` na atualização dos itens;
- melhoria dos nomes das funções;
- organização da lógica do menu.

---

## ✅ Modularização

O projeto foi reorganizado em módulos.

Antes:

```text
inventory.py
```

Depois:

```text
app.py
modules/
    ├── crud.py
    └── variables.py
```

Essa separação tornou o projeto mais organizado, facilitando a manutenção e futuras expansões.

---

# 📚 Aprendizados

Este projeto permitiu aprofundar conhecimentos em:

- organização de projetos Python;
- modularização;
- manipulação de dicionários;
- criação de funções reutilizáveis;
- lógica de programação;
- versionamento utilizando Git;
- utilização do GitHub como portfólio.

---

# 🔮 Próximas melhorias

- [ ] Persistência dos dados utilizando JSON
- [ ] Tratamento de exceções (`try/except`)
- [ ] Validação das entradas do usuário
- [ ] Busca de itens por nome
- [ ] Controle de estoque mínimo
- [ ] Interface gráfica
- [ ] Banco de dados SQLite
- [ ] Testes automatizados

---

# 👨‍💻 Autor

**João Inácio**

🔗 GitHub

https://github.com/JaoInacio

🔗 LinkedIn

https://www.linkedin.com/in/joão-inácio-979b71209/

---

### ⭐ Caso este projeto tenha sido útil ou interessante para você, deixe uma estrela no repositório!