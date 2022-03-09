from entidade.cliente import Cliente

class Conta():
    #criar constantes para tipos de contas
    def __init__(self, codigo:int, titular: Cliente, tipo: int, senha_operacoes:str):
        #Regra de Negócio: Todas as operações ocorrerão na mesma agência
        self.__agencia = "1234"
        self.__codigo = codigo
        self.__saldo = 0.00
        self.__titular = titular
        self.__tipo = tipo
        self.__senha_operacoes = senha_operacoes
        self.__chaves_PIX = []

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

    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    @property
    def senha_operacoes(self):
        return self.__senha_operacoes

    @senha_operacoes.setter
    def senha_operacoes(self, senha_operacoes: str):
        self.__senha_operacoes = senha_operacoes

    @property
    def chaves_PIX(self):
        return self.__chaves_PIX

    @chaves_PIX.setter
    def chaves_PIX(self, chaves_PIX):
        self.__chaves_PIX = chaves_PIX

    def adicionar_chave_PIX(self, chave_PIX: str):
        self.__chaves_PIX.append(chave_PIX)

