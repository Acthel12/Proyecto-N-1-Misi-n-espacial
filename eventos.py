import random
import recursos

eventos_ocurridos = " "
n = 13 #Número total de eventos disponibles Añadir más eventos y actualizar este número
## Traten de añadir eventos variados , que afecten diferentes recursos y que tengan varias opciones

## Selección aleatoria de eventos Nota: agregar más eventos a medida que se creen eventos y actualizar el valor de n
def añadir_evento(evento):
    """Agrega un evento a la lista de eventos ocurridos."""
    global eventos_ocurridos
    eventos_ocurridos += str(evento) + " "

def reiniciar_eventos():
    """Reinicia la lista de eventos ocurridos."""
    global eventos_ocurridos
    eventos_ocurridos = " "

def evento_aleatorio():
    """Selecciona y ejecuta un evento aleatorio."""
    eventos = random.randint(1,n)
    while eventos_ocurridos.find(str(eventos)) != -1:
        eventos = random.randint(1,n)
    if eventos == 1:
        asteriode_metalico()
        añadir_evento(eventos)
    elif eventos == 2:
        tormenta_cosmica_()
        añadir_evento(eventos)
    elif eventos == 3:
        repartir_suministros()
        añadir_evento(eventos)
    elif eventos == 4:
        tormenta_cosmica_repentina()
        añadir_evento(eventos)
    elif eventos == 5:
        encontrar_combustible()
        añadir_evento(eventos)
    elif eventos == 6:
        ganar_combustible_moral()
        añadir_evento(eventos)
    elif eventos == 7:
        minar_combustible()
        añadir_evento(eventos)
    elif eventos == 8:
        ganar_energia()
        añadir_evento(eventos)
    elif eventos == 9:
        ganar_oxigeno()
        añadir_evento(eventos)
    elif eventos == 10:
        ganar_suministros()
        añadir_evento(eventos)
    elif eventos == 11:
        salto_gravitacional()
        añadir_evento(eventos)
    elif eventos == 12:
        refugio_cosmico()
        añadir_evento(eventos)
    elif eventos == 13:
        abandonar_tripulacion()
        añadir_evento(eventos)
    elif eventos == 14:
        estacion_de_servicio()
        añadir_evento(eventos)
    input("Presiona Enter para continuar...")


## Eventos aleatorios que aumetan los recursos
def asteriode_metalico():
    """Evento que otorga suministros y moral."""
    print("¡Has encontrado un asteroide metálico rico en recursos!")
    recursos.actualizar_recurso("suministros", 15)
    recursos.actualizar_recurso("moral", 15)

def salto_gravitacional():
    """Evento que reduce la distancia restante (avance gratuito)."""
    print("Un campo gravitacional te impulsa cientos de kilómetros hacia adelante.")
    recursos.actualizar_recurso("distancia", 100)

def refugio_cosmico():
    """Evento que otorga moral y reduce días restantes (descanso eficiente)."""
    print("Encuentras un refugio cósmico donde la tripulación descansa bien.")
    opcion = input("¿Deseas aprovechar el refugio para mejorar la moral y reducir un día de viaje? (s/n): ").lower()
    while opcion != 's' and opcion != 'n':
        print("Opción no válida. Intente de nuevo.")
        opcion = input("¿Deseas aprovechar el refugio para mejorar la moral y reducir un día de viaje? (s/n): ").lower()
    if opcion == 'n':
        print("Decides no aprovechar el refugio. La tripulación se siente un poco desanimada.")
        recursos.actualizar_recurso("moral", -25)
    else:
        print("Aprovechas el refugio. La tripulación se siente renovada y descansada.")
        recursos.actualizar_recurso("moral", 25)
        recursos.actualizar_recurso("dias_restantes", -1)

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
            recursos.actualizar_recurso("combustible", -20)
        else:
            print("Has perdido algunos días al esquivar la tormenta.")
            recursos.actualizar_recurso("dias_restantes", -3)
    else:
        suerte = random.randint(1, 100)
        if suerte >= 50:
            print("Has logrado atravesar la tormenta sin daños mayores.")
        else:
            print("La tormenta ha causado daños significativos a tu nave, y a afectado los sistemas electronicos de ella.")
            recursos.actualizar_recurso("integridad", -40)
            recursos.actualizar_recurso("energia", -35)

## Eventos de perdida de recursos
def tormenta_cosmica_repentina():
    """Evento que reduce integridad y energia."""
    print("¡Una tormenta cósmica ha aparecido repentinamente y a dañado tu nave!")
    recursos.actualizar_recurso("integridad", -25)
    recursos.actualizar_recurso("energia", -15)

