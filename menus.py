#Importación de módulos necesarios para los diferentes menús
import recursos
import os
import math
import ascii
import puntuacion
import narrativa

#Añadidas variables globales para que la narrativa no se ejecute fuera de las condiciones establecidas
narrativa_ejecutada1 = False
narrativa_ejecutada2 = False
narrativa_ejecutada3 = False
narrativa_ejecutada4 = False
dificultad = "Normal"  # Dificultad por defecto: Normal
eventos_diarios = 5  # Número de eventos diarios por defecto

def reiniciar_narrativa(): #Reinicia la narrativa
    global narrativa_ejecutada1, narrativa_ejecutada2 , narrativa_ejecutada3, narrativa_ejecutada4
    narrativa_ejecutada1 = False
    narrativa_ejecutada2 = False
    narrativa_ejecutada3 = False
    narrativa_ejecutada4 = False

def clear_screen():
    """Limpia la pantalla de la consola."""
    if os.name == 'nt':  # Revisa si el sistema operativo es Windows
        os.system('cls')
    else:  # Asume que es un sistema tipo Unix (Linux, macOS)
        os.system('clear')

def principal():
    """Menú principal del juego.
    Sirve para iniciar el juego, seleccionar la dificultad o salir."""
    recursos.reiniciar_recursos()
    reiniciar_narrativa()
    while True:
        clear_screen()
        ascii.principal()
        print("=== MENÚ PRINCIPAL ===")
        print("1) Iniciar juego")
        print("2) Seleccionar dificultad")
        print("3) Guía del juego")
        print("4) Salir")
        
        global dificultad    

        eleccion = (input("Seleccione una opción: "))
        while eleccion != '1' and eleccion != '2' and eleccion != '3' and eleccion != '4': #Condiciones para cuando las opciones no son válidas
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("Seleccione una opción: ")
            
        if eleccion == '1': #Iniciar juego
            print("Iniciando juego...")
            configurar_dificultad()
            break
        elif eleccion == '2':
            #Selección de dificultad
            print("=== SELECCIONAR DIFICULTAD ===")
            print(f"Dificultad actual: {dificultad}")
            print("1. Fácil")
            print("2. Normal")
            print("3. Difícil")
            
            dificultad = input("Seleccione la dificultad: ")
            
            while dificultad != '1' and dificultad != '2' and dificultad != '3': #Condiciones para cuando las opciones no son válidas
                print("Opción no válida. Intente de nuevo.")
                dificultad = input("Seleccione la dificultad: ")    
            
            if dificultad == '1':
                dificultad = "Fácil"
            elif dificultad == '2':
                dificultad = "Normal"
            elif dificultad == '3':
                dificultad = "Difícil"
            print(f"Dificultad establecida a: {dificultad}")
            input("Presiona Enter para regresar al menú...")
        elif eleccion == '3':
            # Guía del juego
            print("===CARACTERÍSTICAS DE LAS DIFICULTADES===")
            print("Fácil: El viaje tiene una duración máxima de 30 días y debes recorrer una distancia de 1000 años luz.")
            print("Normal: El viaje tiene una duración máxima de 20 días y debes recorrer una distancia de 2000 años luz.")
            print("Difícil: El viaje tiene una duración máxima de 15 días y debes recorrer una distancia de 2500 años luz.")
            input("Presiona Enter para regresar al menú...")
        elif eleccion == '4': #Salir del juego y detener el programa
            print("Saliendo del juego. ¡Hasta luego!")
            exit()

def configurar_dificultad():
    """Configura los recursos iniciales según la dificultad seleccionada."""
    if dificultad == "Fácil":
        recursos.actualizar_recurso("dias_restantes", 30)  # Más días en dificultad fácil
        recursos.actualizar_recurso("distancia", -1000)  # Menor distancia en dificultad fácil
        global eventos_diarios
        eventos_diarios = 3  # Menos eventos diarios en dificultad fácil
    elif dificultad == "Normal":
        recursos.actualizar_recurso("dias_restantes", 20)  # Días estándar
        recursos.actualizar_recurso("distancia", -2000)  # Distancia estándar
    elif dificultad == "Difícil":
        recursos.actualizar_recurso("dias_restantes", 15)  # Menos días en dificultad difícil
        recursos.actualizar_recurso("distancia", -2500)  # Mayor distancia en dificultad difícil
    
