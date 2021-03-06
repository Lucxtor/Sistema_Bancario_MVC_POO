from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, codigo:str, nome: str, data_nascimento, cpf: int, numero_CTPS: str, senha_funcionario: str):
        super().__init__(codigo, nome, data_nascimento, cpf)
        self.__numero_CTPS = numero_CTPS
        self.__senha_funcionario = senha_funcionario

    @property
    def numero_CTPS(self):
        return self.__numero_CTPS

    @property
    def senha_funcionario(self):
        return self.__senha_funcionario

    @numero_CTPS.setter
    def numero_CTPS(self, numero_CTPS: str):
        self.__numero_CTPS = numero_CTPS

    @senha_funcionario.setter
    def senha_funcionario(self, senha_funcionario: str):
        self.__senha_funcionario = senha_funcionario
