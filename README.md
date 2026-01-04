# Projeto Django – Cadastro de Funcionários

## 📌 Descrição Geral

Este projeto foi desenvolvido como atividade prática do programa **Bolsa Futuro Digital (SOFTEX)**, com o objetivo de consolidar os fundamentos do framework **Django**, desde a configuração do ambiente até a execução de uma aplicação web funcional com persistência de dados.

A aplicação demonstra conceitos essenciais como uso de ambiente virtual, criação de projetos e apps Django, modelagem de dados, migrações, painel administrativo e utilização do banco de dados SQLite.

---

## 🎯 Objetivo do Projeto

Demonstrar o funcionamento de uma aplicação web Django simples, capaz de:

- Criar e configurar um projeto Django
- Utilizar ambiente virtual (`venv`)
- Criar aplicativos Django
- Modelar dados utilizando ORM do Django
- Executar migrações de banco de dados
- Persistir dados com SQLite
- Executar o servidor de desenvolvimento local
- Compreender a estrutura padrão de um projeto Django

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Django 5.2.9**
- **SQLite**
- **Virtualenv (venv)**
- **Git e GitHub**

---

## 📁 Estrutura do Projeto

```text
meu_projeto_django/
├── config/              # Configurações principais do projeto
├── core/                # App principal (configurações globais)
├── home/                # App responsável pela aplicação
├── manage.py            # Script de gerenciamento do Django
├── db.sqlite3           # Banco de dados SQLite
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados pelo Git
└── venv/                # Ambiente virtual (não versionado)
▶️ Como Executar o Projeto Localmente
1️⃣ Clonar o repositório
bash
Copiar código
git clone https://github.com/ThiagoAPCV/Projeto-Django-Cadastro-de-Funcionarios.git
cd Projeto-Django-Cadastro-de-Funcionarios/meu_projeto_django
2️⃣ Criar e ativar o ambiente virtual
bash
Copiar código
python -m venv venv
Windows:

powershell
Copiar código
.\venv\Scripts\Activate.ps1
Linux / Mac:

bash
Copiar código
source venv/bin/activate
3️⃣ Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Executar as migrações do banco de dados
bash
Copiar código
python manage.py migrate
5️⃣ Iniciar o servidor de desenvolvimento
bash
Copiar código
python manage.py runserver
6️⃣ Acessar a aplicação
No navegador, acesse:

cpp
Copiar código
http://127.0.0.1:8000/
📸 Evidência de Funcionamento
O funcionamento do projeto pode ser comprovado através de:

Execução do servidor Django via terminal

Acesso bem-sucedido à aplicação pelo navegador

Persistência de dados no banco SQLite

Esses testes validam a correta configuração do ambiente e a execução da aplicação.

📚 Aprendizados Consolidados
Estrutura e organização de projetos Django

Importância do uso de ambiente virtual

Utilização do ORM do Django

Gerenciamento de dependências

Execução e depuração local

Versionamento de código com Git

👤 Autor
Thiago Vasconcelos
Projeto desenvolvido para fins educacionais no programa Bolsa Futuro Digital – SOFTEX.

📄 Licença
Este projeto é destinado exclusivamente para fins educacionais.
