from models.cliente import Cliente
from models.funcionario import Funcionario


class MenuPrincipal:
    def __init__(self, cliente_service):
        self.cliente_service = cliente_service

    def executar(self):
        while True:
            self._exibir_opcoes()
            opcao = input("Escolha uma opcao: ").strip()

            if opcao == "1":
                self._cadastrar_cliente()
            elif opcao == "2":
                self._listar_clientes()
            elif opcao == "3":
                self._buscar_cliente()
            elif opcao == "4":
                self._editar_cliente()
            elif opcao == "5":
                self._excluir_cliente()
            elif opcao == "6":
                self._demonstrar_polimorfismo()
            elif opcao == "0":
                print("Encerrando Nexus ERP Telecom.")
                break
            else:
                print("Opcao invalida.")

    def _exibir_opcoes(self):
        print("\n=== Nexus ERP Telecom ===")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente por CPF/CNPJ")
        print("4 - Editar cliente")
        print("5 - Excluir cliente")
        print("6 - Demonstrar polimorfismo")
        print("0 - Sair")

    def _cadastrar_cliente(self):
        try:
            nome_cliente = input("Nome: ")
            cpf_cnpj = input("CPF/CNPJ: ")
            telefone = input("Telefone: ")
            status_cliente = input("Status: ")
            cliente = self.cliente_service.cadastrar_cliente(
                nome_cliente,
                cpf_cnpj,
                telefone,
                status_cliente,
            )
            print(f"Cliente cadastrado: {cliente}")
        except Exception as erro:
            print(f"Erro ao cadastrar cliente: {erro}")

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
            status_cliente = input("Novo status: ")
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

    def _demonstrar_polimorfismo(self):
        pessoas = [
            Cliente("Maria Silva", "12345678900", "92999990000", "Ativo"),
            Funcionario("Joao Souza", "Tecnico de campo"),
        ]

        print("Mesmo metodo chamado em objetos Cliente e Funcionario:")
        for pessoa in pessoas:
            print(pessoa.obter_identificacao())
