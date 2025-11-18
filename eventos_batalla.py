import recursos
import random





#ataque pirata espacial

def ataque_pirata():
    """Evento en donde unos piratas espaciales atacan la nave."""
    print("¡Unos piratas espaciales estan atacando tu nave!")
    print("1. Pelear")
    print("2. Huir")

    opcion = input("Elige una opcion: ")

    while opcion != "1" and opcion != "2":
        print("Opcion no valida. Intente de nuevo.")
        opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Decidiste pelear contra los piratas.")
        recursos.actualizar_recurso("energia", -10)
        recursos.actualizar_recurso("integridad", -15)
        recursos.actualizar_recurso("suministros", 20)
        print("Ganaste suministros pero tu nave sufrio danos.")
    else:
        print("Intentas huir rapidamente.")
        recursos.actualizar_recurso("combustible", -20)
        print("Gastaste combustible para escapar.")





#emboscada de drones

def drones_hostiles():
    """Evento donde drones hostiles atacan la nave."""
    print("Unos drones hostiles aparecen alrededor de tu nave.")
    print("No puedes evitar el ataque.")

    recursos.actualizar_recurso("integridad", -20)
    recursos.actualizar_recurso("energia", -10)

    print("Los drones atacaron tu nave.")
    print("Perdiste integridad y energia.")

    azar = random.randint(1, 3)

    if azar == 1:
        recursos.actualizar_recurso("suministros", 25)
        print("Destruiste un dron y recuperaste piezas utiles.")





#asalto a la nave

def asalto_enemigo():
    """Evento donde enemigos abordan la nave."""
    print("¡Un grupo enemigo ha abordado tu nave!")
    print("La tripulacion esta luchando por defenderse.")

    recursos.actualizar_recurso("suministros", -15)
    recursos.actualizar_recurso("moral", -20)

    print("Los enemigos robaron suministros.")
    print("La moral de la tripulacion ha bajado.")

    azar = random.randint(1, 2)

    if azar == 1:
        print("Logras expulsar a los invasores.")
        recursos.actualizar_recurso("integridad", 15)
    else:
        print("Los invasores escaparon sin ser detenidos.")