def in_game_menu():
    """Menú dentro del juego.
    Permite al jugador ver recursos, continuar o salir al menú principal."""
    while True:
        clear_screen()
        print("=== MENÚ DEL JUEGO ===")
        ascii.in_game_menu()
        print("1. Ver recursos")
        print("2. Continuar juego")
        print("3. Salir al menú principal")
        
        eleccion = input("Seleccione una opción: ")
        while eleccion != '1' and eleccion != '2' and eleccion != '3': #Condiciones para cuando las opciones no son válidas
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1': #Muestra los recursos actuales
            clear_screen()
            print("=== RECURSOS ACTUALES ===")
            ascii.recursos()
            recursos.mostrar_recursos()
            input("Presiona Enter para regresar al menú...")
        elif eleccion == '2': #Continúa el juego
            print("Continuando el juego...")
            return False
        elif eleccion == '3': # Regresar al menú principal
            print("Regresando al menú principal...")
            return True 

def inicio_dia(): #Función para el inicio del día
    clear_screen()
    """Menú de inicio del día."""
    narrativa_juego()
    clear_screen()
    print("=== INICIO DEL DÍA ===")
    ascii.inicio_dia()
    print("Día número:", recursos.dias_transcurridos + 1) #Muestra los días transcurridos actuales
    recursos.mostrar_recursos()
    input("Presiona Enter para continuar...")

def fin_dia():
    """Menú de fin del día."""
    clear_screen()
    print("=== FIN DEL DÍA ===")
    ascii.fin_dia()
    recursos.mostrar_recursos()
    recursos.actualizar_recurso("dias", 1)
    if dificultad == "Difícil":
        recursos.actualizar_recurso("suministros", -10)  # Pérdida adicional de suministros en dificultad difícil
        recursos.actualizar_recurso("moral", -5)  # Pérdida adicional de moral en dificultad difícil
        recursos.actualizar_recurso("energia", -10)  # Pérdida adicional de energía en dificultad difícil
        recursos.actualizar_recurso("oxigeno", -10)  # Pérdida adicional de oxígeno en dificultad difícil
    else: #Pérdidas estándar de recursos en el resto de dificultades
        recursos.actualizar_recurso("suministros", -6)
        recursos.actualizar_recurso("moral", -3)
        recursos.actualizar_recurso("energia", -6)
        recursos.actualizar_recurso("oxigeno", -6)
    input("Presiona Enter para continuar...")

def game_over(): #Función para el menú cuando pierdes el juego
    """Menú de game over."""
    clear_screen()
    narrativa.narrativa_al_perder()
    clear_screen()
    print("=== GAME OVER ===")
    ascii.game_over()
    print("Lo siento, has perdido la misión.")
    recursos.mostrar_recursos()
    print("Ir al menú principal o salir del juego.")
    print("1. Ir al menú principal")
    print("2. Salir del juego")
    eleccion = input("Seleccione una opción: ")
    while eleccion != '1' and eleccion != '2': #Condiciones para cuando las opciones no son válidas
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("Seleccione una opción: ")
    if eleccion == '1': #Regresa al menú principal
        print("Regresando al menú principal...")
        input("Presiona Enter para continuar...")
    elif eleccion == '2': #Salir del juego
        print("Saliendo del juego. ¡Hasta luego!")
        exit()

def victoria(): #Función para el menú cuando ganas el juego
    """Menú de victoria."""
    narrativa.narrar_final()
    clear_screen()
    print("=== ¡FELICIDADES, HAS GANADO! ===")
    ascii.victoria()
    print("Has logrado llegar a tu destino con éxito.")
    recursos.mostrar_recursos()
    puntuacion.puntuacion_final()
    print("Ir al menú principal o salir del juego.")
    print("1. Ir al menú principal")
    print("2. Salir del juego")
    eleccion = input("Seleccione una opción: ")
    while eleccion != '1' and eleccion != '2': #Condiciones para cuando las opciones no son válidas
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("Seleccione una opción: ")
    if eleccion == '1': #Regresa al menú principal
        print("Regresando al menú principal...")
        input("Presiona Enter para continuar...")
    elif eleccion == '2': #Salir del juego
        print("Saliendo del juego. ¡Hasta luego!")
        exit() 

