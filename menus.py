import random

dificultad = "Normal"  # Dificultad por defecto: Normal

def principal():
    """Menu principal del juego."""
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")
    print("2. Seleccionar dificultad")
    print("3. Salir")
    
    global dificultad    

    eleccion = (input("Seleccione una opción: "))
    while eleccion not in ['1', '2', '3']:
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("Seleccione una opción: ")
        
    if eleccion == '1':
        print("Iniciando juego...")
        # Aquí se llamaría a la función para iniciar el juego
    elif eleccion == '2':
        #Selección de dificultad
        print("=== SELECCIONAR DIFICULTAD ===")
        print(f"Dificultad actual: {dificultad}")
        print("1. Fácil")
        print("2. Normal")
        print("3. Difícil")
        
        dificultad = input("Seleccione la dificultad: ")
        
        while dificultad not in ['1', '2', '3']:
            print("Opción no válida. Intente de nuevo.")
            dificultad = input("Seleccione la dificultad: ")    
        
        if dificultad == '1':
            dificultad = "Fácil"
        elif dificultad == '2':
            dificultad = "Normal"
        elif dificultad == '3':
            dificultad = "Difícil"
    



#def generar_nombre_nave():
#    """Genera un nombre aleatorio para la nave."""
#    nombres = [
#    "USS Enterprise", "Halcón Milenario", "Serenity", "Galáctica",
#    "Nostromo", "Rocinante", "Andromeda", "Odyssey", "Event Horizon",
#    "Intrepid", "Discovery", "Voyager", "Endeavour", "Constellation",
#    "Prometheus", "Daedalus", "Hawking", "Aurora", "Nova", "Orion",
#    "Pioneer", "Falcon", "Nebula", "Phoenix", "Aegis", "Valkyrie",
#    "Leviathan", "Atlas", "Corsair", "Argonaut"
#]
#    return random.choice(nombres)