from models.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cargo, id_func=None):
        super().__init__(nome)
        self.id_func = id_func
        self.cargo = cargo

    def obter_identificacao(self):
        return f"Funcionario: {self.nome} - Cargo: {self.cargo}"

    def alterar_cargo(self, cargo):
        if not cargo or not cargo.strip():
            raise ValueError("Cargo nao pode ser vazio.")
        self.cargo = cargo.strip()

    def __str__(self):
        return f"Funcionario(id={self.id_func}, nome={self.nome}, cargo={self.cargo})"
