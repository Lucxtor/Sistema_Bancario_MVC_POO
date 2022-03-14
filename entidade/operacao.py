from datetime import datetime
from entidade.conta import Conta
from entidade.movimentacao import Movimentacao

class Operacao():

    def __init__(self, codigo: int, tipo: str, data_operacao: datetime, chave: str = ""):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__data_operacao = data_operacao
        self.__chave = chave
        self.__movimentacao = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data_operacao(self):
      return self.__data_operacao

    @property
    def chave(self):
        return self.__chave

    @property
    def movimentacao(self):
        return self.__movimentacao

    def adicionar_movimentacao(self, conta: Conta, valor: float, desc: str=""):
        movimentacao = Movimentacao(conta, valor, desc)
        self.__movimentacao.append(movimentacao)