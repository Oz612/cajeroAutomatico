#solicitud de datos del usuario
usuario = (input("Ingrese su usuario  "))
usuario = usuario

clave = int(input("Ingrese su contraseña  "))
clave = clave

saldo = 0

#variables de movimiento
historial1 = "Sin movimiento"
historial2 = "Sin movimiento"
historial3 = "Sin movimiento"

#control del menu
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

if opcion == 1:
    print(f"Su saldo es de: ${saldo}")
    
    historial1 = historial2
    historial2 = historial3
    historial3 = "consulta de saldo"
    
elif opcion == 2:
    ingreso = int(input("Ingrese el valor a depositar:   "))
    saldo = saldo + ingreso
    print(f"Deposito realizado. Su nuevo saldo es de: ${saldo}")
    
    historial1 = historial2
    historial2 = historial3
    historial3 = f"Deposito de ${ingreso}"
    
elif opcion == 3:
    retiro = int(input("Ingrese el valor a retirar:   "))
    
    if retiro > saldo:
        print("Saldo insuficiente")
    else:
        saldo = saldo - retiro  
        print(f"Retiro Exitoso. saldo restante es de ${saldo}")
        
        historial1 = historial2
        historial2 = historial3
        historial3 = f"Retiro de ${retiro}"

elif opcion == 4:
        claveActual = int(input("Ingrese su contraseña actual:   "))
        
        if claveActual == clave:
            nuevaClave = int(input("Ingrese su nueva contraseña:   "))
            clave = nuevaClave
            print("Cambio de contraseña exitoso")
            
            historial1 = historial2
            historial2 = historial3
            historial3 = "Cambio de contraseña"
            
        else:
            print("contraseña incorrecta")

elif opcion == 5:
    print("--- HISTORIAL ---")
    print( historial1 )
    print( historial2 )
    print( historial3 )
    
elif opcion == 6:
    print("Gracias")
    
else:
    print("Opcion no valida.")        
            