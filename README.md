# Nexus ERP Telecom

## Aluno: Pedro Jhevison
Sistema ERP de telecomunicacoes desenvolvido para a disciplina de Programacao Orientada a Objetos.

## Banco de dados

O banco PostgreSQL não é entregue como arquivo físico. O projeto possui o arquivo `database/schema.sql`, responsável pela criação das tabelas, e a função `criar_tabelas()` em `database/connection.py`, chamada automaticamente ao iniciar o sistema.

Para executar em outro computador, basta criar um banco vazio chamado `nexus_erp`, instalar as dependências e executar `python main.py`. O sistema solicitará a senha do PostgreSQL e criará as tabelas automaticamente.


## Tecnologias

- Python 3.12
- PostgreSQL
- psycopg2-binary
- Interface em terminal
- Sem frameworks externos, sem ORM e sem SQLAlchemy

## Estrutura de pastas

- `main.py`: ponto de entrada da aplicacao.
- `models/`: classes do dominio.
- `repositories/`: acesso ao banco com psycopg2.
- `services/`: regras de negocio.
- `ui/`: menu textual e interacao com o usuario.
- `database/`: conexao PostgreSQL e schema SQL.

## Configuracao do banco

Crie um banco PostgreSQL chamado `nexus_erp` ou configure outro nome por variavel de ambiente.

Valores padrao usados em `database/connection.py`:

- `DB_NAME=nexus_erp`
- `DB_USER=postgres`
- `DB_HOST=localhost`
- `DB_PORT=5432`

Se `DB_PASSWORD` nao estiver definida, o sistema solicita a senha do PostgreSQL automaticamente ao executar `main.py`.

Exemplo no PowerShell:

```powershell
$env:DB_NAME="nexus_erp"
$env:DB_USER="postgres"
$env:DB_PASSWORD="sua_senha"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
```

As tabelas sao criadas automaticamente na inicializacao do sistema a partir de `database/schema.sql`.

## Formas de execução

### Forma 1: terminal / VS Code

No PowerShell, entre na pasta do projeto, ative o ambiente virtual e execute o sistema:

```powershell
cd C:\Users\pedro\Documents\Nexus-ERP---BD--POO
.\.venv\Scripts\Activate.ps1
python main.py
```

Ao executar `python main.py`, o sistema pergunta `Senha do PostgreSQL:` automaticamente se `DB_PASSWORD` ainda nao estiver definida.

No VS Code, abra `main.py` e use o botao Run. O sistema tambem perguntara a senha do PostgreSQL antes de criar/verificar as tabelas e abrir o menu.

### Forma 2: execução facilitada no Windows

1. Crie o banco `nexus_erp` no pgAdmin.
2. De dois cliques em `executar.bat`.
3. Informe a senha do PostgreSQL quando solicitado.

O banco pode estar vazio no inicio. As tabelas sao criadas automaticamente pelo sistema a partir de `database/schema.sql`.

Os dados cadastrados pelo menu sao persistidos no PostgreSQL. Para conferir os dados no pgAdmin, acesse `nexus_erp > Schemas > public > Tables > cliente` ou execute:

```sql
SELECT * FROM cliente;
```

## Funcionalidades da versao inicial

- Cadastrar cliente.
- Listar clientes.
- Buscar cliente por CPF/CNPJ.
- Editar cliente.
- Excluir cliente.
- Demonstrar polimorfismo entre `Cliente` e `Funcionario`.

## Conceitos de POO aplicados

- Classe abstrata: `Pessoa` em `models/pessoa.py`, usando `ABC` e `@abstractmethod`.
- Heranca: `Cliente` e `Funcionario` herdam de `Pessoa`.
- Encapsulamento: `Cliente` encapsula `cpf_cnpj` com atributo privado e property.
- Polimorfismo: o menu chama `obter_identificacao()` em objetos `Cliente` e `Funcionario`.
- Metodos de negocio: `ativar`, `inativar`, `atualizar_contato`, `alterar_cargo`, `reajustar_valor`, `resolver`.
- `__str__`: implementado nas classes principais.
- Tratamento de excecoes: menu e inicializacao capturam erros de validacao e conexao.

## Aderencia ao Modelo ER

O arquivo `database/schema.sql` cria exatamente as tabelas solicitadas:

- `cliente`
- `planos`
- `contrato`
- `fatura`
- `os`
- `funcionario`
- `atende`

A classe abstrata `Pessoa` existe apenas no codigo Python. Nao existe tabela `pessoa`, pois ela nao faz parte do Modelo ER.

O relacionamento entre funcionario e O.S. foi implementado pela tabela associativa `atende`, com chave primaria composta por `id_func` e `id_os`.
