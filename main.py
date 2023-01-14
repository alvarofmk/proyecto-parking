import random
from Entities.cliente import Cliente
from Entities.estado import Estado
from Entities.tipoPlaza import TipoPlaza
from Entities.plaza import Plaza
from Entities.ocupa import Ocupa

numPlazas = 200
plazasTurismos = TipoPlaza("Turismos", 0.12, 70)
plazasMotos = TipoPlaza("Motocicletas", 0.08, 15)
plazasReducidas = TipoPlaza("Movilidad reducida", 0.10, 15)
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

print("Bienvenido, por favor indique si quiere acceder como administrador o como cliente:")
print("1. Cliente")
print("2. Administrador")
print("0. Salir")

seleccionMenu = int(input())

if seleccionMenu == 1:

    while seleccionSubmenu != 0:

        print("Por favor indique lo que desea hacer:")
        print("1. Depositar vehículo")
        print("2. Retirar vehículo")
        print("3. Depositar vehículo abonado")
        print("4. Retirar vehículo abonado")
        print("0. Volver")
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
                print("Por favor indique el tipo de su vehículo:")
                print("1. Turismo")
                print("2. Motocicleta")
                print("3. Vehículo para personas con movilidad reducida")
                seleccionSubmenu2 = int(input())
                if seleccionSubmenu2 == 1 and disponiblesTurismo > 0:
                    print("Por favor introduzca su matrícula:")
                    matricula = input()
                    plaza = [plaza for plaza in plazasDisponibles if plaza.tipoPlaza.tipo == "Turismos"][0]
                    plaza.estado = Estado.OCUPADA
                    plazaOcupada = Ocupa(plaza, Cliente(matricula), random.randint(100000, 999999))
                    print(plazaOcupada)
                elif seleccionSubmenu2 == 2:
                    pass
                elif seleccionSubmenu2 == 3:
                    pass
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