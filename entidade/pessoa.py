from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa(ABC):
      @abstractmethod
      def __init__(self, codigo:str, nome: str, data_nascimento: datetime, cpf: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf

      @property
      def codigo(self):
        return self.__codigo

      @property
      def nome(self):
          return self.__nome

      @property
      def data_nascimento(self):
        return self.__data_nascimento

      @property
      def cpf(self):
        return self.__cpf

      @codigo.setter
      def codigo(self, codigo: str):
        self.__codigo = codigo

      @nome.setter
      def nome(self, nome: str):
        self.__nome = nome

      @data_nascimento.setter
      def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

      @cpf.setter
      def cpf(self, cpf: str):
        self.__cpf = cpf
