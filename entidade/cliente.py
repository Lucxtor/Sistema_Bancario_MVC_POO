from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, codigo:str, nome: str, data_nascimento, cpf: int, senha_operacoes: str):
        super().__init__(codigo, nome, data_nascimento, cpf)
        self.__senha_operacoes = senha_operacoes

    @property
    def senha_operacoes(self):
        return self.__senha_operacoes

    @senha_operacoes.setter
    def senha_operacoes(self, senha_operacoes: str):
        self.__senha_operacoes = senha_operacoes
