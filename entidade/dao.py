from abc import ABC, abstractmethod
import pickle

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=""):
        self.datasource = datasource
        self.cache = ()
        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    def __dump(self):
        pickle.dump(self. cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    def valida_chave_int(self, key):
        return isinstance(key, int)
