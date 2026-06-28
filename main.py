from database.connection import criar_tabelas
from repositories.cliente_repository import ClienteRepository
from services.cliente_service import ClienteService
from ui.menu import MenuPrincipal


def main():
    try:
        criar_tabelas()
        print("Tabelas verificadas/criadas com sucesso.")
    except Exception as erro:
        print("Nao foi possivel conectar/criar as tabelas no PostgreSQL.")
        print(f"Detalhes: {erro}")
        print("Confira as variaveis DB_NAME, DB_USER, DB_PASSWORD, DB_HOST e DB_PORT.")
        return

    cliente_repository = ClienteRepository()
    cliente_service = ClienteService(cliente_repository)
    menu = MenuPrincipal(cliente_service)
    menu.executar()


if __name__ == "__main__":
    main()
