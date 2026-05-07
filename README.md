# PizzaLab API 🍕

## Tópicos

- [Descrição](#decricao)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalação e Execução](#instalacao-e-execucao)
- [Banco de Dados](#banco-de-dados)
- [Segurança e Login](#seguranca-e-login)
- [Documentação da API](#documentacao-da-api)
- [Deploy](#deploy)
- [Link da API](#link-da-api)
- [Desenvolvedor](#desenvolvedor)
- [Licença](#licenca)

---

<a id="descricao"></a>
## 📖 Descrição

O **PizzaLab API** é um sistema back-end desenvolvido para gerenciamento de uma pizzaria, permitindo o controle de clientes, cardápio, pedidos e produção.

O projeto foi desenvolvido utilizando Django e PostgreSQL, seguindo o padrão REST API, com autenticação JWT, validação e sanitização de dados, além de deploy em ambiente cloud.

O sistema possui foco acadêmico e tem como objetivo aplicar conceitos modernos de desenvolvimento back-end, segurança e publicação de APIs.

---

<a id="arquitetura-do-sistema"></a>
## 🏗 Arquitetura do Sistema

O sistema foi estruturado utilizando múltiplos aplicativos Django para melhor organização e modularização.

```bash
Pizzalab/
│
├── apps/
│   ├── cardapio/
│   ├── clientes/
│   ├── pedidos/
│   ├── producao/
│   ├── usuarios/
│   └── core/
│
├── pizzalab/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

<a id="funcionalidades"></a>
## ⚙ Funcionalidades

- **Cadastro e login de usuários**
- **Gerenciamento de clientes**
- **Gerenciamento do cardápio**
- **Gerenciamento de pedidos**
- **Gerenciamento da produção**

---

<a id="tecnologias-utilizadas"></a>
## 🛠 Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| **Back-end** | Python, Django, Django REST Framework, PostgreSQL |
| **Segurança** | JWT Authentication, Django Forms, Bleach |
| **Deploy** | Gunicorn, WhiteNoise, Render |
| **Ferramentas** | Postman, GitHub |

---

<a id="requisitos-do-sistema"></a>
## 💻 Requisitos do Sistema

- **Python 3.12** ou superior
- **PostgreSQL** instalado e configurado
- **Pip** para gerenciamento de dependências
- **Virtualenv** para criação do ambiente virtual Python
- **Navegador Web moderno** (Chrome, Edge ou Firefox)
- **Visual Studio Code** ou outra IDE compatível com Python e Django

---

<a id="instalacao-e-execucao"></a>
## 🚀 Instalação e Execução

1. **Clonar o repositório**
   
```bash
git clone https://github.com/SEU-USUARIO/BackEndPizzalab.git
```

2. **Entrar na pasta do projeto**

```bash
cd BackEndPizzalab
```

3. **Criar ambiente virtual**
   
    Windows:
   
     ```bash
     python -m venv venv
     ```

     Linux/Mac:
   
     ```bash
     python3 -m venv venv
     ```
   
4. **Ativar ambiente virtual**
   
    Windows:
   
     ```bash
     venv\Scripts\activate
     ```
    Linux/Mac:

     ```bash
     source venv/bin/activate
     ```
     
5. **Instalar dependências**
   
```bash
pip install -r requirements.txt
```
     
6. **Configurar variáveis de ambiente**

   Criar um arquivo .env na raiz do projeto:
  
    ```bash
    SECRET_KEY=sua_secret_key
    DEBUG=True
    DATABASE_URL=sua_database_url
    ```

7. **Executar migrations**
   
  ```bash
  python manage.py migrate
  ```

8. **Rodar servidor**
   
  ```bash
  python manage.py runserver
  ```

---

<a id="banco-de-dados"></a>
## 💾 Banco de Dados

O sistema utiliza PostgreSQL como banco de dados principal.

A conexão é realizada utilizando variáveis de ambiente para maior segurança.

Exemplo:

```bash
DATABASE_URL=postgresql://usuario:senha@host:porta/database
```

---

<a id="seguranca-e-login"></a>
## 🔐 Segurança e Login

O sistema implementa autenticação utilizando JWT (JSON Web Token).

Após realizar login, o usuário recebe um token JWT que deve ser enviado no cabeçalho das requisições protegidas.

- **Header de autenticação**
```bash
Authorization: Bearer TOKEN
```

- **Segurança implementada**

  - Rotas protegidas
  -  Validação de dados com Django Forms
  - Sanitização com Bleach
  - Tratamento de JSON inválido
  - Controle de métodos HTTP

---

<a id="documentacao-da-api"></a>
## 📚 Documentação da API

A documentação detalhada da API encontra-se disponível no PDF do projeto

---

<a id="deploy"></a>
## ☁ Deploy

A API encontra-se publicada online utilizando a plataforma Render.

---

<a id="link-da-api"></a>
📌 Link da API: [https://backendpizzalab.onrender.com]

---

<a id="desenvolvedor"></a>
## 👨‍💻 Desenvolvedor

  **Luiz Rodrigo Melo de Freitas Junior**
  
  - Github: luizrodrigox
    
  - LinkedIn: Luiz Rodrigo

---

<a id="licenca"></a>
## 📄 Licença

  Este projeto está licenciado sob a licença **MIT**

  Você pode usar, copiar, modificar e distribuir o sistema livremente, desde que mantenha os créditos aos autores originais.
