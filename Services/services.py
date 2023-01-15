import pickle
from Entities.tipoPlaza import TipoPlaza
from Entities.plaza import Plaza
from Entities.Enums.tipoVehiculo import TipoVehiculo
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

    archivoTipos = open("../Persistence/tipos.txt", "wb")
    pickle.dump(tiposPlazas, archivoTipos)
    archivoTipos.close()

    for tipo in tiposPlazas:
        preid += 1000
        tipo.numPlazas = int(numPlazas * (tipo.porcentajePlazas / 100))
        for i in range(tipo.numPlazas):
            plazas.append(Plaza(preid + i, tipo))

    archivoPlazas = open("../Persistence/plazas.txt", "wb")
    pickle.dump(plazas, archivoPlazas)
    archivoPlazas.close()

    archivoOcupa = open("../Persistence/ocupas.txt", "wb")
    pickle.dump(ocupas, archivoOcupa)
    archivoOcupa.close()

    archivoClientes = open("../Persistence/clientes.txt", "wb")
    pickle.dump(clientes, archivoClientes)
    archivoClientes.close()