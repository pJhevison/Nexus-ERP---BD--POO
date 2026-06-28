from database.connection import obter_conexao


class ContratoRepository:
    def salvar(self, contrato):
        sql = """
            INSERT INTO contrato (
                idcliente,
                idplanos,
                data_base,
                end_instalacao,
                tempo_contrato
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_contrato
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        contrato.idcliente,
                        contrato.idplanos,
                        contrato.data_base,
                        contrato.end_instalacao,
                        contrato.tempo_contrato,
                    ),
                )
                contrato.id_contrato = cursor.fetchone()[0]
            conexao.commit()
        return contrato
