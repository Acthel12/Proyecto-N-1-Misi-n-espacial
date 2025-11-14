import recursos
import eventos
import engine

dificultad = "Normal"  # Dificultad por defecto: Normal
eventos_diarios = 5  # Número de eventos diarios por defecto

def principal():
    """Menu principal del juego.
    Sirve para iniciar el juego, seleccionar la dificultad o salir."""
    while True:
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
            engine.juego()
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
        elif eleccion == '3':
            print("Saliendo del juego. ¡Hasta luego!")
            exit()

def configurar_dificultad():
    if dificultad == "Fácil":
        print("Has seleccionado la dificultad Fácil.")
        recursos.actualizar_recurso("dias", -30)  # Más días en dificultad fácil
        global eventos_diarios
        eventos_diarios = 3  # Menos eventos diarios en dificultad fácil
    elif dificultad == "Normal":
        print("Has seleccionado la dificultad Normal.")
        recursos.actualizar_recurso("dias", -20)  # Días estándar
    elif dificultad == "Difícil":
        print("Has seleccionado la dificultad Difícil.")
        recursos.actualizar_recurso("dias", -15)  # Menos días en dificultad difícil
    
def in_game_menu():
    """Menú dentro del juego.
    Permite al jugador ver recursos, continuar o salir al menú principal."""
    while True:
        print("=== MENÚ DEL JUEGO ===")
        print("1. Ver recursos")
        print("2. Continuar juego")
        print("3. Salir al menú principal")
        
        eleccion = input("Seleccione una opción: ")
        while eleccion != '1' and eleccion != '2' and eleccion != '3':
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("Seleccione una opción: ")
        
        if eleccion == '1':
            recursos.mostrar_recursos()
        elif eleccion == '2':
            print("Continuando el juego...")
            break  # Salir del menú para continuar el juego
        elif eleccion == '3':
            print("Regresando al menú principal...")
            principal()  # Regresar al menú principal

def inicio_dia():
    """Menu de inicio de día."""
    print("=== INICIO DEL DÍA ===")
    print("Dia numero:", recursos.dias_transcurridos)
    recursos.mostrar_recursos()
    input("Presiona Enter para continuar...")

def fin_dia():
    """Menu de fin de día."""
    print("=== FIN DEL DÍA ===")
    recursos.mostrar_recursos()
    recursos.actualizar_recurso("dias", 1)
    input("Presiona Enter para continuar...")