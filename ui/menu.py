class MenuPrincipal:
    def __init__(self, cliente_service):
        self.cliente_service = cliente_service

    def executar(self):
        while True:
            self._exibir_opcoes()
            opcao = input("Escolha uma opcao: ").strip()

            if opcao == "1":
                self._cadastrar_cliente_ou_novo_ponto()
            elif opcao == "2":
                self._listar_clientes()
            elif opcao == "3":
                self._buscar_cliente()
            elif opcao == "4":
                self._editar_cliente()
            elif opcao == "5":
                self._excluir_cliente()
            elif opcao == "6":
                self._listar_ordens_servico()
            elif opcao == "0":
                print("Encerrando Nexus ERP Telecom.")
                break
            else:
                print("Opcao invalida.")

    def _exibir_opcoes(self):
        print("\n=== Nexus ERP Telecom ===")
        print("1 - Cadastrar cliente / novo ponto")
        print("2 - Listar clientes")
        print("3 - Buscar cliente por CPF/CNPJ")
        print("4 - Editar cliente")
        print("5 - Excluir cliente")
        print("6 - Listar ordens de servico")
        print("0 - Sair")

    def _cadastrar_cliente_ou_novo_ponto(self):
        try:
            cpf_cnpj = input("CPF/CNPJ: ")
            cliente = self.cliente_service.buscar_por_cpf_cnpj(cpf_cnpj)

            if cliente is None:
                self._cadastrar_cliente_novo(cpf_cnpj)
                return

            print(f"Cliente ja existe: {cliente}")
            if cliente.status_cliente == "ATIVO":
                resposta = input("Deseja cadastrar um novo ponto de instalacao? (s/n): ")
                if resposta.strip().lower() == "s":
                    self._cadastrar_novo_ponto(cpf_cnpj)
                else:
                    print("Operacao cancelada.")
                return

            if cliente.status_cliente == "INADIMPLENTE":
                print(
                    "Cliente esta inadimplente. Regularize a situacao antes de abrir novo ponto."
                )
                return

            if cliente.status_cliente == "INATIVO":
                print("Cliente esta inativo. Reative o cadastro antes de abrir novo ponto.")
                return

            print("Cliente precisa estar ATIVO para abrir novo ponto.")
        except Exception as erro:
            print(f"Erro ao cadastrar cliente / novo ponto: {erro}")

    def _cadastrar_cliente_novo(self, cpf_cnpj):
        nome_cliente = input("Nome: ")
        telefone = input("Telefone: ")
        planos = self._listar_planos_disponiveis()
        if not planos:
            return

        id_planos = input("Id do plano: ")
        end_instalacao = input("Endereco de instalacao: ")
        cliente, contrato, ordem_servico = self.cliente_service.cadastrar_cliente_com_ponto(
            nome_cliente,
            cpf_cnpj,
            telefone,
            id_planos,
            end_instalacao,
        )
        print(f"Cliente cadastrado: {cliente}")
        print(f"Contrato criado: {contrato}")
        print(f"Ordem de servico criada: {ordem_servico}")

    def _cadastrar_novo_ponto(self, cpf_cnpj):
        planos = self._listar_planos_disponiveis()
        if not planos:
            return

        id_planos = input("Id do plano: ")
        end_instalacao = input("Novo endereco de instalacao: ")
        cliente, contrato, ordem_servico = self.cliente_service.cadastrar_novo_ponto(
            cpf_cnpj,
            id_planos,
            end_instalacao,
        )
        print(f"Novo ponto criado para: {cliente.nome_cliente}")
        print(f"Contrato criado: {contrato}")
        print(f"Ordem de servico criada: {ordem_servico}")

    def _listar_planos_disponiveis(self):
        planos = self.cliente_service.listar_planos()
        if not planos:
            print("Nenhum plano cadastrado. Cadastre planos no banco antes de abrir contrato.")
            return []

        print("\nPlanos disponiveis:")
        for plano in planos:
            print(plano)
        return planos

    def _listar_clientes(self):
        try:
            clientes = self.cliente_service.listar_clientes()
            if not clientes:
                print("Nenhum cliente cadastrado.")
                return
            for cliente in clientes:
                print(cliente)
        except Exception as erro:
            print(f"Erro ao listar clientes: {erro}")

    def _buscar_cliente(self):
        try:
            cpf_cnpj = input("CPF/CNPJ: ")
            cliente = self.cliente_service.buscar_por_cpf_cnpj(cpf_cnpj)
            if cliente is None:
                print("Cliente nao encontrado.")
                return
            print(cliente)
        except Exception as erro:
            print(f"Erro ao buscar cliente: {erro}")

    def _editar_cliente(self):
        try:
            cpf_cnpj_atual = input("CPF/CNPJ atual: ")
            nome_cliente = input("Novo nome: ")
            novo_cpf_cnpj = input("Novo CPF/CNPJ: ")
            telefone = input("Novo telefone: ")
            status_cliente = input("Novo status (ATIVO, INATIVO ou INADIMPLENTE): ")
            cliente = self.cliente_service.editar_cliente(
                cpf_cnpj_atual,
                nome_cliente,
                novo_cpf_cnpj,
                telefone,
                status_cliente,
            )
            print(f"Cliente atualizado: {cliente}")
        except Exception as erro:
            print(f"Erro ao editar cliente: {erro}")

    def _excluir_cliente(self):
        try:
            cpf_cnpj = input("CPF/CNPJ do cliente: ")
            self.cliente_service.excluir_cliente(cpf_cnpj)
            print("Cliente excluido com sucesso.")
        except Exception as erro:
            print(f"Erro ao excluir cliente: {erro}")

    def _listar_ordens_servico(self):
        try:
            ordens_servico = self.cliente_service.listar_ordens_servico()
            if not ordens_servico:
                print("Nenhuma ordem de servico cadastrada.")
                return
            for ordem_servico in ordens_servico:
                print(ordem_servico)
        except Exception as erro:
            print(f"Erro ao listar ordens de servico: {erro}")
