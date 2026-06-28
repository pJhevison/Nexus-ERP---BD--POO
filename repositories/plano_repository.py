from database.connection import obter_conexao
from models.plano import Plano


class PlanoRepository:
    def listar(self):
        sql = """
            SELECT id_planos, descricao_planos, velocidade_franquia, valor_mensal
            FROM planos
            ORDER BY id_planos
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql)
                linhas = cursor.fetchall()
        return [self._mapear_plano(linha) for linha in linhas]

    def buscar_por_id(self, id_planos):
        sql = """
            SELECT id_planos, descricao_planos, velocidade_franquia, valor_mensal
            FROM planos
            WHERE id_planos = %s
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, (id_planos,))
                linha = cursor.fetchone()
        if linha is None:
            return None
        return self._mapear_plano(linha)

    def seed_planos_padrao(self):
        planos_padrao = [
            ("Fibra 300 Mega", "300 Mbps", 99.90),
            ("Fibra 500 Mega", "500 Mbps", 129.90),
            ("Fibra 1 Giga", "1 Gbps", 199.90),
        ]

        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM planos")
                total = cursor.fetchone()[0]
                if total > 0:
                    return 0

                cursor.executemany(
                    """
                    INSERT INTO planos (descricao_planos, velocidade_franquia, valor_mensal)
                    VALUES (%s, %s, %s)
                    """,
                    planos_padrao,
                )
            conexao.commit()
        return len(planos_padrao)

    def _mapear_plano(self, linha):
        return Plano(
            id_planos=linha[0],
            descricao_planos=linha[1],
            velocidade_franquia=linha[2],
            valor_mensal=linha[3],
        )
