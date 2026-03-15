# 📋 Sistema de Cadastro de Clientes

Este projeto é um exercício prático desenvolvido durante as aulas de Python e Banco de Dados. O objetivo principal foi criar uma aplicação funcional que integra uma interface web moderna com um banco de dados relacional local.

## 🚀 Funcionalidades

- **Cadastro de Clientes:** Interface para entrada de Nome, E-mail e Telefone.
- **Validação de Dados:** Implementação de lógica em Python (Regex) para garantir formatos corretos de e-mail e telefone.
- **Segurança de Dados:** Uso de restrições SQL (`UNIQUE`) para evitar e-mails duplicados.
- **Gestão de Banco de Dados:** Operações de Inserção, Listagem e Exclusão (CRUD) utilizando SQLite.
- **Interface Web:** Desenvolvido com Streamlit para uma experiência de usuário fluida.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Interface:** [Streamlit](https://streamlit.io/)
- **Banco de Dados:** SQLite3
- **Controle de Versão:** Git e GitHub

## 📂 Estrutura do Projeto

- `main.py`: Arquivo principal com a interface e lógica do Streamlit.
- `banco.py`: Classe de conexão e comandos SQL (Backend).
- `clientes.db`: Arquivo do banco de dados (gerado automaticamente).
- `.gitignore`: Configuração para não subir arquivos temporários e o banco local.

## 🏁 Como rodar o projeto

1. Certifique-se de ter o Python e o Anaconda instalados.
2. Instale o Streamlit:
   ```bash
   pip install streamlit