# 📦 Inventory Management System

Sistema de gerenciamento de estoque desenvolvido em Python como projeto de estudo e prática de lógica de programação, estruturas de dados, modularização e manipulação de arquivos JSON.

O projeto começou como uma aplicação simples para gerenciamento de itens e foi evoluindo gradualmente, passando a utilizar uma estrutura modular e persistência dos dados em arquivos JSON.

---

## 🚀 Funcionalidades

Atualmente o sistema possui:

- ✅ Adicionar itens ao estoque
- ✅ Listar itens cadastrados
- ✅ Atualizar itens
- ✅ Remover itens
- ✅ Consultar estoque
- ✅ Salvar dados em arquivos JSON
- ✅ Carregar dados de arquivos JSON
- ✅ Listar arquivos JSON disponíveis no projeto
- ✅ Escolher em qual arquivo JSON salvar os dados
- ✅ Criar novos arquivos JSON
- ✅ Menu interativo pelo terminal
- ✅ Validação de entradas numéricas
- ✅ Organização do código em módulos

---

## 🛠️ Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub

### Bibliotecas utilizadas

- `json` — leitura e escrita dos arquivos JSON
- `os` — identificação dos arquivos JSON existentes no diretório

---

## 📂 Estrutura do projeto

```text
inventory-management-system/
│
├── app.py
├── README.md
├── .gitignore
│
├── controle_estoque.json
├── estoque.json
├── novo.json
│
└── modules/
    ├── crud.py
    ├── menu.py
    └── variables.py



app.py

Arquivo responsável por iniciar a aplicação e chamar o menu principal.

modules/menu.py

Responsável pelo fluxo do menu e pela interação entre as opções escolhidas pelo usuário e as funções do sistema.

modules/crud.py

Concentra as principais funcionalidades do sistema, incluindo:

criação de itens;
listagem;
atualização;
exclusão;
consulta do estoque;
salvamento em JSON;
carregamento de JSON;
listagem dos arquivos JSON;
validação de entradas.
modules/variables.py

Centraliza algumas variáveis utilizadas pelo sistema, como:

done = False
store = {}
div = "=" * 50
file_name = None
📋 Menu do sistema

Ao executar o programa, o usuário encontra as seguintes opções:

1 - Adicionar
2 - Remover
3 - Atualizar
4 - Listar
5 - Consultar Estoque
6 - Carregar Dados
7 - Salvar Dados
8 - Sair
📦 Estrutura dos dados

Os produtos são armazenados em um dicionário Python.

Exemplo:

store = {
    "Notebook": {
        "nome": "Notebook",
        "unidades": 8,
        "descricao": "Dell Inspiron",
        "valor": 3500.00
    }
}

O nome do produto é utilizado como chave do dicionário, permitindo localizar e manipular os dados de forma mais organizada.

💾 Persistência com JSON

Uma das principais evoluções do projeto foi a implementação da persistência dos dados.

Anteriormente, os dados ficavam somente na memória enquanto o programa estava em execução.

Agora o sistema consegue transformar o dicionário store em JSON e armazená-lo em um arquivo.

Exemplo:

{
    "Notebook": {
        "nome": "Notebook",
        "unidades": 8,
        "descricao": "Dell Inspiron",
        "valor": 3500.0
    }
}

Dessa forma, os dados podem continuar disponíveis mesmo depois que o programa é encerrado.

📁 Gerenciamento dos arquivos JSON

O sistema também consegue identificar os arquivos .json existentes no diretório.

Exemplo:

1 - estoque.json
2 - controle_estoque.json
3 - novo.json

Isso permite ao usuário escolher um arquivo existente para carregar ou utilizar como destino para salvar os dados.

Criar um novo arquivo

Ao selecionar a opção de salvar, o sistema pergunta:

Deseja salvar em um novo arquivo?
> sim

Caso a resposta seja positiva, o usuário informa o nome do arquivo:

Qual nome do arquivo deseja criar?
> meu_estoque

O sistema adiciona a extensão .json quando necessário.

Resultado:

meu_estoque.json
Utilizar um arquivo existente

Caso o usuário escolha não criar um novo arquivo, o sistema apresenta os arquivos JSON disponíveis para que seja escolhido um arquivo existente.

🔄 Operações CRUD

O projeto implementa as quatro operações básicas de manipulação de dados:

Operação	Função
Create	create_item()
Read	list_items()
Update	update_item()
Delete	delete_item()

Essas operações permitem realizar o gerenciamento básico dos produtos cadastrados.

🧠 Conceitos praticados

Durante o desenvolvimento deste projeto estou praticando conceitos importantes de Python, como:

Variáveis
Strings
Números
Dicionários
Listas
Funções
Parâmetros
Retorno de funções
if, elif e else
while
for
enumerate()
List comprehension
try/except
Manipulação de arquivos
with open()
JSON
json.dumps()
json.load()
Modularização
Imports entre módulos
Organização de responsabilidades
CRUD
Git
GitHub
🧩 Modularização

Uma das principais mudanças realizadas no projeto foi a separação do código em módulos.

Antes

O projeto concentrava as funcionalidades em um único arquivo.

Atualmente

O código foi dividido de acordo com suas responsabilidades:

app.py
   │
   └── menu.py
          │
          └── crud.py
                 │
                 └── variables.py

Essa organização facilita a manutenção do código e permite adicionar novas funcionalidades sem concentrar toda a lógica em um único arquivo.

▶️ Como executar
1. Clone o repositório
git clone https://github.com/JaoInacio/inventory-management-system.git
2. Entre na pasta
cd inventory-management-system
3. Execute o programa
python app.py
📈 Evolução do projeto

O projeto vem sendo desenvolvido de forma incremental, acompanhando meu aprendizado em Python.

Etapa 1 — Estrutura inicial
Criação do menu
Cadastro de itens
Armazenamento utilizando dicionários
Etapa 2 — CRUD

Implementação das operações:

Create
Read
Update
Delete
Etapa 3 — Modularização

Separação das responsabilidades em:

app.py
modules/
├── crud.py
├── menu.py
└── variables.py
Etapa 4 — Persistência dos dados

Implementação da utilização de arquivos JSON para:

salvar dados;
carregar dados;
criar novos arquivos;
selecionar arquivos existentes;
listar arquivos JSON disponíveis.
Etapa 5 — Validação

Implementação de funções para validar entradas numéricas:

get_int()
get_float()
🔮 Próximas melhorias

Algumas funcionalidades que pretendo estudar e implementar futuramente:

 Melhorar o tratamento de erros
 Validação mais completa dos dados
 Busca de produtos
 Controle de estoque mínimo
 Melhor gerenciamento dos arquivos JSON
 Separação dos arquivos de dados em uma pasta específica
 Testes automatizados
 Banco de dados SQLite
 Interface gráfica
📚 Objetivo do projeto

Mais do que criar um sistema de estoque, este projeto está sendo utilizado para transformar os conceitos estudados em Python em uma aplicação prática.

A cada nova funcionalidade, estou buscando entender não apenas como fazer o código funcionar, mas também como organizar melhor o projeto, reutilizar funções, separar responsabilidades e trabalhar com persistência de dados.

👨‍💻 Autor

João Inácio

🔗 GitHub:
https://github.com/JaoInacio

🔗 LinkedIn:
https://www.linkedin.com/in/joão-inácio-979b71209/

⭐ Se você quiser acompanhar a evolução do projeto, fique à vontade para explorar o repositório.