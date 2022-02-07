from entidade.conta import Conta

class Movimentacao():

    def __init__(self, conta: Conta, valor: float, descricao: str=''):
        self.__conta = conta
        self.__valor = valor
        self.__descricao = descricao

    @property
    def conta(self):
      return self.__conta

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao