import random
import recursos

#Traten de añadir eventos variados , que afecten diferentes recursos y que tengan varias opciones

#selección aleatoria de eventos Nota: agregar más eventos a medida que se creen eventos
def evento_aleatorio():
    """Selecciona y ejecuta un evento aleatorio."""
    eventos = random.choice("1234567")
    if eventos == "1":
        asteriode_metalico()
    elif eventos == "2":
        tormenta_cosmica_()
    elif eventos == "3":
        repartir_suministros()
    elif eventos == "4":
        tormenta_cosmica_repentina()
    elif eventos == "5":
        encontrar_combustible()
    elif eventos == "6":
        ganar_combustible_moral()
    elif eventos == "7":
        minar_combustible()
    input("Presiona Enter para continuar...")

#Los eventos por ahora solo afetan -5 o +5 a los recursos, pero se pueden modificar

#Eventos aleatorios que aumetan los recursos
def asteriode_metalico():
    """Evento que otorga suministros y moral."""
    print("¡Has encontrado un asteroide metálico rico en recursos!")
    recursos.actualizar_recurso("suministros", 5)
    recursos.actualizar_recurso("moral", 5)

#Eventos aleatorios que reducen los recursos
def tormenta_cosmica_():
    """Evento que reduce integridad o suministros."""
    print("¡En el camino te has topado con una tormenta cósmica!")
    eleccion = input("¿Deseas esquivarla (1) o atravesarla (2)? ")
    while eleccion != '1' and eleccion != '2':
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("¿Deseas esquivarla (1) o atravesarla (2)? ")
    if eleccion == '1':
        recurso = random.choice("cd")
        if recurso == "c":
            print("Has perdido algo de combustible al esquivar la tormenta.")
            recursos.actualizar_recurso("combustible", -5)
        else:
            print("Has perdido algunos días al esquivar la tormenta.")
            recursos.actualizar_recurso("dias", 2)
    else:
        suerte = random.randint(1, 100)
        if suerte >= 50:
            print("Has logrado atravesar la tormenta sin daños mayores.")
        else:
            print("La tormenta ha causado daños significativos a tu nave.")
            recursos.actualizar_recurso("integridad", -5)
            recursos.actualizar_recurso("suministros", -5)

#Eventos de perdida de recursos
def tormenta_cosmica_repentina():
    """Evento que reduce integridad y energia."""
    print("¡Una tormenta cósmica ha aparecido repentinamente y a dañado tu nave!")
    recursos.actualizar_recurso("integridad", -5)
    recursos.actualizar_recurso("energia", -5)

#Eventos que sacrifican suministros para mejorar otros recursos
def repartir_suministros():
    """Evento para mejorar la moral a costa de suministros."""
    print("Has decidido visitar los camarotes para ver a la tripulación.")
    if recursos.moral <= 50:
        print("Observas a la tripulacion desmotivada. Podrias aumentar la racion de hoy para elevar un poco los animos.")
        eleccion = input("¿Deseas aumentar la ración de suministros? (s/n): ").lower()
        while eleccion != 's' and eleccion != 'n':
            print("Opción no válida. Intente de nuevo.")
            eleccion = input("¿Deseas aumentar la ración de suministros? (s/n): ").lower()
        if eleccion == 's':
            print("Has aumentado la ración de suministros, mejorando la moral de la tripulación.")
            recursos.actualizar_recurso("suministros", -5)
            recursos.actualizar_recurso("moral", 5)
        else:
            print("Decides no aumentar la ración de suministros.")
            suerte = random.randint(1, 100)
            if suerte <= 50:
                print("La moral de la tripulación ha disminuido debido a la falta de atención.")
                recursos.actualizar_recurso("moral", -5)
            else:
                print("La moral de la tripulación se mantiene estable.")
    else:
        print("La moral de la tripulación es alta, no es necesario aumentar la ración de suministros.")

#Eventos para ganar combustible
def encontrar_combustible():
    """Evento que otorga combustible."""
    print("¡Has encontrado un depósito de combustible flotando en el espacio!")
    recursos.actualizar_recurso("combustible", 5)

def ganar_combustible_moral():
    """Evento que otorga combustible y moral."""
    print("¡Un miembro de la tripulación ha encontrado una manera de optimizar el uso del combustible!")
    recursos.actualizar_recurso("combustible", 10)
    recursos.actualizar_recurso("moral", 5)
    
def minar_combustible():
    """Evento que permite minar combustible a costa de suministros."""
    print("Has encontrado un asteroide rico en combustible.")
    eleccion = input("¿Deseas minar el combustible? (s/n): ").lower()
    while eleccion != "s" and eleccion != "n":
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("¿Deseas minar el combustible? (s/n): ").lower()
    if eleccion == "s":
        print("Has minado combustible, pero has consumido algunos suministros en el proceso.")
        recursos.actualizar_recurso("combustible", 20)
        recursos.actualizar_recurso("suministros", -5)
        print(f"Tienes disponible {recursos.combustible}% de combustible y {recursos.suministros} de suministros.")
    else:
        print("Decides no minar el combustible.")