import os

from database.connection import criar_tabelas
from repositories.cliente_repository import ClienteRepository
from services.cliente_service import ClienteService
from ui.menu import MenuPrincipal


def configurar_banco():
    os.environ.setdefault("DB_NAME", "nexus_erp")
    os.environ.setdefault("DB_USER", "postgres")
    os.environ.setdefault("DB_HOST", "localhost")
    os.environ.setdefault("DB_PORT", "5432")

    if not os.getenv("DB_PASSWORD"):
        senha = input("Senha do PostgreSQL: ").strip()
        os.environ["DB_PASSWORD"] = senha


def main():
    configurar_banco()

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