import pickle

from Entities.Enums.estado import Estado
from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.ocupa import Ocupa
from Entities.tipoPlaza import TipoPlaza
from Entities.plaza import Plaza
from Entities.Enums.tipoVehiculo import TipoVehiculo
from datetime import datetime, timedelta
def initConfig():
    numPlazas = 200
    plazasTurismos = TipoPlaza(TipoVehiculo.TURISMO, 0.12, 70)
    plazasMotos = TipoPlaza(TipoVehiculo.MOTOCICLETA, 0.08, 15)
    plazasReducidas = TipoPlaza(TipoVehiculo.MOVILIDADREDUCIDA, 0.10, 15)
    tiposPlazas = [plazasTurismos, plazasMotos, plazasReducidas]
    plazas = []
    ocupas = []
    clientes = []
    preid = 0

    archivoTipos = open("../Persistence/tipos.pickle", "wb")
    pickle.dump(tiposPlazas, archivoTipos)
    archivoTipos.close()

    for tipo in tiposPlazas:
        preid += 1000
        tipo.numPlazas = int(numPlazas * (tipo.porcentajePlazas / 100))
        for i in range(tipo.numPlazas):
            plazas.append(Plaza(preid + i, tipo))

    cNormal = Cliente("123D", TipoVehiculo.TURISMO)
    cAbonado = Abonado("234F", TipoVehiculo.TURISMO, "54219289D", "Álvaro", "Franco", "alvaro@ejemplo", "2222222222", "semestral", datetime.now() - timedelta(days = 30), datetime.now() + timedelta(days = 150), True, plazas[3], 111111)
    clientes.append(cNormal)
    clientes.append(cAbonado)
    plazas[3].estado = Estado.ABONOLIBRE

    entrada = datetime.now() - timedelta(days=2, hours=1, minutes=15)
    salida = datetime.now() - timedelta(days=2)
    tiempoEstacionado = divmod((salida - entrada).total_seconds(), 60)[0]
    ocupacion1 = Ocupa(plazas[3], cAbonado, cAbonado.pin, datetime.now() - timedelta(days = 10), timedelta(days = 8), 0, False)
    ocupacion2 = Ocupa(plazas[0], cNormal, 763248, entrada, salida, tiempoEstacionado * plazas[0].tipoPlaza.tarifa, False)
    ocupas.append(ocupacion1)
    ocupas.append(ocupacion2)

    archivoPlazas = open("../Persistence/plazas.pickle", "wb")
    pickle.dump(plazas, archivoPlazas)
    archivoPlazas.close()

    archivoOcupa = open("../Persistence/ocupas.pickle", "wb")
    pickle.dump(ocupas, archivoOcupa)
    archivoOcupa.close()

    archivoClientes = open("../Persistence/clientes.pickle", "wb")
    pickle.dump(clientes, archivoClientes)
    archivoClientes.close()