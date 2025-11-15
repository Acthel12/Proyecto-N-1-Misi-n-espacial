import recursos
import os
import math

dificultad = "Normal"  # Dificultad por defecto: Normal
eventos_diarios = 5  # Número de eventos diarios por defecto

def clear_screen():
    """Limpia la pantalla de la consola."""
    #Gracias Khalid por ayudarme con esto :)
    if os.name == 'nt':  # Revisa si el sistema operativo es Windows
        os.system('cls')
    else:  # Asume que es un sistema tipo Unix (Linux, macOS)
        os.system('clear')

def principal():
    """Menu principal del juego.
    Sirve para iniciar el juego, seleccionar la dificultad o salir."""
    while True:
        clear_screen()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Iniciar juego")
        print("2. Seleccionar dificultad")
        print("3. Salir")
        
        global dificultad    

        eleccion = (input("Seleccione una opción: "))
        while eleccion != '1' and eleccion != '2' and eleccion != '3':
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("Seleccione una opción: ")
            
        if eleccion == '1':
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
            
            while dificultad != '1' and dificultad != '2' and dificultad != '3':
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
            print("Saliendo del juego. ¡Hasta luego!")
            exit()

def configurar_dificultad():
    if dificultad == "Fácil":
        recursos.actualizar_recurso("dias", -30)  # Más días en dificultad fácil
        recursos.actualizar_recurso("distancia", 1000)  # Menor distancia en dificultad fácil
        global eventos_diarios
        eventos_diarios = 3  # Menos eventos diarios en dificultad fácil
    elif dificultad == "Normal":
        recursos.actualizar_recurso("dias", -20)  # Días estándar
        recursos.actualizar_recurso("distancia", 2000)  # Distancia estándar
    elif dificultad == "Difícil":
        recursos.actualizar_recurso("dias", -15)  # Menos días en dificultad difícil
        recursos.actualizar_recurso("distancia", 2500)  # Mayor distancia en dificultad difícil
    
def in_game_menu():
    """Menú dentro del juego.
    Permite al jugador ver recursos, continuar o salir al menú principal."""
    while True:
        clear_screen()
        print("=== MENÚ DEL JUEGO ===")
        print("1. Ver recursos")
        print("2. Continuar juego")
        print("3. Salir al menú principal")
        
        eleccion = input("Seleccione una opción: ")
        while eleccion != '1' and eleccion != '2' and eleccion != '3':
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1':
            clear_screen()
            print("=== RECURSOS ACTUALES ===")
            recursos.mostrar_recursos()
            input("Presiona Enter para regresar al menú...")  # Pausa para que el jugador pueda ver los recursos
        elif eleccion == '2':
            print("Continuando el juego...")
            return False
        elif eleccion == '3':
            print("Regresando al menú principal...")
            recursos.reiniciar_recursos()  # Reiniciar los recursos para una nueva partida
            return True # Regresar al menú principal

def inicio_dia():
    clear_screen()
    """Menu de inicio de día."""
    print("=== INICIO DEL DÍA ===")
    print("Dia numero:", recursos.dias_transcurridos)
    recursos.mostrar_recursos()
    input("Presiona Enter para continuar...")

def fin_dia():
    clear_screen()
    """Menu de fin de día."""
    print("=== FIN DEL DÍA ===")
    recursos.mostrar_recursos()
    recursos.actualizar_recurso("dias", 1)
    if dificultad == "Difícil":
        recursos.actualizar_recurso("suministros", -1.5)  # Pérdida adicional de suministros en dificultad difícil
        recursos.actualizar_recurso("moral", -1)  # Pérdida adicional de moral en dificultad difícil
        recursos.actualizar_recurso("energia", -1.5)  # Pérdida adicional de energía en dificultad difícil
        recursos.actualizar_recurso("oxigeno", -1.5)  # Pérdida adicional de oxígeno en dificultad difícil
    else:
        recursos.actualizar_recurso("suministros", -1)
        recursos.actualizar_recurso("moral", -0.5)
        recursos.actualizar_recurso("energia", -1)
        recursos.actualizar_recurso("oxigeno", -1)
    input("Presiona Enter para continuar...")