## Eventos que sacrifican suministros para mejorar otros recursos
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
            recursos.actualizar_recurso("suministros", -40)
            recursos.actualizar_recurso("moral", 40)
        else:
            print("Decides no aumentar la ración de suministros.")
            suerte = random.randint(1, 100)
            if suerte <= 50:
                print("La moral de la tripulación ha disminuido debido a la falta de atención.")
                recursos.actualizar_recurso("moral", -40)
            else:
                print("La moral de la tripulación se mantiene estable.")
    else:
        print("La moral de la tripulación es alta, no es necesario aumentar la ración de suministros.")

def abandonar_tripulacion():
    #Idea de Sara, por abandonarla en la beca XD
    """Evento donde abandonamos parte de la tripulación para ahorrar suministros."""
    print("A habido un problema en la gestion de recursos y se ha decidido que parte de la tripulacion debe abandonar la nave para ahorrar suministros.")
    eleccion = input("¿Deseas que parte de la tripulación abandone la nave? (s/n): ").lower()
    while eleccion != 's' and eleccion != 'n':
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("¿Deseas que parte de la tripulación abandone la nave? (s/n): ").lower()
    if eleccion == 's':
        print("Parte de la tripulación ha abandonado la nave, ahorrando suministros pero reduciendo la moral.")
        recursos.actualizar_recurso("moral", -30)
    else:
        print("Decides no abandonar a la tripulación, La tripulacion se alegra de tu decision y confia mas en ti.")
        print("Sin embargo, los suministros se han vuelto críticos debido a la sobrecarga de la tripulación.")
        recursos.actualizar_recurso("moral", 10)
        recursos.actualizar_recurso("suministros", -40)
          
## Eventos para ganar combustible
def encontrar_combustible():
    """Evento que otorga combustible."""
    print("¡Has encontrado un depósito de combustible flotando en el espacio!")
    recursos.actualizar_recurso("combustible", 25)

def ganar_combustible_moral():
    """Evento que otorga combustible y moral."""
    print("¡Un miembro de la tripulación ha encontrado una manera de optimizar el uso del combustible!")
    recursos.actualizar_recurso("combustible", 20)
    recursos.actualizar_recurso("moral", 20)
    
def minar_combustible():
    """Evento que permite minar combustible a costa de suministros."""
    print("Has encontrado un asteroide rico en combustible.")
    eleccion = input("¿Deseas minar el combustible? (s/n): ").lower()
    while eleccion != "s" and eleccion != "n":
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("¿Deseas minar el combustible? (s/n): ").lower()
    if eleccion == "s":
        print("Has minado combustible, pero has consumido algunos suministros en el proceso.")
        recursos.actualizar_recurso("combustible", 40)
        recursos.actualizar_recurso("suministros", -25)
    else:
        print("Decides no minar el combustible.")

def estacion_de_servicio():
    """Evento que permite restablecer integridad a costa de unos días"""
    print("Te has encontrado con una estacion de servicio aliada, mientras te dispones a recargar algo de combustible rapidamente")
    print("la estacion conciente de tu mision desiden hacer una reparacion gratis, lo malo es que tardaran un par de dias")
    eleccion = input("¿Acepta la reparación? (s/n): ").lower()
    while eleccion != "s" and eleccion != "n":
        print("Opción no válida. Intente de nuevo.")
        eleccion = input("¿Acepta la reparación? (s/n): ").lower()
    if eleccion == "s":
        print("Has aceptado, ademas del combustible reparan tu casco.")
        recursos.actualizar_recurso("combustible", 50)
        recursos.actualizar_recurso("integridad", 50)
        recursos.actualizar_recurso("dias_restantes", -4)
    else:
        print("Has rechazado amablemente la solicitud, no tienes tiempo que perder, te ponen una cantidad basica de combustible")
        recursos.actualizar_recurso("combustible", 25)

## Eventos para ganar recursos
def ganar_energia():
    """Evento que otorga energía."""
    print("¡Has encontrado una fuente de energía renovable en el espacio!")
    recursos.actualizar_recurso("energia", 20)

def ganar_oxigeno():
    """Evento que otorga oxígeno."""
    print("¡Has descubierto una reserva de oxígeno en un asteroide cercano!")
    recursos.actualizar_recurso("oxigeno", 20)

def ganar_suministros():
    """Evento que otorga suministros."""
    print("¡Has encontrado un cargamento abandonado de suministros!")
    recursos.actualizar_recurso("suministros", 20)


