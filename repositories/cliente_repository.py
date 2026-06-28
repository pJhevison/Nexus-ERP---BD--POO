from database.connection import obter_conexao
from models.cliente import Cliente


class ClienteRepository:
    def salvar(self, cliente):
        sql = """
            INSERT INTO cliente (nome_cliente, cpf_cnpj, telefone, status_cliente)
            VALUES (%s, %s, %s, %s)
            RETURNING id_cliente
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        cliente.nome_cliente,
                        cliente.cpf_cnpj,
                        cliente.telefone,
                        cliente.status_cliente,
                    ),
                )
                cliente.id_cliente = cursor.fetchone()[0]
            conexao.commit()
        return cliente

    def listar(self):
        sql = """
            SELECT id_cliente, nome_cliente, cpf_cnpj, telefone, status_cliente
            FROM cliente
            ORDER BY id_cliente
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql)
                linhas = cursor.fetchall()
        return [self._mapear_cliente(linha) for linha in linhas]

    def buscar_por_cpf_cnpj(self, cpf_cnpj):
        sql = """
            SELECT id_cliente, nome_cliente, cpf_cnpj, telefone, status_cliente
            FROM cliente
            WHERE cpf_cnpj = %s
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, (cpf_cnpj,))
                linha = cursor.fetchone()
        if linha is None:
            return None
        return self._mapear_cliente(linha)

    def atualizar(self, cliente):
        sql = """
            UPDATE cliente
            SET nome_cliente = %s,
                cpf_cnpj = %s,
                telefone = %s,
                status_cliente = %s
            WHERE id_cliente = %s
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        cliente.nome_cliente,
                        cliente.cpf_cnpj,
                        cliente.telefone,
                        cliente.status_cliente,
                        cliente.id_cliente,
                    ),
                )
                linhas_afetadas = cursor.rowcount
            conexao.commit()
        return linhas_afetadas > 0

    def excluir_por_id(self, id_cliente):
        sql = "DELETE FROM cliente WHERE id_cliente = %s"
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, (id_cliente,))
                linhas_afetadas = cursor.rowcount
            conexao.commit()
        return linhas_afetadas > 0

    def _mapear_cliente(self, linha):
        return Cliente(
            id_cliente=linha[0],
            nome_cliente=linha[1],
            cpf_cnpj=linha[2],
            telefone=linha[3],
            status_cliente=linha[4],
        )
