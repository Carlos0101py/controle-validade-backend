# Controle De Validade De Produtos

Uma API desenvolvida para fornecer uma solução web eficaz no controle de validades de produtos.

## Índice

- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Introdução

Este projeto foi criado com o objetivo de desenvolver uma solução prática para o controle de validade de produtos, uma necessidade crítica para empreendedores que dependem dessas informações para manter a qualidade e segurança de seus produtos. A escolha desse tema reflete a importância de uma ferramenta que permita aos funcionários de uma empresa compartilhar e acessar informações vitais sobre a validade dos produtos de forma centralizada e eficiente.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com) - Micro framework web para Python.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) - Extensão para integração com bancos de dados usando SQLAlchemy.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Extensão para gerenciamento de migrações de banco de dados.
- [Pytest](https://docs.pytest.org/en/stable/index.html) - Biblioteca usada para execução de testes unitários das rotas.
- [Python](https://www.python.org) - Linguagem de programação utilizada.
- [MySQL](https://www.mysql.com) - Sistema de gerenciamento de banco de dados relacional.

## Funcionalidades

As principais funcionalidades e recursos do projeto incluem:

- Autenticação de usuários.
- Criação e gerenciamento de produtos.
- Criação e gerenciamento de grupos para visualização dos produtos por mais de um usuário.
- Filtros avançados para busca e visualização de informações.

## Instalação

Siga as instruções abaixo para configurar o ambiente de desenvolvimento local:

1. Clone o repositório:
   git clone https://github.com/seuusuario/seu-projeto.git

2. Entre no diretório do projeto:
   cd seu-projeto

3. Crie um ambiente virtual:
 ``` python -m venv venv ```

4. Configure as variáveis de ambiente:

   Você precisará definir duas variáveis de ambiente com as seguintes informações:

   1. DATABASE_URI = "string de conexão com o MySQL ou similar"
   2. SECRET_KEY = "Senha que você preferir"

5. Ative o ambiente virtual:

   - No Linux/macOS:
     source venv/bin/activate

   - No Windows:
     venv\Scripts\activate

6. Instale as dependências:
   ``` pip install -r requirements.txt ```
