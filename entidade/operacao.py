from datetime import datetime
from entidade.conta import Conta

class Operacao():

    def __init__(self, conta: Conta, tipo: str, data_operacao: datetime, valor: float, conta_destino: Conta, chave: str):
        self.__conta = conta
        self.__tipo = tipo
        self.__data_operacao = data_operacao
        self.__valor = valor
        self.__conta_destino = conta_destino
        self.__chave = chave

    @property
    def conta(self):
      return self.__conta

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data_operacao(self):
      return self.__data_operacao

    @property
    def valor(self):
        return self.__valor

    @property
    def conta_destino(self):
      return self.__conta_destino

    @property
    def chave(self):
        return self.__chave