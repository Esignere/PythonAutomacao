# 🤖 Automação de Cadastro de Produtos

Script desenvolvido em **Python** para automatizar o cadastro de produtos em um sistema web utilizando **PyAutoGUI**.

O programa lê os dados de um arquivo CSV e utiliza automação de teclado e mouse para preencher os campos do sistema automaticamente.

## 🚀 Tecnologias utilizadas

* **Python**
* **PyAutoGUI** — automação de mouse e teclado
* **Pandas** — leitura e manipulação dos dados em CSV
* **Time** — controle de pausas durante a automação

## 📌 Como funciona

O programa realiza automaticamente as seguintes etapas:

1. Abre o Google Chrome.
2. Acessa a página de login do sistema.
3. Preenche o usuário e a senha.
4. Realiza o login.
5. Lê os produtos armazenados no arquivo `produtos.csv`.
6. Percorre cada produto do arquivo.
7. Preenche automaticamente os campos:

   * Código
   * Marca
   * Tipo
   * Categoria
   * Preço unitário
   * Custo
   * Observações
8. Envia o cadastro.
9. Repete o processo para todos os produtos.

## 📁 Estrutura do projeto

```text id="v0u2wo"
Automacao-Cadastro/
├── App.py
├── CSV/
│   └── produtos.csv
└── README.md
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash id="1x0v9j"
git clone URL_DO_SEU_REPOSITORIO
cd Automacao-Cadastro
```

### 2. Crie um ambiente virtual

```bash id="6cz1jq"
python -m venv .venv
```

No Windows:

```bash id="gk7x3n"
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash id="p1u5k4"
pip install pyautogui pandas
```

Ou, caso exista um `requirements.txt`:

```bash id="4qf5r7"
pip install -r requirements.txt
```

### 4. Configure os dados

Coloque os produtos que deseja cadastrar no arquivo:

```text id="z7h1ae"
CSV/produtos.csv
```

O arquivo deve possuir as colunas utilizadas pelo programa:

```text id="xj4l8p"
codigo
marca
tipo
categoria
preco_unitario
custo
obs
```

### 5. Execute o programa

```bash id="0xj7sk"
python App.py
```

O programa abrirá o navegador e realizará o cadastro automaticamente.

## ⚠️ Observações

O PyAutoGUI utiliza **coordenadas da tela** para localizar os elementos da página. Por isso, o funcionamento pode depender de:

* Resolução do monitor
* Escala do Windows
* Posição da janela do navegador
* Zoom do navegador
* Layout atual da página

Alterações na interface do site podem exigir a atualização das coordenadas utilizadas no código.

## 🔐 Segurança

**Não coloque credenciais reais no código antes de publicar o projeto no GitHub.**

O ideal é utilizar variáveis de ambiente para armazenar informações sensíveis, como usuário e senha.

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar **automação de tarefas**, manipulação de arquivos CSV e integração entre Python e aplicações web através de automação de interface.

## 🔮 Possíveis melhorias

* Utilizar variáveis de ambiente para as credenciais
* Substituir coordenadas fixas por identificação de elementos
* Adicionar tratamento de erros
* Criar logs para acompanhar os cadastros realizados
* Adicionar validação dos dados do CSV
* Criar uma interface para selecionar o arquivo CSV
* Detectar automaticamente quando uma página terminou de carregar
