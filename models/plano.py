class Plano:
    def __init__(self, descricao_planos, velocidade_franquia, valor_mensal, id_planos=None):
        self.id_planos = id_planos
        self.descricao_planos = descricao_planos
        self.velocidade_franquia = velocidade_franquia
        self.__valor_mensal = None
        self.valor_mensal = valor_mensal

    @property
    def valor_mensal(self):
        return self.__valor_mensal

    @valor_mensal.setter
    def valor_mensal(self, valor):
        if valor <= 0:
            raise ValueError("Valor mensal deve ser maior que zero.")
        self.__valor_mensal = valor

    def reajustar_valor(self, novo_valor):
        self.valor_mensal = novo_valor

    def __str__(self):
        return (
            f"Plano(id={self.id_planos}, descricao={self.descricao_planos}, "
            f"velocidade_franquia={self.velocidade_franquia}, valor={self.valor_mensal})"
        )
