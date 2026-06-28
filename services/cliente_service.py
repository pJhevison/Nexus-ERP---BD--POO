from models.cliente import Cliente


class ClienteService:
    def __init__(self, cliente_repository):
        self.cliente_repository = cliente_repository

    def cadastrar_cliente(self, nome_cliente, cpf_cnpj, telefone, status_cliente):
        self._validar_campos_obrigatorios(nome_cliente, cpf_cnpj, telefone, status_cliente)
        if self.cliente_repository.buscar_por_cpf_cnpj(cpf_cnpj):
            raise ValueError("Ja existe cliente cadastrado com este CPF/CNPJ.")

        cliente = Cliente(nome_cliente, cpf_cnpj, telefone, status_cliente)
        return self.cliente_repository.salvar(cliente)

    def listar_clientes(self):
        return self.cliente_repository.listar()

    def buscar_por_cpf_cnpj(self, cpf_cnpj):
        if not cpf_cnpj or not cpf_cnpj.strip():
            raise ValueError("CPF/CNPJ deve ser informado.")
        return self.cliente_repository.buscar_por_cpf_cnpj(cpf_cnpj.strip())

    def editar_cliente(self, cpf_cnpj_atual, nome_cliente, novo_cpf_cnpj, telefone, status_cliente):
        self._validar_campos_obrigatorios(nome_cliente, novo_cpf_cnpj, telefone, status_cliente)
        cliente = self.buscar_por_cpf_cnpj(cpf_cnpj_atual)
        if cliente is None:
            raise ValueError("Cliente nao encontrado.")

        cliente_com_novo_cpf = self.cliente_repository.buscar_por_cpf_cnpj(novo_cpf_cnpj)
        if cliente_com_novo_cpf and cliente_com_novo_cpf.id_cliente != cliente.id_cliente:
            raise ValueError("Ja existe outro cliente com este CPF/CNPJ.")

        cliente.nome_cliente = nome_cliente.strip()
        cliente.cpf_cnpj = novo_cpf_cnpj.strip()
        cliente.atualizar_contato(telefone)
        cliente.status_cliente = status_cliente.strip()
        self.cliente_repository.atualizar(cliente)
        return cliente

    def excluir_cliente(self, cpf_cnpj):
        cliente = self.buscar_por_cpf_cnpj(cpf_cnpj)
        if cliente is None:
            raise ValueError("Cliente nao encontrado.")
        return self.cliente_repository.excluir_por_id(cliente.id_cliente)

    def _validar_campos_obrigatorios(self, nome_cliente, cpf_cnpj, telefone, status_cliente):
        campos = {
            "nome_cliente": nome_cliente,
            "cpf_cnpj": cpf_cnpj,
            "telefone": telefone,
            "status_cliente": status_cliente,
        }
        for nome_campo, valor in campos.items():
            if not valor or not valor.strip():
                raise ValueError(f"{nome_campo} deve ser informado.")
