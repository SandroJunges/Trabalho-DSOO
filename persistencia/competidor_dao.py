from persistencia.abstract_dao import DAO
from entidade.competidor import Competidor

class CompetidorDAO(DAO):

    def __init__(self):
        super().__init__('competidor.pkl')

    def add(self, competidor: Competidor):
        if self.__competidor_valido(competidor):
            super().add(competidor.id_competidor, competidor)
    
    def remove(self, competidor: Competidor):
        if self.__competidor_valido(competidor):
            super().remove(competidor.id_competidor)

    def __competidor_valido(self, competidor):
        return (competidor is not None) and (isinstance(competidor, Competidor)) and (isinstance(competidor.id_competidor, int))