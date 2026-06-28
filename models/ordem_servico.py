class OrdemServico:
    def __init__(
        self,
        idcontrato,
        data_abertura,
        data_resolucao,
        status,
        desc_os,
        tipo_os,
        id_os=None,
    ):
        self.id_os = id_os
        self.idcontrato = idcontrato
        self.data_abertura = data_abertura
        self.data_resolucao = data_resolucao
        self.status = status
        self.desc_os = desc_os
        self.tipo_os = tipo_os

    def resolver(self, data_resolucao):
        self.data_resolucao = data_resolucao
        self.status = "Resolvida"

    def __str__(self):
        return (
            f"OrdemServico(id={self.id_os}, contrato={self.idcontrato}, "
            f"status={self.status}, tipo={self.tipo_os})"
        )
