import random
import time
from Entities.abonado import Abonado
from Entities.cliente import Cliente
from Entities.Enums.estado import Estado
from Entities.Enums.tipoVehiculo import TipoVehiculo
from Entities.ocupa import Ocupa
from View.view import *
import pickle
from datetime import datetime, timedelta
from threading import Thread

archivoAbonos = open("Persistence/tiposAbonos.pickle", "rb")
archivoPlazas = open("Persistence/plazas.pickle", "rb")
archivoTipos = open("Persistence/tipos.pickle", "rb")
archivoClientes = open("Persistence/clientes.pickle", "rb")
archivoOcupa = open("Persistence/ocupas.pickle", "rb")

abonos = pickle.load(archivoAbonos)
plazas = pickle.load(archivoPlazas)
tipos = pickle.load(archivoTipos)
clientes = pickle.load(archivoClientes)
ocupas = pickle.load(archivoOcupa)

archivoAbonos.close()
archivoPlazas.close()
archivoOcupa.close()
archivoClientes.close()
archivoTipos.close()
def persistCollections():
    on = True
    while on:
        i=0
        while i < 300:
            if mainThread.is_alive():
                time.sleep(1)
                i += 1
            else:
                i = 300
                on = False

        open("Persistence/tiposAbonos.pickle", "w").close()
        open("Persistence/ocupas.pickle", "w").close()
        open("Persistence/plazas.pickle", "w").close()
        open("Persistence/clientes.pickle", "w").close()
        open("Persistence/tipos.pickle", "w").close()

        archivoAbonos = open("Persistence/tiposAbonos.pickle", "wb")
        pickle.dump(abonos, archivoAbonos)
        archivoAbonos.close()
        archivoTipos = open("Persistence/tipos.pickle", "wb")
        pickle.dump(tipos, archivoTipos)
        archivoTipos.close()
        archivoPlazas = open("Persistence/plazas.pickle", "wb")
        pickle.dump(plazas, archivoPlazas)
        archivoPlazas.close()
        archivoOcupa = open("Persistence/ocupas.pickle", "wb")
        pickle.dump(ocupas, archivoOcupa)
        archivoOcupa.close()
        archivoClientes = open("Persistence/clientes.pickle", "wb")
        pickle.dump(clientes, archivoClientes)
        archivoClientes.close()


