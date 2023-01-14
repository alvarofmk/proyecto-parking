class TipoPlaza:

    def __init__(self, tipo, tarifa, porcentajePlazas, numPlazas=None):
        self.__numPlazas = numPlazas
        self.__tipo = tipo
        self.__tarifa = tarifa
        self.__porcentajePlazas = porcentajePlazas

    def __str__(self):
        return "Plazas reservadas para " + self.__tipo + " con tarificación por minuto de " + self.__tarifa

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

    @property
    def porcentajePlazas(self):
        return self.__porcentajePlazas

    @porcentajePlazas.setter
    def porcentajePlazas(self, porcentajePlazas):
        self.__porcentajePlazas = porcentajePlazas

    @property
    def numPlazas(self):
        return self.__numPlazas

    @numPlazas.setter
    def numPlazas(self, numPlazas):
        self.__numPlazas = numPlazas