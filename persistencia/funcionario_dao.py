from abc import ABC, abstractmethod
from persistencia.dao import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')

    def add(self, funcionario: Funcionario):
        if (isinstance(funcionario.codigo, int)) and (funcionario is not None) and isinstance(funcionario, Funcionario):
            super().add(funcionario.codigo, funcionario)

    def get(self, key: int):
        if super().valida_chave_int(key):
            return super().get(key)

    def remove(self, key: int):
        if super().valida_chave_int(key):
            return super().remove(key)
