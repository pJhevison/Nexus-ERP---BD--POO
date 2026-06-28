# Nexus ERP Telecom

Sistema ERP de telecomunicacoes desenvolvido para a disciplina de Programacao Orientada a Objetos.

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
- `DB_PASSWORD=postgres`
- `DB_HOST=localhost`
- `DB_PORT=5432`

Exemplo no PowerShell:

```powershell
$env:DB_NAME="nexus_erp"
$env:DB_USER="postgres"
$env:DB_PASSWORD="postgres"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
```

As tabelas sao criadas automaticamente na inicializacao do sistema a partir de `database/schema.sql`.

## Como executar

Ative o ambiente virtual e execute:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
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