def mainMethod():
    seleccionMenu = -1;

    while seleccionMenu != 0:

        seleccionSubmenu = -1;
        seleccionSubmenu2 = -1;
        seleccionSubmenu3 = 1;
        confirmacion = 1;
        printMenuRoles()
        try:
            seleccionMenu = int(input())
        except:
            print("Por favor introduzca un n??mero.")

        if seleccionMenu == 1:

            while seleccionSubmenu != 0:

                printMenuUser()
                try:
                    seleccionSubmenu = int(input())
                except:
                    print("Por favor introduzca un n??mero.")

                if seleccionSubmenu == 1:
                    plazasDisponibles = [plaza for plaza in plazas if plaza.estado == Estado.LIBRE]
                    disponiblesTurismo = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.TURISMO])
                    disponiblesMotos = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOTOCICLETA])
                    disponiblesReducidas = len([plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == TipoVehiculo.MOVILIDADREDUCIDA])
                    if len(plazasDisponibles) > 0:
                        printPlazasDisponibles(plazasDisponibles, disponiblesTurismo, disponiblesMotos, disponiblesReducidas)
                        printMenuTipoVehiculo()
                        try:
                            tipoVehiculo = list(TipoVehiculo)[int(input()) - 1]
                            if (tipoVehiculo == TipoVehiculo.TURISMO and disponiblesTurismo > 0) or (tipoVehiculo == TipoVehiculo.MOTOCICLETA and disponiblesMotos > 0) or (tipoVehiculo == TipoVehiculo.MOVILIDADREDUCIDA and disponiblesReducidas > 0) :
                                matricula = input("Por favor introduzca su matr??cula: ")
                                plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == tipoVehiculo][0]
                                plaza.estado = Estado.OCUPADA
                                plazaOcupada = Ocupa(plaza, Cliente(matricula, tipoVehiculo), random.randint(100000, 999999))
                                ocupas.append(plazaOcupada)
                                print(f"Matricula: {plazaOcupada.cliente.matricula}, Id: {plazaOcupada.plaza.id}, Pin: {plazaOcupada.pin}")
                            else:
                                print("No hay plazas disponibles")
                        except:
                            print("Introduzca una opci??n v??lida")
                    else:
                        print("No hay plazas disponibles")

                elif seleccionSubmenu == 2:
                    try:
                        matricula = input("Por favor introduzca su matr??cula: ")
                        nPlaza = int(input("Introduzca el n??mero de la plaza de aparcamiento: "))
                        pin = int(input("Por ??ltimo, introduzca el pin que se le proporcion?? al estacionar: "))
                        ocupasEncontrados = [ocupa for ocupa in ocupas if ocupa.plaza.id == nPlaza and ocupa.cliente.matricula == matricula and ocupa.pin == pin]
                        if(len(ocupa) >= 1):
                            ocupa = ocupasEncontrados[0]
                            ocupa.activo = False
                            ocupa.salida = datetime.now()
                            tiempoEstacionado = divmod((ocupa.salida - ocupa.entrada).total_seconds(), 60)[0]
                            ocupa.costeTotal = ocupa.plaza.tipoPlaza.tarifa * tiempoEstacionado
                            ocupa.plaza.estado = Estado.LIBRE
                            print(f"El coste total ha sido de {ocupa.costeTotal} ???")
                        else:
                            print("No se encuentra el veh??culo estacionado.")
                    except:
                        print("Por favor introduzca una plaza y pin v??lidos")

                elif seleccionSubmenu == 3:
                    dni = input("Bienvenido de nuevo, por favor, introduzca su dni: ")
                    matricula = input("Introduzca su matr??cula: ")
                    try:
                        cliente = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo and cliente.matricula == matricula and cliente.dni == dni)
                        print(f"Puede proceder a estacionar su vehiculo, su plaza es la {cliente.plaza.id}")
                        cliente.plaza = [plaza for plaza in plazas if plaza.id == cliente.plaza.id][0]
                        cliente.plaza.estado = Estado.ABONOOCUPADA
                        ocupas.append(Ocupa(cliente.plaza, cliente, cliente.pin, costeTotal=0))
                    except:
                        print("No se encuentra el veh??culo con los datos proporcionados.")

                elif seleccionSubmenu == 4:
                    dni = input("Bienvenido de nuevo, por favor, introduzca su dni: ")
                    matricula = input("Introduzca su matr??cula: ")
                    pin = input("Introduzca su pin: ")
                    try:
                        ocupa = next(ocupa for ocupa in ocupas if ocupa.activo and ocupa.pin == int(pin) and ocupa.cliente.matricula == matricula and ocupa.cliente.dni == dni)
                        print("Puede proceder a sacar su vehiculo")
                        cliente.plaza.estado = Estado.ABONOLIBRE
                        ocupa.activo = False
                    except:
                        print("No se encuentra el veh??culo con los datos proporcionados.")

        elif seleccionMenu == 2:
            while seleccionSubmenu != 0:
                printMenuAdmin()
                try:
                    seleccionSubmenu = int(input())
                except:
                    print("Por favor introduzca un n??mero.")

                if seleccionSubmenu == 1:
                    plazasDisponibles = len([plaza for plaza in plazas if plaza.estado == Estado.LIBRE])
                    porcentajeOcupacion = (200 - plazasDisponibles) / (200/100)
                    print(f"Actualmente hay {plazasDisponibles} plazas disponibles, el porcentaje de ocupaci??n es del {porcentajeOcupacion}%")
                    printPlazas(plazas)

                elif seleccionSubmenu == 2:
                    try:
                        print("Introduzca la fecha a partir de la que consultar.")
                        anioInicio = input("A??o: ")
                        mesInicio = input("Mes: ")
                        diaInicio = input("D??a: ")
                        horaInicio = input("Hora: ")
                        minutosInicio = input("Minutos: ")
                        inicio = datetime(int(anioInicio), int(mesInicio), int(diaInicio), int(horaInicio), int(minutosInicio))
                        print("Introduzca la fecha hasta la que consultar.")
                        anioFin = input("A??o: ")
                        mesFin = input("Mes: ")
                        diaFin = input("D??a: ")
                        horaFin = input("Hora: ")
                        minutosFin = input("Minutos: ")
                        fin = datetime(int(anioFin), int(mesFin), int(diaFin), int(horaFin), int(minutosFin))
                        cobros = [ocupa for ocupa in ocupas if (not ocupa.activo) and (ocupa.costeTotal > 0 and ocupa.salida < fin and ocupa.salida > inicio)]
                        printCobros(cobros)
                    except:
                        print("Ha habido un error al obtener las fechas. Indique el a??o, mes, dia, etc, solo con n??meros.")

                elif seleccionSubmenu == 3:
                    clientesAbonados = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo]
                    printAbonados(clientesAbonados)

                elif seleccionSubmenu == 4:
                    printMenuAbonados()
                    try:
                        seleccionSubmenu2 = int(input())
                    except:
                        print("Por favor introduzca un n??mero.")

                    if seleccionSubmenu2 == 1:
                        dni = input("Dni del abonado: ")
                        nombre = input("Nombre del abonado: ")
                        apellidos = input("Apellidos del abonado: ")
                        email = input("Email del abonado: ")

                        try:
                            print("Seleccione el tipo de abono:")
                            for i, abono in enumerate(abonos):
                                print(f"{i+1}. {abono.nombre} - {abono.precio}???")
                            tipoAbono = abonos[int(input()) - 1]
                            tarjeta = input("Tarjeta del abonado: ")

                            printMenuTipoVehiculo()
                            tipoVehiculo = list(TipoVehiculo)[int(input()) - 1]
                            matricula = input("Matricula del veh??culo: ")
                            plaza = next(plaza for plaza in plazas if plaza.estado == Estado.LIBRE and plaza.tipoPlaza.tipo == tipoVehiculo)
                            pin = random.randint(100000, 999999)

                            nuevoCliente = Abonado(matricula, tipoVehiculo, dni, nombre, apellidos, email, tarjeta, tipoAbono, datetime.now(), datetime.now() + timedelta(days = 30 * tipoAbono.duracion), True, plaza, pin)
                            clientes.append(nuevoCliente)
                            plaza.estado = Estado.ABONOLIBRE
                            print("El cliente se ha suscrito con ??xito.")
                        except:
                            print("Por favor escoja una opci??n v??lida.")

                    elif seleccionSubmenu2 == 2:
                        dni = input("Introduzca el DNI del abonado a modificar: ")
                        try:
                            abonado = next(cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.activo and cliente.dni == dni)
                            print("1. Modificar datos del cliente")
                            print("2. Renovar abono")
                            seleccionSubmenu3 = int(input())

                            if seleccionSubmenu3 == 1:
                                print("Introduzca los datos a continuaci??n, para mantener el actual, simplemente pulse intro.")
                                abonado.dni = input(f"Dni del abonado (actual: {abonado.dni}): ") or abonado.dni
                                abonado.nombre = input(f"Nombre del abonado (actual: {abonado.nombre}): ") or abonado.nombre
                                abonado.apellidos = input(f"Apellidos del abonado (actual: {abonado.apellidos}): ") or abonado.apellidos
                                abonado.email = input(f"Email del abonado (actual: {abonado.email}): ") or abonado.email
                                abonado.matricula = input(f"Matricula del veh??culo (actual: {abonado.matricula}): ") or abonado.matricula
                                abonado.tarjeta = input(f"Tarjeta del abonado (actual: {abonado.tarjeta}): ") or abonado.tarjeta

                            elif seleccionSubmenu3 == 2:
                                caducidadAntigua = abonado.fechaCancelacion
                                abonado.fechaCancelacion = caducidadAntigua + timedelta(days=30 * abonado.tipoAbono.duracion)
                                print(f"El abono {abonado.tipoAbono.nombre} del cliente con DNI {abonado.dni} caducaba el {caducidadAntigua.strftime('%d de %B del %Y')}")
                                print(f"Su abono se ha extendido por {abonado.tipoAbono.duracion} meses, la nueva fecha de cancelaci??n es el {abonado.fechaCancelacion.strftime('%d de %B del %Y')}")
                        except:
                            print("No se ha encontrado al cliente, su dni est?? err??neo o no es actualmente un abonado")

                    elif seleccionSubmenu2 == 3:
                        dni = input("Introduzca el DNI del abonado a dar de baja: ")
                        try:
                            abonado = next(
                                cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.dni == dni)
                            if abonado.activo:
                                printConfirmacionBaja(abonado.fechaCancelacion)
                                confirmacion = int(input())
                                if confirmacion == 1:
                                    abonado.plaza = [plaza for plaza in plazas if plaza.id == abonado.plaza.id][0]
                                    abonado.activo = False
                                    abonado.plaza.estado = Estado.LIBRE
                                    print("El cliente se ha dado de baja con ??xito.")
                            else:
                                print("El cliente no tiene un abono activo.")
                        except:
                            print("No se ha encontrado el cliente")

                elif seleccionSubmenu == 5:
                    print("1. Consultar los abonos que caducan en un mes")
                    print("2. Consultar los abonos que caducan en menos de 10 d??as")
                    try:
                        seleccionSubmenu2 = int(input())
                    except:
                        print("Por favor introduzca un n??mero.")

                    if seleccionSubmenu2 == 1:
                        mes = int(input("Indique el n?? del mes que quiere consultar: "))
                        anio = int(input("Indique el a??o que quiere consultar: "))
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCancelacion.month == mes and cliente.fechaCancelacion.year == anio]
                        printClientesACaducar(aCaducar)
                        if len(aCaducar) == 0: print("No hay ning??n cliente cuyo abono caduque en ese mes.")

                    elif seleccionSubmenu2 == 2:
                        aCaducar = [cliente for cliente in clientes if isinstance(cliente, Abonado) and cliente.fechaCancelacion > datetime.now() and cliente.fechaCancelacion < datetime.now() + timedelta(days = 10)]
                        printClientesACaducar(aCaducar)
                        if len(aCaducar) == 0: print("No hay ning??n cliente cuyo abono caduque en 10 d??as.")

mainThread = Thread(target=mainMethod)
persistenceThread = Thread(target=persistCollections)

mainThread.start()
persistenceThread.start()