def motores(): #Función para manejar los motores de la nave
    """Menú de motores."""
    clear_screen()
    while recursos.combustible > 0:
        clear_screen()
        print("=== MENÚ DE MOTORES ===")
        ascii.motores()
        print("Aquí puedes gestionar los motores de tu nave espacial.") #Indicaciones para el jugador
        print("¿Qué cantidad de combustible deseas usar para avanzar?")
        print("la cantidad máxima es 50 %.")
        print("La cantidad minima es 0 %.")
        print(f"Tienes {recursos.combustible}% de combustible disponible.")
        cantidad = input("Ingresa la cantidad de combustible a usar: ")
        while (cantidad.replace('.','',1).isdigit() == False) or (float(cantidad) <= 0.0 or float(cantidad) > 50.0) or (float(cantidad) > float(recursos.combustible)): #Bucle para comprobar que la cantidad ingresada es válida
            if cantidad.replace('.','',1).isdigit() == False:
                print("Opción no válida. Intente de nuevo.")
            elif float(cantidad) <= 0.0 or float(cantidad) > 50.0:
                print("La cantidad debe estar entre 0 y 50. Intente de nuevo.")
            elif float(cantidad) > float(recursos.combustible):
                print("No tienes suficiente combustible. Intente de nuevo.")
            cantidad = input("Ingresa la cantidad de combustible a usar: ")                        
        cantidad = float(cantidad)
        print(f"Usando {cantidad}% de combustible para avanzar...")
        print(f"Tu nave avanzará una distancia de {round(math.sqrt(cantidad/100) * (200 / math.sqrt(0.5)), 2)} años luz.") #Fórmula para calcular la distancia avanzada según el combustible usado
        print("Está seguro?") #Confirmación antes de usar el combustible
        confirmacion = input("Ingrese 's' para confirmar o 'n' para cancelar: ")
        while confirmacion != 's' and confirmacion != 'n':
            print("Opción no válida. Intente de nuevo.")
            confirmacion = input("Ingrese 's' para confirmar o 'n' para cancelar: ")
        if confirmacion == 'n':
            print("Operación cancelada. Regresando al menú de motores...")
            input("Presiona Enter para continuar...")
        elif confirmacion == 's': #Actualiza los recursos según el combustible usado
            recursos.actualizar_recurso("combustible", -cantidad)
            recursos.actualizar_recurso("distancia", math.sqrt(cantidad/100) * (200 / math.sqrt(0.5)))  # Avanza según la raíz cuadrada del combustible usado
            print("Mientras los motores funcionan, duermes un poco...")
            print(f"Has avanzado {round(math.sqrt(cantidad/100) * (200 / math.sqrt(0.5)), 2)} en tu viaje.")
            input("Presiona Enter para regresar al menú del juego...")
            break
        
def narrativa_juego(): #Función para manejar la narrativa del juego de acuerdo a la dificultad seleccionada
    """Narrativa para las diferents dificultades."""
    global narrativa_ejecutada1, narrativa_ejecutada2 , narrativa_ejecutada3, narrativa_ejecutada4
    if dificultad == "Fácil":
        if recursos.dias_transcurridos== 0 and not narrativa_ejecutada1:
            narrativa.narrar_primera_parte()
            narrativa_ejecutada1 = True
        if 0 < recursos.distancia_recorrida<= 200 and not narrativa_ejecutada2:
            narrativa.narrar_segunda_parte()
            narrativa_ejecutada2 = True
        if 200 < recursos.distancia_recorrida <= 500 and not narrativa_ejecutada3:
            narrativa.narrar_tercera_parte()
            narrativa_ejecutada3 = True
        if 500 < recursos.distancia_recorrida <= 800 and not narrativa_ejecutada4:
            narrativa.narrar_cuarta_parte()
            narrativa_ejecutada4 = True
    elif dificultad == "Normal":
        if recursos.dias_transcurridos== 0 and not narrativa_ejecutada1:
            narrativa.narrar_primera_parte()
            narrativa_ejecutada1 = True
        if 0 < recursos.distancia_recorrida <= 500 and not narrativa_ejecutada2:
            narrativa.narrar_segunda_parte()
            narrativa_ejecutada2 = True
        if 500 < recursos.distancia_recorrida <= 1000 and not narrativa_ejecutada3:
            narrativa.narrar_tercera_parte()
            narrativa_ejecutada3 = True
        if 1000 < recursos.distancia_recorrida <= 1500 and not narrativa_ejecutada4:
            narrativa.narrar_cuarta_parte()
            narrativa_ejecutada4 = True
    elif dificultad == "Difícil":
        if recursos.dias_transcurridos== 0 and not narrativa_ejecutada1:
            narrativa.narrar_primera_parte()
        if 0 < recursos.distancia_recorrida <= 800 and not narrativa_ejecutada2:
            narrativa.narrar_segunda_parte()
        if 800 < recursos.distancia_recorrida <= 1500 and not narrativa_ejecutada3:
            narrativa.narrar_tercera_parte()
        if 1500 < recursos.distancia_recorrida <= 2000 and not narrativa_ejecutada4:
            narrativa.narrar_cuarta_parte()

