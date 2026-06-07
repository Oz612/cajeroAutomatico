import sys
#Mensaje inicial del cajero
print ("-------Bienvenid@ a OZLAURED, tu banco de confianza------")
print("------- Registro de nueva cuenta -------")

#Creación de usuario y contraseña
usuario_registrado = input("Cree su nombre de usuario: ")
clave_registrada = int(input("Cree su contraseña (numérica): "))
print("Usuario creado con éxito.\n")

#Solicitud de datos del usuario
intentos = 3
login_exitoso = False

print("------- INICIO DE SESIÓN -------")
while intentos > 0:
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = int(input("Ingrese su contraseña: "))

    if usuario_ingresado == usuario_registrado and clave_ingresada == clave_registrada:
        print("\n¡Bienvenido al sistema!")
        login_exitoso = True
        break  #Rompe el bucle si los datos son correctos
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos}")
        if intentos > 0:
            print("Inténtelo de nuevo.\n")

#Cerrar el programa al tercer intento fallido
if not login_exitoso:
    print("Ha superado el límite de intentos permitidos. Sistema bloqueado.")
    sys.exit()  #Cierra el programa por completo


#solicitud de datos del usuario
usuario = (input("Ingrese su usuario  "))
clave = clave_registrada #La clave actual será la que registró

saldo = 0

#variables de movimiento
historial1 = "Sin movimiento"
historial2 = "Sin movimiento"
historial3 = "Sin movimiento"

#control del menu
opcion = 0

while opcion != 6:
    print("\n ----MENU CAJERO AUTOMATICO OZLAURED----")
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
        print("Gracias por usar los servicios de OZLAURED. ¡Hasta luego!")
    
    else:
        print("Opcion no valida.")        
            