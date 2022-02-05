from entidade.conta import Conta

class Movimentacao():

    def __init__(self, conta: Conta, valor: float):
        self.__conta = conta
        self.__valor = valor

    @property
    def conta(self):
      return self.__conta

    @property
    def valor(self):
        return self.__valor