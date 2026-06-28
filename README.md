# Nexus ERP Telecom

Sistema ERP de telecomunicações desenvolvido para a disciplina de **Programação Orientada a Objetos**.

| Informação | Descrição |
|---|---|
| Projeto | Nexus ERP Telecom |
| Aluno | Pedro Jhevison |
| Disciplina | Programação Orientada a Objetos |
| Tema | ERP para empresas de telecomunicações |
| Banco de dados | PostgreSQL |
| Interface | Terminal |

## Descrição do sistema

O Nexus ERP Telecom é um sistema acadêmico desenvolvido para representar parte da estrutura de um ERP voltado para empresas de telecomunicações.

O sistema utiliza conceitos de Programação Orientada a Objetos em Python e realiza persistência de dados em um banco relacional PostgreSQL.

A versão inicial implementa o CRUD completo da entidade **Cliente**, permitindo cadastrar, listar, buscar, editar e excluir clientes. Além disso, o projeto contém as demais entidades previstas no Modelo ER, como planos, contratos, faturas, ordens de serviço, funcionários e o relacionamento de atendimento entre funcionário e ordem de serviço.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.12 | Linguagem principal do sistema |
| PostgreSQL | Banco de dados relacional |
| psycopg2-binary | Biblioteca de conexão entre Python e PostgreSQL |
| PowerShell / Terminal | Execução do sistema |
| VS Code | Ambiente de desenvolvimento |
| pgAdmin | Administração e visualização do banco de dados |

O projeto não utiliza framework web, ORM ou SQLAlchemy. A comunicação com o banco é feita diretamente com SQL por meio da biblioteca `psycopg2`.

## Estrutura do projeto

| Caminho | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada do sistema |
| `models/` | Classes de domínio do sistema |
| `repositories/` | Camada de acesso ao banco de dados |
| `services/` | Regras de negócio |
| `ui/` | Menu textual e interação com o usuário |
| `database/` | Conexão com PostgreSQL e script SQL |
| `database/schema.sql` | Criação das tabelas do banco |
| `requirements.txt` | Dependências do projeto |
| `executar.bat` | Execução facilitada no Windows |

## Banco de dados

O banco PostgreSQL não é entregue como arquivo físico. O projeto contém o arquivo `database/schema.sql`, responsável pela criação das tabelas, e a função `criar_tabelas()` em `database/connection.py`, chamada automaticamente ao iniciar o sistema.

Para executar o projeto em outro computador, basta criar um banco vazio chamado `nexus_erp`, instalar as dependências e executar o sistema. Na inicialização, o programa solicita a senha do PostgreSQL e cria automaticamente as tabelas, caso elas ainda não existam.

| Item | Descrição |
|---|---|
| Nome padrão do banco | `nexus_erp` |
| Usuário padrão | `postgres` |
| Host padrão | `localhost` |
| Porta padrão | `5432` |
| Script de criação | `database/schema.sql` |
| Criação automática | Realizada ao executar `main.py` |

As variáveis usadas pela conexão podem ser configuradas no ambiente, mas o sistema já possui valores padrão para facilitar a execução local.

| Variável | Valor padrão |
|---|---|
| `DB_NAME` | `nexus_erp` |
| `DB_USER` | `postgres` |
| `DB_HOST` | `localhost` |
| `DB_PORT` | `5432` |
| `DB_PASSWORD` | Solicitada ao executar o sistema |

## Execução do sistema

Antes de executar, crie no pgAdmin um banco de dados vazio chamado `nexus_erp`.

### Execução pelo terminal ou VS Code

No PowerShell, entre na pasta do projeto, ative o ambiente virtual e execute o arquivo principal:

```powershell
cd C:\Users\pedro\Documents\Nexus-ERP---BD--POO
.\.venv\Scripts\Activate.ps1
python main.py
