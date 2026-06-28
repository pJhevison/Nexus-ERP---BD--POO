class Contrato:
    def __init__(
        self,
        idcliente,
        idplanos,
        data_base,
        end_instalacao,
        tempo_contrato,
        id_contrato=None,
    ):
        self.id_contrato = id_contrato
        self.idcliente = idcliente
        self.idplanos = idplanos
        self.data_base = data_base
        self.end_instalacao = end_instalacao
        self.tempo_contrato = tempo_contrato

    def alterar_endereco_instalacao(self, end_instalacao):
        if not end_instalacao or not end_instalacao.strip():
            raise ValueError("Endereco de instalacao nao pode ser vazio.")
        self.end_instalacao = end_instalacao.strip()

    def __str__(self):
        return (
            f"Contrato(id={self.id_contrato}, cliente={self.idcliente}, plano={self.idplanos}, "
            f"data_base={self.data_base}, tempo={self.tempo_contrato})"
        )
