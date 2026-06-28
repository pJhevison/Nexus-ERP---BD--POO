from database.connection import obter_conexao
from models.ordem_servico import OrdemServico


class OrdemServicoRepository:
    def salvar(self, ordem_servico):
        sql = """
            INSERT INTO os (
                idcontrato,
                data_abertura,
                data_resolucao,
                status,
                desc_os,
                tipo_os
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_os
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    sql,
                    (
                        ordem_servico.idcontrato,
                        ordem_servico.data_abertura,
                        ordem_servico.data_resolucao,
                        ordem_servico.status,
                        ordem_servico.desc_os,
                        ordem_servico.tipo_os,
                    ),
                )
                ordem_servico.id_os = cursor.fetchone()[0]
            conexao.commit()
        return ordem_servico

    def listar(self):
        sql = """
            SELECT id_os, idcontrato, data_abertura, data_resolucao, status, desc_os, tipo_os
            FROM os
            ORDER BY id_os
        """
        with obter_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql)
                linhas = cursor.fetchall()
        return [self._mapear_ordem_servico(linha) for linha in linhas]

    def _mapear_ordem_servico(self, linha):
        return OrdemServico(
            id_os=linha[0],
            idcontrato=linha[1],
            data_abertura=linha[2],
            data_resolucao=linha[3],
            status=linha[4],
            desc_os=linha[5],
            tipo_os=linha[6],
        )
