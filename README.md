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

## Pré-requisitos

| Tecnologia | Obrigatório | Observação |
|---|---|---|
| Python 3.12 ou superior | Sim | Necessário para executar o sistema |
| PostgreSQL | Sim | Banco de dados utilizado pelo projeto |
| psycopg2-binary | Sim | Instalado pelo `requirements.txt` |
| pgAdmin | Opcional | Usado apenas para visualizar o banco |
| VS Code | Opcional | Ambiente usado no desenvolvimento |

## Entrega do banco de dados

O banco de dados não é entregue como arquivo `.db`, pois o projeto utiliza PostgreSQL.

A estrutura do banco é entregue por meio do arquivo `database/schema.sql`, e a criação automática das tabelas é feita pela função `criar_tabelas()` no arquivo `database/connection.py`.

Para reproduzir o banco em outro computador, basta criar um banco vazio chamado `nexus_erp` e executar:

```powershell
pip install -r requirements.txt
python main.py

## Execução do sistema

Antes de executar, crie no pgAdmin um banco de dados vazio chamado `nexus_erp`.

### Execução pelo terminal ou VS Code

No PowerShell, entre na pasta do projeto, ative o ambiente virtual e execute o arquivo principal:

```powershell
cd C:\Users\pedro\Documents\Nexus-ERP---BD--POO
.\.venv\Scripts\Activate.ps1
python main.py

## Evidências dos conceitos de POO no código

Esta seção apresenta trechos do código onde os principais conceitos de Programação Orientada a Objetos foram aplicados no projeto.

## Classe abstrata

Arquivo: `models/pessoa.py`

```python
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def obter_identificacao(self):
        pass
```
---
### FUNDAMENTOS UTILIZADOS DE PROGRAMAÇÃO ORIENTADA A OBJETOS

| Conceito | Explicação |
|---|---|
| Classe abstrata | A classe `Pessoa` foi criada usando `ABC`, indicando que ela serve como base para outras classes. |
| Contrato | O método `obter_identificacao()` é abstrato, obrigando as classes filhas a implementarem esse comportamento. |
| Justificativa | Faz sentido porque `Cliente` e `Funcionario` são tipos de pessoa no sistema, mas cada um possui uma forma diferente de identificação. |

## Herança

Arquivos: `models/cliente.py` e `models/funcionario.py`

```python
from models.pessoa import Pessoa


class Cliente(Pessoa):
    def obter_identificacao(self):
        return f"Cliente: {self.nome_cliente} - CPF/CNPJ: {self.cpf_cnpj}"
```

```python
from models.pessoa import Pessoa


class Funcionario(Pessoa):
    def obter_identificacao(self):
        return f"Funcionario: {self.nome} - Cargo: {self.cargo}"
```

| Conceito | Explicação |
|---|---|
| Herança | `Cliente` e `Funcionario` herdam da classe abstrata `Pessoa`. |
| Reaproveitamento | O atributo comum `nome` fica centralizado na classe base. |
| Justificativa | A herança é coerente porque cliente e funcionário representam pessoas dentro do domínio do sistema. |

## Polimorfismo

Arquivo: `ui/menu.py`

```python
def _demonstrar_polimorfismo(self):
    pessoas = [
        Cliente("Maria Silva", "12345678900", "92999990000", "Ativo"),
        Funcionario("Joao Souza", "Tecnico de campo"),
    ]

    print("Mesmo metodo chamado em objetos Cliente e Funcionario:")
    for pessoa in pessoas:
        print(pessoa.obter_identificacao())
```

| Conceito | Explicação |
|---|---|
| Polimorfismo | O mesmo método `obter_identificacao()` é chamado para objetos de classes diferentes. |
| Comportamento diferente | Quando o objeto é `Cliente`, retorna dados do cliente. Quando é `Funcionario`, retorna dados do funcionário. |
| Justificativa | O sistema consegue tratar objetos diferentes de forma uniforme, respeitando o contrato definido pela classe `Pessoa`. |

## Encapsulamento

Arquivo: `models/cliente.py`

```python
class Cliente(Pessoa):
    def __init__(self, nome_cliente, cpf_cnpj, telefone, status_cliente, id_cliente=None):
        super().__init__(nome_cliente)
        self.id_cliente = id_cliente
        self.__cpf_cnpj = None
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.status_cliente = status_cliente

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, valor):
        if not valor or not valor.strip():
            raise ValueError("CPF/CNPJ nao pode ser vazio.")
        self.__cpf_cnpj = valor.strip()
```

