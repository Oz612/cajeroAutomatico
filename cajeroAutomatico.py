#solicitud de datos del usuario
usuario = (input("Ingrese su usuario  "))
usuario = usuario

contraseña = int(input("Ingrese su contraseña  "))
contraseña = contraseña

saldo = 0

#variables de movimiento
historial1 = "Sin movimiento"
historial2 = "Sin movimiento"
historial3 = "Sin movimiento"

#variable del control del menun
opcion = 0

while opcion != 6:
    print("MENU ----CAJERO AUTOMATICO OZLAURED")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Cambiar contraseña")
    print("5. Ver Movimientos")
    print("6. Cerrar")
    
opcion = int(input("Seleccione una opcion:   ")) 

