from models.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome_cliente, cpf_cnpj, telefone, status_cliente, id_cliente=None):
        super().__init__(nome_cliente)
        self.id_cliente = id_cliente
        self.__cpf_cnpj = None
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.status_cliente = status_cliente

    @property
    def nome_cliente(self):
        return self.nome

    @nome_cliente.setter
    def nome_cliente(self, valor):
        self.nome = valor

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, valor):
        if not valor or not valor.strip():
            raise ValueError("CPF/CNPJ nao pode ser vazio.")
        self.__cpf_cnpj = valor.strip()

    def ativar(self):
        self.status_cliente = "Ativo"

    def inativar(self):
        self.status_cliente = "Inativo"

    def atualizar_contato(self, telefone):
        if not telefone or not telefone.strip():
            raise ValueError("Telefone nao pode ser vazio.")
        self.telefone = telefone.strip()

    def obter_identificacao(self):
        return f"Cliente: {self.nome_cliente} - CPF/CNPJ: {self.cpf_cnpj}"

    def __str__(self):
        return (
            f"Cliente(id={self.id_cliente}, nome={self.nome_cliente}, "
            f"cpf_cnpj={self.cpf_cnpj}, telefone={self.telefone}, "
            f"status={self.status_cliente})"
        )
