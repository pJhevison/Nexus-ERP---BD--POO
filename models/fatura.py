class Fatura:
    def __init__(
        self,
        idcontrato,
        valor_fatura,
        data_emissao,
        data_vencimento,
        id_fatura=None,
    ):
        self.id_fatura = id_fatura
        self.idcontrato = idcontrato
        self.__valor_fatura = None
        self.valor_fatura = valor_fatura
        self.data_emissao = data_emissao
        self.data_vencimento = data_vencimento

    @property
    def valor_fatura(self):
        return self.__valor_fatura

    @valor_fatura.setter
    def valor_fatura(self, valor):
        if valor <= 0:
            raise ValueError("Valor da fatura deve ser maior que zero.")
        self.__valor_fatura = valor

    def alterar_valor(self, valor_fatura):
        self.valor_fatura = valor_fatura

    def __str__(self):
        return (
            f"Fatura(id={self.id_fatura}, contrato={self.idcontrato}, "
            f"valor={self.valor_fatura}, vencimento={self.data_vencimento})"
        )
