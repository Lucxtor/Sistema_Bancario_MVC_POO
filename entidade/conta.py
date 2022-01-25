class Conta():
    def __init__(self, codigo:int, cpf_titular: int, tipo: int, senha_conta:str):
        self.__agencia = "1234"
        self.__codigo = codigo
        self.__saldo = 0.00
        self.__cpf_titular = cpf_titular
        self.__tipo = tipo
        self.__extrato = []
        self.__senha_conta = senha_conta

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
    def cpf_titular(self):
        return self.__cpf_titular

    @property
    def tipo(self):
        return self.__tipo

    @property
    def extrato(self):
        return self.__extrato

    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    @property
    def senha_conta(self):
        return self.__senha_conta

    @senha_conta.setter
    def senha_conta(self, senha_conta: str):
        self.__senha_conta = senha_conta


    def adiciona_operacao(self, operacao):
        self.__extrato.append(operacao)