def game_over():
    clear_screen()
    """Menu de game over."""
    print("=== GAME OVER ===")
    print("Lo siento, has perdido la misión.")
    recursos.mostrar_recursos()
    print("Ir al menu principal o salir del juego.")
    print("1. Ir al menú principal")
    print("2. Salir del juego")
    eleccion = input("Seleccione una opción: ")
    while eleccion != '1' and eleccion != '2':
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("Seleccione una opción: ")
    if eleccion == '1':
        print("Regresando al menú principal...")
        input("Presiona Enter para continuar...")
        recursos.reiniciar_recursos()  # Reiniciar los recursos para una nueva partida
    elif eleccion == '2':
        print("Saliendo del juego. ¡Hasta luego!")
        exit()

def victoria():
    clear_screen()
    """Menu de victoria."""
    print("=== ¡FELICIDADES, HAS GANADO! ===")
    print("Has logrado llegar a tu destino con éxito.")
    recursos.mostrar_recursos()
    print("Ir al menu principal o salir del juego.")
    print("1. Ir al menú principal")
    print("2. Salir del juego")
    eleccion = input("Seleccione una opción: ")
    while eleccion != '1' and eleccion != '2':
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("Seleccione una opción: ")
    if eleccion == '1':
        print("Regresando al menú principal...")
        input("Presiona Enter para continuar...")
        recursos.reiniciar_recursos()  # Reiniciar los recursos para una nueva partida
    elif eleccion == '2':
        print("Saliendo del juego. ¡Hasta luego!")
        exit() 

def motores():
    clear_screen()
    """Menu de motores."""
    while True:
        print("=== MENÚ DE MOTORES ===")
        print("Aquí puedes gestionar los motores de tu nave espacial.")
        print("Que cantidad de combustible deseas usar para avanzar?")
        print("la cantidad máxima es 50 %.")
        print("La cantidad minima es 0 %.")
        cantidad = input("Ingresa la cantidad de combustible a usar: ")
        while (cantidad.replace('.','',1).isdigit() == False) and (float(cantidad) < 0.0 or float(cantidad) > 50.0) and (float(cantidad) > float(recursos.combustible)):
            print("Cantidad no válida. Intente de nuevo.")
            cantidad = input("Ingresa la cantidad de combustible a usar: ")
            if cantidad.replace('.','',1).isdigit() == True:
                cantidad = float(cantidad)
                while cantidad < 0.0 or cantidad >= 50.0:
                    print("Cantidad no válida. Intente de nuevo.")
                    cantidad = float(input("Ingresa la cantidad de combustible a usar: "))
                if cantidad.replace('.','',1).isdigit() == False and (float(cantidad) < 0.0 or float(cantidad) > 50.0):
                    while float(cantidad) > float(recursos.combustible):
                        print("Cantidad no válida. Intente de nuevo.")
                        cantidad = input("Ingresa la cantidad de combustible a usar: ")
                    
        cantidad = float(cantidad)      
        print(f"Usando {cantidad}% de combustible para avanzar...")
        print("Esta seguro?")
        confirmacion = input("Ingrese 's' para confirmar o 'n' para cancelar: ")
        while confirmacion != 's' and confirmacion != 'n':
            print("Opción no válida. Intente de nuevo.")
            confirmacion = input("Ingrese 's' para confirmar o 'n' para cancelar: ")
        if confirmacion == 'n':
            print("Operación cancelada. Regresando al menú de motores...")
            input("Presiona Enter para continuar...")
        elif confirmacion == 's':
            recursos.actualizar_recurso("combustible", -(cantidad))
            recursos.actualizar_recurso("distancia", -(math.sqrt(cantidad/100) * (1000 / math.sqrt(0.5))))  # Avanza según la raíz cuadrada del combustible usado
            print("Mientras los motores funcionan, duermes un poco...")
            print(f"Has avanzado {math.sqrt(cantidad/100) * (1000 / math.sqrt(0.5))} en tu viaje.")
            input("Presiona Enter para regresar al menú del juego...")
            break