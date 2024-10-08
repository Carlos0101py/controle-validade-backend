# Controle De Validade De Produtos

Uma API desenvolvida para fornecer uma solução web eficaz no controle de validades de produtos.

## Índice

- [Introdução](#introdução)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Como Testar](#como-testar)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Introdução

Este projeto foi criado com o objetivo de desenvolver uma solução prática para o controle de validade de produtos, uma necessidade crítica para empreendedores que dependem dessas informações para manter a qualidade e segurança de seus produtos. A escolha desse tema reflete a importância de uma ferramenta que permita aos funcionários de uma empresa compartilhar e acessar informações vitais sobre a validade dos produtos de forma centralizada e eficiente.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com) - Micro framework web para Python.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) - Extensão para integração com bancos de dados usando SQLAlchemy.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Extensão para gerenciamento de migrações de banco de dados.
- [flasgger](https://github.com/flasgger/flasgger) - Gerador automatico de documentação com base em anotações nas rotas Flask
- [Python](https://www.python.org) - Linguagem de programação utilizada.
- [MySQL](https://www.mysql.com) - Sistema de gerenciamento de banco de dados relacional.

## Funcionalidades

As principais funcionalidades e recursos do projeto incluem:

- Autenticação de usuários.
- Criação e gerenciamento de produtos.
- Filtros avançados para busca e visualização de informações.

## Instalação

Siga as instruções abaixo para configurar o ambiente de desenvolvimento local:

Clone o repositório
```
git clone https://github.com/seuusuario/seu-projeto.git
```

Entre no diretório do projeto
```
cd "seu-projeto"
```

Crie um ambiente virtual
```
python -m venv venv
```

Ative o ambiente virtual
No Linux/macOS:
```
source venv/bin/activate
```
No Windows:
```
venv\Scripts\activate
```

Instale as dependências
```
pip install -r requirements.txt
```

Configure as variáveis de ambiente:
   1. DATABASE_URI = "string de conexão com o MySQL ou similar"
   2. SECRET_KEY = "Senha que você preferir"

Faça a inicialização do banco de dados
```
flask db upgrade
```

## Como Testar
Inicialize o servidor do flask
```
python run.py
```
Acesse a URL da documentação interativa no navegador
```
http://127.0.0.1:5000/apidocs/ 
```


