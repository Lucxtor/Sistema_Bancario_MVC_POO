from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, codigo:str, nome: str, telefone: str, cpf: int, senha_contas: str):
        super().__init__(codigo, nome, telefone, cpf)
        self.__senha_contas = senha_contas

    @property
    def senha_contas(self):
        return self.__senha_contas

    @senha_contas.setter
    def senha_contas(self, senha_contas: str):
        self.__senha_contas = senha_contas
