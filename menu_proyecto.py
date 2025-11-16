import recursos

dificultad= 2

def seleccion_dificultad():
    global dificultad
    while True:
        if dificultad== 1:
            dificultad= "Fácil"
            ## Llamar a los recursos para fácil
            print("Dificultad establecida a fácil")
            recursos.actualizar_recurso("dias", 10)
            recursos.actualizar_recurso("distancia", 100)
            break
        elif dificultad== 2:
            dificultad= "Normal"
            ## Llamar a los recursos para normal
            print("Dificultad establecida a normal")
            recursos.actualizar_recurso("dias", 20)
            recursos.actualizar_recurso("distancia", 150)
            break
        elif dificultad== 3:
            dificultad= "Difícil"
            ## Llamar a los recursos para difícil
            print("Dificultad establecida a difícil")
            recursos.actualizar_recurso("dias", 30)
            recursos.actualizar_recurso("distancia", 250)
            break
        else:
            print("Opción no válida")
        
def menu_principal():
    global dificultad
    while True:
        print("¡Bienvenido al menú principal del juego!")
        print("Selecciona una opción de las siguientes:")
        print("1) Iniciar el juego")
        print("2) Seleccionar la dificultad")
        print("3) Guía del juego")
        print("4) Salir del juego")
        opcion= int(input("Selecciona una opción: "))
        if opcion==1:
            print("¡Iniciando el juego!")
            ##Llamado al modulo del juego
        elif opcion==2:
            print("Selecciona una dificultad:")
            print("1) Fácil")
            print("2) Normal")
            print("3) Difícil")
            seleccion_dificultad()
            dificultad= int(input("Elige una dificultad: "))
        elif opcion==3:
            print("Características de las dificultades:")
            print("Fácil: El viaje tiene una duración máxima de 30 días y debes recorrer una distancia de 1000 años luz.")
            print("Normal: El viaje tiene una duración máxima de 20 días y debes recorrer una distancia de 2000 años luz.")
            print("Difícil: El viaje tiene una duración máxima de 15 días y debes recorrer una distancia de 2500 años luz. ")
        elif opcion==4:
            print("Gracias por jugar")
        break
            