import random

from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.Enums.estado import Estado
from Entities.Enums.tipoVehiculo import TipoVehiculo
from Entities.ocupa import Ocupa
from Entities.plaza import Plaza
from Entities.tipoPlaza import TipoPlaza
from View.view import *
import pickle
from datetime import datetime, timedelta
from Services.services import initConfig

archivoPlazas = open("Persistence/plazas.pickle", "rb")
archivoTipos = open("Persistence/tipos.pickle", "rb")
archivoClientes = open("Persistence/clientes.pickle", "rb")
archivoOcupa = open("Persistence/ocupas.pickle", "rb")

plazas = pickle.load(archivoPlazas)
tipos = pickle.load(archivoTipos)
clientes = pickle.load(archivoClientes)
ocupas = pickle.load(archivoOcupa)

archivoPlazas.close()
archivoOcupa.close()
archivoClientes.close()
archivoTipos.close()

seleccionMenu = 1;
seleccionSubmenu = 1;
seleccionSubmenu2 = 0;

while seleccionMenu != 0:

    seleccionSubmenu = 1;
    seleccionSubmenu2 = 1;
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
                print("Bienvenido de nuevo, por favor, introduzca su dni:")
                dni = input()
                print("Introduzca su matrícula")
                matricula = input()
                try:
                    cliente = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.matricula == matricula and cliente.dni == dni)
                    print(f"Puede proceder a estacionar su vehiculo, su plaza es la {cliente.plaza.id}")
                    cliente.plaza.estado = Estado.ABONOOCUPADA
                    ocupas.append(Ocupa(cliente.plaza, cliente, cliente.pin, costeTotal=0))
                except:
                    print("Ha habido un error en los datos")
            elif seleccionSubmenu == 4:
                dni = input("Bienvenido de nuevo, por favor, introduzca su dni: ")
                matricula = input("Introduzca su matrícula: ")
                pin = input("Introduzca su pin: ")
                try:
                    ocupa = next(ocupa for ocupa in ocupas if ocupa.activo and ocupa.pin == int(pin) and ocupa.cliente.matricula == matricula and ocupa.cliente.dni == dni)
                    print("Puede proceder a sacar su vehiculo")
                    cliente.plaza.estado = Estado.ABONOLIBRE
                    ocupa.activo = False
                except:
                    print("Ha habido un error en los datos")
            elif seleccionSubmenu == 0:
                pass

    elif seleccionMenu == 2:

        while seleccionSubmenu != 0:

            printMenuAdmin()
            seleccionSubmenu = int(input())

            if seleccionSubmenu == 1:
                plazasDisponibles = len([plaza for plaza in plazas if plaza.estado == Estado.LIBRE])
                porcentajeOcupacion = (200 - plazasDisponibles) / (200/100)

                print(f"Actualmente hay {plazasDisponibles} plazas disponibles, el porcentaje de ocupación es del {porcentajeOcupacion}%")
                for plaza in plazas:
                    print(f"Plaza id {plaza.id} - {plaza.estado}")
            elif seleccionSubmenu == 2:
                print("Introduzca la fecha a partir de la que consultar.")
                anioInicio = input("Año: ")
                mesInicio = input("Mes: ")
                diaInicio = input("Día: ")
                horaInicio = input("Hora: ")
                minutosInicio = input("Minutos: ")
                inicio = datetime(int(anioInicio), int(mesInicio), int(diaInicio), int(horaInicio), int(minutosInicio))

                print("Introduzca la fecha hasta la que consultar.")
                anioFin = input("Año: ")
                mesFin = input("Mes: ")
                diaFin = input("Día: ")
                horaFin = input("Hora: ")
                minutosFin = input("Minutos: ")
                fin = datetime(int(anioFin), int(mesFin), int(diaFin), int(horaFin), int(minutosFin))

                cobros = [ocupa for ocupa in ocupas if ocupa.costeTotal > 0 and ocupa.salida < fin and ocupa.salida > inicio]
                for cobro in cobros:
                    print(f"Plaza {cobro.plaza.id}({cobro.plaza.tipoPlaza.tipo}) - {cobro.entrada} hasta {cobro.salida} - Total = {cobro.costeTotal} €")
            elif seleccionSubmenu == 3:
                pass
            elif seleccionSubmenu == 4:
                pass
            elif seleccionSubmenu == 5:
                pass