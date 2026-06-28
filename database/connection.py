import os
from pathlib import Path

import psycopg2


def obter_conexao():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "nexus_erp"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
    )


def criar_tabelas():
    caminho_schema = Path(__file__).with_name("schema.sql")
    schema_sql = caminho_schema.read_text(encoding="utf-8")

    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(schema_sql)
        conexao.commit()
