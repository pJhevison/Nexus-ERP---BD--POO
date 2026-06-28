from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def obter_identificacao(self):
        pass
