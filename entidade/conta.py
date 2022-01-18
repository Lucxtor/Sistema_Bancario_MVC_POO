from cliente import Cliente

class Conta():
    def __init__(self, codigo:int, titular: Cliente, tipo: str):
        self.__agencia = "1234"
        self.__codigo = codigo
        self.__saldo = 0.00
        self.__titular = titular
        self.__tipo = tipo
        self.__extrato = []

    @property
    def agencia(self):
      return self.__agencia

    @property
    def codigo(self):
        return self.__codigo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def tipo(self):
        return self.__tipo

    @property
    def extrato(self):
        return self.__extrato

    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    def adiciona_operacao(self, operacao):
        self.__extrato.append(operacao)

