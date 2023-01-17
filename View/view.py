def printMenuRoles():
    print("Bienvenido, por favor indique si quiere acceder como administrador o como cliente:")
    print("1. Cliente")
    print("2. Administrador")
    print("0. Salir")

def printMenuUser():
    print("Por favor indique lo que desea hacer:")
    print("1. Depositar vehículo")
    print("2. Retirar vehículo")
    print("3. Depositar vehículo abonado")
    print("4. Retirar vehículo abonado")
    print("0. Volver")

def printMenuTipoVehiculo():
    print("Seleccione el tipo del vehículo:")
    print("1. Turismo")
    print("2. Motocicleta")
    print("3. Vehículo para personas con movilidad reducida")

def printMenuAdmin():
    print("Por favor indique lo que desea hacer:")
    print("1. Consultar estado del parking")
    print("2. Consultar facturación")
    print("3. Consultar abonos")
    print("4. Gestión de abonos")
    print("5. Caducidad de abonos")
    print("0. Volver")

def printMenuAbonados():
    print("1. Alta de abonado")
    print("2. Modificación de datos del abonado")
    print("3. Baja del abonado")

def printConfirmacionBaja(fechaBaja):
    print(
        f"El cliente tiene una suscripción hasta el {fechaBaja.strftime('%d de %B del %Y')}.")
    print(
        "Este cliente perderá su abono de forma inmediata a pesar del tiempo de suscripción restante,")
    print("¿está seguro de querer dar de baja al cliente? (esta acción no tiene vuelta atrás):")
    print("1. Si")
    print("2. No")

def printClientesACaducar(aCaducar):
    for cliente in aCaducar:
        print(
            f"{cliente.nombre} {cliente.apellidos}: Suscripcion {cliente.tipoAbono.nombre}, caduca el {cliente.fechaCancelacion.strftime('%d de %B del %Y')}")

def printPlazas(plazas):
    pos = 1
    for plaza in plazas:
        if pos < 5:
            print(f"| {plaza.id} - {plaza.estado.value} |", end=" ")
            pos += 1
        else:
            print(f"| {plaza.id} - {plaza.estado.value} |")
            pos = 1

def printCobros(cobros):
    for cobro in cobros:
        print(
            f"Plaza {cobro.plaza.id}({cobro.plaza.tipoPlaza.tipo.value}) - {cobro.entrada.strftime('%d/%m/%Y, %H:%M:%S')} hasta {cobro.salida.strftime('%d/%m/%Y, %H:%M:%S')} - Total = {cobro.costeTotal} €")

def printAbonados(clientesAbonados):
    if len(clientesAbonados) == 0:
        print("No hay ningún cliente abonado actualmente.")
    for cliente in clientesAbonados:
        print(
            f"{cliente.nombre} {cliente.apellidos}: Suscripcion {cliente.tipoAbono.nombre}, caduca el {cliente.fechaCancelacion.strftime('%d de %B del %Y')}")

def printPlazasDisponibles(plazasDisponibles, disponiblesTurismo, disponiblesMotos, disponiblesReducidas):
    print(f"Hay un total de {len(plazasDisponibles)} plazas disponibles")
    print(
        f"{disponiblesTurismo} plazas disponibles para turismos." if disponiblesTurismo > 0 else "Ninguna plaza disponible para turismos")
    print(
        f"{disponiblesMotos} plazas disponibles para motos." if disponiblesMotos > 0 else "Ninguna plaza disponible para motos")
    print(
        f"{disponiblesReducidas} plazas disponibles para vehículos para personas con movilidad reducidad." if disponiblesReducidas > 0 else "Ninguna plaza disponible para vehículos para personas con movilidad reducidad")