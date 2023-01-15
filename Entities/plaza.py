from Entities.Enums.estado import Estado

class Plaza:

    def __init__(self, id, tipoPlaza, estado = Estado.LIBRE):
        self.__id = id;
        self.__tipoPlaza = tipoPlaza
        self.__estado = estado

    def __str__(self):
        return "Plaza con id " + self.id + " reservada para " + self.tipoPlaza.tipo + ", actualmente se encuentra " + self.estado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tipoPlaza(self):
        return self.__tipoPlaza

    @tipoPlaza.setter
    def tipoPlaza(self, tipoPlaza):
        self.__tipoPlaza = tipoPlaza

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado
