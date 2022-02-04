from abc import ABC, abstractmethod
from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, codigo:str, nome: str, data_nascimento, cpf: int, senha_cadastro: str):
        super().__init__(codigo, nome, data_nascimento, cpf)
        self.__senha_cadastro = senha_cadastro

    @property
    def senha_cadastro(self):
        return self.__senha_cadastro

    @senha_cadastro.setter
    def senha_cadastro(self, senha_cadastro: str):
        self.__senha_cadastro = senha_cadastro
