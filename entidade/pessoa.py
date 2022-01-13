from abc import ABC, abstractmethod

class Pessoa(ABC):
      @abstractmethod
      def __init__(self, codigo:str, nome: str, telefone: str, cpf: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf

      @property
      def codigo(self):
        return self.__codigo

      @property
      def nome(self):
          return self.__nome

      @property
      def telefone(self):
        return self.__telefone

      @property
      def cpf(self):
        return self.__cpf

      @codigo.setter
      def codigo(self, codigo: str):
        self.__codigo = codigo

      @nome.setter
      def nome(self, nome: str):
        self.__nome = nome

      @telefone.setter
      def telefone(self, telefone: str):
        self.__telefone = telefone

      @cpf.setter
      def cpf(self, cpf: str):
        self.__cpf = cpf