| Conceito | Explicação |
|---|---|
| Encapsulamento | O atributo `__cpf_cnpj` é privado e não deve ser alterado diretamente fora da classe. |
| Validação | O CPF/CNPJ só pode ser alterado por meio do setter, que impede valor vazio. |
| Justificativa | CPF/CNPJ é uma informação essencial do cliente e precisa estar sempre em estado válido. |

## Encapsulamento com validação de valores

Arquivos: `models/plano.py` e `models/fatura.py`

```python
@property
def valor_mensal(self):
    return self.__valor_mensal

@valor_mensal.setter
def valor_mensal(self, valor):
    if valor <= 0:
        raise ValueError("Valor mensal deve ser maior que zero.")
    self.__valor_mensal = valor
```

```python
@property
def valor_fatura(self):
    return self.__valor_fatura

@valor_fatura.setter
def valor_fatura(self, valor):
    if valor <= 0:
        raise ValueError("Valor da fatura deve ser maior que zero.")
    self.__valor_fatura = valor
```

| Conceito | Explicação |
|---|---|
| Encapsulamento | Os valores de plano e fatura são protegidos por atributos privados e properties. |
| Regra de consistência | O sistema impede valores menores ou iguais a zero. |
| Justificativa | Não faz sentido existir plano ou fatura com valor negativo ou zerado. A própria classe protege seu estado interno. |

## Métodos de negócio

Arquivo: `models/cliente.py`

```python
def ativar(self):
    self.status_cliente = "Ativo"

def inativar(self):
    self.status_cliente = "Inativo"

def atualizar_contato(self, telefone):
    if not telefone or not telefone.strip():
        raise ValueError("Telefone nao pode ser vazio.")
    self.telefone = telefone.strip()
```

| Conceito | Explicação |
|---|---|
| Métodos de negócio | A classe `Cliente` possui comportamentos próprios, como ativar, inativar e atualizar contato. |
| Objeto com comportamento | O objeto não armazena apenas dados; ele também executa ações relacionadas ao seu domínio. |
| Justificativa | Isso reforça a modelagem orientada a objetos, pois regras ligadas ao cliente ficam dentro da classe `Cliente`. |

## Regra de negócio no Service

Arquivo: `services/cliente_service.py`

```python
def cadastrar_cliente(self, nome_cliente, cpf_cnpj, telefone, status_cliente):
    self._validar_campos_obrigatorios(nome_cliente, cpf_cnpj, telefone, status_cliente)

    if self.cliente_repository.buscar_por_cpf_cnpj(cpf_cnpj):
        raise ValueError("Ja existe cliente cadastrado com este CPF/CNPJ.")

    cliente = Cliente(nome_cliente, cpf_cnpj, telefone, status_cliente)
    return self.cliente_repository.salvar(cliente)
```

| Conceito | Explicação |
|---|---|
| Regra de negócio | O sistema não permite cadastrar dois clientes com o mesmo CPF/CNPJ. |
| Separação de responsabilidade | A regra fica no `ClienteService`, e não diretamente no menu ou no banco. |
| Justificativa | O service centraliza a lógica de negócio antes de enviar os dados para persistência. |

## Persistência com Repository

Arquivo: `repositories/cliente_repository.py`

```python
def salvar(self, cliente):
    sql = """
        INSERT INTO cliente (nome_cliente, cpf_cnpj, telefone, status_cliente)
        VALUES (%s, %s, %s, %s)
        RETURNING id_cliente
    """

    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    cliente.nome_cliente,
                    cliente.cpf_cnpj,
                    cliente.telefone,
                    cliente.status_cliente,
                ),
            )
            cliente.id_cliente = cursor.fetchone()[0]
        conexao.commit()

    return cliente
```

| Conceito | Explicação |
|---|---|
| Repository | A classe `ClienteRepository` é responsável pelo acesso ao banco de dados. |
| Persistência | O objeto `Cliente` é convertido em um registro na tabela `cliente`. |
| Justificativa | Essa separação evita que o menu ou as classes de domínio tenham comandos SQL misturados à lógica principal. |

## Integração entre objeto e tabela

| Etapa | O que acontece |
|---|---|
| 1 | O usuário informa os dados no menu |
| 2 | O `ClienteService` valida os dados e aplica as regras de negócio |
| 3 | Um objeto `Cliente` é criado no Python |
| 4 | O `ClienteRepository` executa o comando SQL |
| 5 | O cliente é salvo na tabela `cliente` do PostgreSQL |

Essa estrutura demonstra a relação entre Programação Orientada a Objetos e banco de dados relacional. A classe `Cliente` representa o conceito no código, enquanto a tabela `cliente` armazena os dados de forma persistente.
