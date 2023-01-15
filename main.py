import random
from Entities.cliente import Cliente
from Entities.Enums.estado import Estado
from Entities.Enums.tipoVehiculo import TipoVehiculo
from Entities.ocupa import Ocupa
from View.view import *
import pickle
from datetime import datetime

archivoPlazas = open("Persistence/plazas.txt", "rb")
archivoTipos = open("Persistence/tipos.txt", "rb")
archivoClientes = open("Persistence/clientes.txt", "rb")
archivoOcupa = open("Persistence/ocupas.txt", "rb")

plazas = pickle.load(archivoPlazas)
tipos = pickle.load(archivoTipos)
clientes = pickle.load(archivoClientes)
ocupas = pickle.load(archivoOcupa)

archivoPlazas.close()
archivoOcupa.close()
archivoClientes.close()
archivoTipos.close()

seleccionMenu = 0;
seleccionSubmenu = 1;
seleccionSubmenu2 = 0;

printMenuRoles()
seleccionMenu = int(input())

if seleccionMenu == 1:

    while seleccionSubmenu != 0:

        printMenuUser()
        seleccionSubmenu = int(input())
        if seleccionSubmenu == 1:
            plazasDisponibles = [plaza for plaza in plazas if plaza.estado == Estado.LIBRE]
            disponiblesTurismo = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.TURISMO])
            disponiblesMotos = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOTOCICLETA])
            disponiblesReducidas = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOVILIDADREDUCIDA])
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
                    ocupas.append(plazaOcupada)
                    print(f"Matricula: {plazaOcupada.cliente.matricula}, Id: {plazaOcupada.plaza.id}, Pin: {plazaOcupada.pin}")
                elif seleccionSubmenu2 == 2:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOTOCICLETA][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula, TipoVehiculo.MOTOCICLETA),random.randint(100000, 999999))
                    ocupas.append(plazaOcupada)
                    print(f"Matricula: {plazaOcupada.cliente.matricula}, Id: {plazaOcupada.plaza.id}, Pin: {plazaOcupada.pin}")
                elif seleccionSubmenu2 == 3:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOVILIDADREDUCIDA][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula, TipoVehiculo.MOVILIDADREDUCIDA),random.randint(100000, 999999))
                    ocupas.append(plazaOcupada)
                    print(f"Matricula: {plazaOcupada.cliente.matricula}, Id: {plazaOcupada.plaza.id}, Pin: {plazaOcupada.pin}")
            else:
                print("No hay plazas disponibles")
        elif seleccionSubmenu == 2:
            print("Por favor introduzca su matrícula:")
            matricula = input()
            print("Introduzca el número de la plaza de aparcamiento:")
            nPlaza = int(input())
            print("Por último, introduzca el pin que se le proporcionó al estacionar:")
            pin = int(input())
            try:
                ocupa = next(ocupa for ocupa in ocupas if ocupa.plaza.id == nPlaza and ocupa.cliente.matricula == matricula and ocupa.pin == pin)
                ocupa.activo = False
                ocupa.salida = datetime.now()
                tiempoEstacionado = divmod((ocupa.salida - ocupa.entrada).total_seconds(), 60)[0]
                ocupa.costeTotal = ocupa.plaza.tipoPlaza.tarifa * tiempoEstacionado
                print(f"El coste total ha sido de {ocupa.costeTotal}")
            except:
                print("Los datos no coinciden")
        elif seleccionSubmenu == 3:
            pass
        elif seleccionSubmenu == 4:
            pass
        elif seleccionSubmenu == 0:
            pass
elif seleccionMenu == 2:
    pass