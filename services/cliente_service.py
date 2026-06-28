from datetime import date

from models.cliente import Cliente
from models.contrato import Contrato
from models.ordem_servico import OrdemServico


class ClienteService:
    DESC_OS_INSTALACAO = "Ordem de servico gerada automaticamente para instalacao do ponto"

    def __init__(
        self,
        cliente_repository,
        plano_repository,
        contrato_repository,
        ordem_servico_repository,
    ):
        self.cliente_repository = cliente_repository
        self.plano_repository = plano_repository
        self.contrato_repository = contrato_repository
        self.ordem_servico_repository = ordem_servico_repository

    def cadastrar_cliente_com_ponto(
        self,
        nome_cliente,
        cpf_cnpj,
        telefone,
        id_planos,
        end_instalacao,
    ):
        self._validar_campos_obrigatorios(
            nome_cliente=nome_cliente,
            cpf_cnpj=cpf_cnpj,
            telefone=telefone,
            id_planos=id_planos,
            end_instalacao=end_instalacao,
        )
        cpf_cnpj_normalizado = Cliente.normalizar_cpf_cnpj(cpf_cnpj)
        if self.cliente_repository.buscar_por_cpf_cnpj(cpf_cnpj_normalizado):
            raise ValueError("Ja existe cliente cadastrado com este CPF/CNPJ.")

        cliente = Cliente(
            nome_cliente.strip(),
            cpf_cnpj_normalizado,
            telefone.strip(),
            Cliente.STATUS_ATIVO,
        )
        cliente = self.cliente_repository.salvar(cliente)
        contrato, ordem_servico = self._abrir_ponto(cliente, id_planos, end_instalacao)
        return cliente, contrato, ordem_servico

    def cadastrar_novo_ponto(self, cpf_cnpj, id_planos, end_instalacao):
        self._validar_campos_obrigatorios(
            cpf_cnpj=cpf_cnpj,
            id_planos=id_planos,
            end_instalacao=end_instalacao,
        )
        cliente = self.buscar_por_cpf_cnpj(cpf_cnpj)
        if cliente is None:
            raise ValueError("Cliente nao encontrado.")

        if cliente.status_cliente == Cliente.STATUS_INADIMPLENTE:
            raise ValueError(
                "Cliente esta inadimplente. Regularize a situacao antes de abrir novo ponto."
            )

        if cliente.status_cliente == Cliente.STATUS_INATIVO:
            raise ValueError(
                "Cliente esta inativo. Reative o cadastro antes de abrir novo ponto."
            )

        if cliente.status_cliente != Cliente.STATUS_ATIVO:
            raise ValueError("Cliente precisa estar ATIVO para abrir novo ponto.")

        contrato, ordem_servico = self._abrir_ponto(cliente, id_planos, end_instalacao)
        return cliente, contrato, ordem_servico

    def listar_clientes(self):
        return self.cliente_repository.listar()

    def listar_planos(self):
        return self.plano_repository.listar()

    def listar_ordens_servico(self):
        return self.ordem_servico_repository.listar()

    def buscar_por_cpf_cnpj(self, cpf_cnpj):
        cpf_cnpj_normalizado = Cliente.normalizar_cpf_cnpj(cpf_cnpj)
        return self.cliente_repository.buscar_por_cpf_cnpj(cpf_cnpj_normalizado)

    def editar_cliente(self, cpf_cnpj_atual, nome_cliente, novo_cpf_cnpj, telefone, status_cliente):
        self._validar_campos_obrigatorios(
            cpf_cnpj_atual=cpf_cnpj_atual,
            nome_cliente=nome_cliente,
            novo_cpf_cnpj=novo_cpf_cnpj,
            telefone=telefone,
            status_cliente=status_cliente,
        )
        cliente = self.buscar_por_cpf_cnpj(cpf_cnpj_atual)
        if cliente is None:
            raise ValueError("Cliente nao encontrado.")

        novo_cpf_cnpj_normalizado = Cliente.normalizar_cpf_cnpj(novo_cpf_cnpj)
        cliente_com_novo_cpf = self.cliente_repository.buscar_por_cpf_cnpj(
            novo_cpf_cnpj_normalizado
        )
        if cliente_com_novo_cpf and cliente_com_novo_cpf.id_cliente != cliente.id_cliente:
            raise ValueError("Ja existe outro cliente com este CPF/CNPJ.")

        cliente.nome_cliente = nome_cliente.strip()
        cliente.cpf_cnpj = novo_cpf_cnpj_normalizado
        cliente.atualizar_contato(telefone)
        cliente.status_cliente = status_cliente.strip()
        self.cliente_repository.atualizar(cliente)
        return cliente

    def excluir_cliente(self, cpf_cnpj):
        cliente = self.buscar_por_cpf_cnpj(cpf_cnpj)
        if cliente is None:
            raise ValueError("Cliente nao encontrado.")
        return self.cliente_repository.excluir_por_id(cliente.id_cliente)

    def _abrir_ponto(self, cliente, id_planos, end_instalacao):
        plano = self.plano_repository.buscar_por_id(self._converter_id(id_planos, "Plano"))
        if plano is None:
            raise ValueError("Plano nao encontrado.")

        if not end_instalacao or not end_instalacao.strip():
            raise ValueError("Endereco de instalacao deve ser informado.")

        contrato = Contrato(
            idcliente=cliente.id_cliente,
            idplanos=plano.id_planos,
            data_base=date.today(),
            end_instalacao=end_instalacao.strip(),
            tempo_contrato=12,
        )
        contrato = self.contrato_repository.salvar(contrato)

        ordem_servico = OrdemServico(
            idcontrato=contrato.id_contrato,
            data_abertura=date.today(),
            data_resolucao=None,
            status="Aberta",
            desc_os=self.DESC_OS_INSTALACAO,
            tipo_os="Instalacao",
        )
        ordem_servico = self.ordem_servico_repository.salvar(ordem_servico)
        return contrato, ordem_servico

    def _converter_id(self, valor, nome_campo):
        try:
            valor_convertido = int(valor)
        except (TypeError, ValueError) as erro:
            raise ValueError(f"{nome_campo} deve ser um numero inteiro.") from erro

        if valor_convertido <= 0:
            raise ValueError(f"{nome_campo} deve ser maior que zero.")
        return valor_convertido

    def _validar_campos_obrigatorios(self, **campos):
        for nome_campo, valor in campos.items():
            if valor is None or not str(valor).strip():
                raise ValueError(f"{nome_campo} deve ser informado.")
