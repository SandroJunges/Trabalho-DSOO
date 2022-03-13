from persistencia.abstract_dao import DAO
from entidade.partida import Partida

class PartidaDAO(DAO):

    def __init__(self):
        super().__init__('partida.pkl')

    def add(self, partida: Partida):
        if self.__partida_valida(partida):
            super().add(partida.id_partida, partida)

    def remove(self, partida: Partida):
        if self.__partida_valida(partida):
            super().remove(partida.id_partida)

    def __partida_valida(self, partida):
        return (partida is not None) and (isinstance(partida, Partida)) and (isinstance(partida.id_partida, int))