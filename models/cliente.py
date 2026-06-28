from models.pessoa import Pessoa


class Cliente(Pessoa):
    STATUS_ATIVO = "ATIVO"
    STATUS_INATIVO = "INATIVO"
    STATUS_INADIMPLENTE = "INADIMPLENTE"
    STATUS_PERMITIDOS = {STATUS_ATIVO, STATUS_INATIVO, STATUS_INADIMPLENTE}

    def __init__(self, nome_cliente, cpf_cnpj, telefone, status_cliente, id_cliente=None):
        super().__init__(nome_cliente)
        self.id_cliente = id_cliente
        self.__cpf_cnpj = None
        self.__status_cliente = None
        self.cpf_cnpj = cpf_cnpj
        self.atualizar_contato(telefone)
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
        self.__cpf_cnpj = self.normalizar_cpf_cnpj(valor)

    @property
    def status_cliente(self):
        return self.__status_cliente

    @status_cliente.setter
    def status_cliente(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Status do cliente nao pode ser vazio.")

        status = valor.strip().upper()
        if status not in self.STATUS_PERMITIDOS:
            raise ValueError(
                "Status do cliente deve ser ATIVO, INATIVO ou INADIMPLENTE."
            )
        self.__status_cliente = status

    @staticmethod
    def normalizar_cpf_cnpj(valor):
        if valor is None or not str(valor).strip():
            raise ValueError("CPF/CNPJ deve ser informado.")

        valor = str(valor).strip()
        if any(caractere.isalpha() for caractere in valor):
            raise ValueError("CPF/CNPJ nao pode conter letras.")

        caracteres_permitidos = set("0123456789.-/ ")
        if any(caractere not in caracteres_permitidos for caractere in valor):
            raise ValueError("CPF/CNPJ deve conter apenas numeros e pontuacao de mascara.")

        somente_numeros = "".join(caractere for caractere in valor if caractere.isdigit())
        if len(somente_numeros) not in (11, 14):
            raise ValueError("CPF/CNPJ deve ter 11 digitos para CPF ou 14 digitos para CNPJ.")

        return somente_numeros

    def ativar(self):
        self.status_cliente = self.STATUS_ATIVO

    def inativar(self):
        self.status_cliente = self.STATUS_INATIVO

    def marcar_inadimplente(self):
        self.status_cliente = self.STATUS_INADIMPLENTE

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
