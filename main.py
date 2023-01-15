import random
from Entities.cliente import Cliente
from Entities.Enums.estado import Estado
from Entities.Enums.tipoVehiculo import TipoVehiculo
from Entities.tipoPlaza import TipoPlaza
from Entities.plaza import Plaza
from Entities.ocupa import Ocupa
from View.view import *
import pickle

numPlazas = 200
plazasTurismos = TipoPlaza(TipoVehiculo.TURISMO, 0.12, 70)
plazasMotos = TipoPlaza(TipoVehiculo.MOTOCICLETA, 0.08, 15)
plazasReducidas = TipoPlaza(TipoVehiculo.MOVILIDADREDUCIDA, 0.10, 15)
tiposPlazas = [plazasTurismos, plazasMotos, plazasReducidas]
plazas = []
preid = 0
seleccionMenu = 0;
seleccionSubmenu = 1;
seleccionSubmenu2 = 0;
for tipo in tiposPlazas:
    preid += 1000
    tipo.numPlazas = int(numPlazas * (tipo.porcentajePlazas / 100))
    for i in range(tipo.numPlazas):
        plazas.append(Plaza(preid + i, tipo))

printMenuRoles()
seleccionMenu = int(input())

if seleccionMenu == 1:

    while seleccionSubmenu != 0:

        printMenuUser()
        seleccionSubmenu = int(input())
        if seleccionSubmenu == 1:
            plazasDisponibles = [plaza for plaza in plazas if plaza.estado == Estado.LIBRE]
            disponiblesTurismo = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == "Turismos"])
            disponiblesMotos = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == "Motocicletas"])
            disponiblesReducidas = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == "Movilidad reducida"])
            if len(plazasDisponibles) > 0:
                print(f"Hay un total de {len(plazasDisponibles)}")
                print(f"{disponiblesTurismo} plazas disponibles para turismos." if disponiblesTurismo > 0 else "Ninguna plaza disponible para turismos")
                print(f"{disponiblesMotos} plazas disponibles para motos." if disponiblesMotos > 0 else "Ninguna plaza disponible para motos")
                print(f"{disponiblesReducidas} plazas disponibles para vehículos para personas con movilidad reducidad." if disponiblesReducidas > 0 else "Ninguna plaza disponible para vehículos para personas con movilidad reducidad")
                print()
                printMenuTipoVehiculo()
                seleccionSubmenu2 = int(input())
                if seleccionSubmenu2 == 1 and disponiblesTurismo > 0:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.TURISMO][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula, TipoVehiculo.TURISMO), random.randint(100000, 999999))
                    print(plazaOcupada)
                elif seleccionSubmenu2 == 2:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOTOCICLETA][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula, TipoVehiculo.MOTOCICLETA),random.randint(100000, 999999))
                    print(plazaOcupada)
                elif seleccionSubmenu2 == 3:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOVILIDADREDUCIDA][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula, TipoVehiculo.MOVILIDADREDUCIDA),random.randint(100000, 999999))
                    print(plazaOcupada)
            else:
                print("No hay plazas disponibles")
        elif seleccionSubmenu == 2:
            pass
        elif seleccionSubmenu == 3:
            pass
        elif seleccionSubmenu == 4:
            pass
        elif seleccionSubmenu == 0:
            pass
elif seleccionMenu == 2:
    pass