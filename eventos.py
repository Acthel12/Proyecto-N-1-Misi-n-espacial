import random
import recursos
import ascii
import os

eventos_ocurridos = " "
n = 24 #Número total de eventos disponibles

## Selección aleatoria de eventos. Nota: agregar más eventos a medida que se creen eventos y actualizar el valor de n
def añadir_evento(evento):
    """Agrega un evento a la lista de eventos ocurridos."""
    global eventos_ocurridos
    eventos_ocurridos += str(evento) + " "

def reiniciar_eventos():
    """Reinicia la lista de eventos ocurridos."""
    global eventos_ocurridos
    eventos_ocurridos = " "

def clear_screen():
    """Limpia la pantalla de la consola."""
    if os.name == 'nt':  # Revisa si el sistema operativo es Windows
        os.system('cls')
    else:  # Asume que es un sistema tipo Unix (Linux, macOS)
        os.system('clear')

def evento_aleatorio(i):
    """Selecciona y ejecuta un evento aleatorio."""
    eventos = random.randint(1,n)
    while eventos_ocurridos.find(str(eventos)) != -1:
        eventos = random.randint(1,n)
    while True:
        clear_screen()
        print(f"=== EVENTO DIARIO ({i + 1} de {recursos.eventos_diarios})===")
        ascii.evento_diario()
        if eventos == 1:
            if not asteroide_metalico():
                continue
            añadir_evento(eventos)
        elif eventos == 2:
            if not tormenta_cosmica_():
                continue
            añadir_evento(eventos)
        elif eventos == 3:
            if not repartir_suministros():
                continue
            añadir_evento(eventos)
        elif eventos == 4:
            if not tormenta_cosmica_repentina():
                continue
            añadir_evento(eventos)
        elif eventos == 5:
            if not encontrar_combustible():
                continue
            añadir_evento(eventos)
        elif eventos == 6:
            if not ganar_combustible_moral():
                continue
            añadir_evento(eventos)
        elif eventos == 7:
            if not minar_combustible():
                continue
            añadir_evento(eventos)
        elif eventos == 8:
            if not ganar_energia():
                continue
            añadir_evento(eventos)
        elif eventos == 9:
            if not ganar_oxigeno():
                continue
            añadir_evento(eventos)
        elif eventos == 10:
            if not ganar_suministros():
                continue
            añadir_evento(eventos)
        elif eventos == 11:
            if not salto_gravitacional():
                continue
            añadir_evento(eventos)
        elif eventos == 12:
            if not refugio_cosmico():
                continue
            añadir_evento(eventos)
        elif eventos == 13:
            if not abandonar_tripulacion():
                continue
            añadir_evento(eventos)
        elif eventos == 14:
            if not estacion_de_servicio():
                continue
            añadir_evento(eventos)
        elif eventos == 15:
            if not asalto_enemigo():
                continue
            añadir_evento(eventos)
        elif eventos == 16:
            if not drones_hostiles():
                continue
            añadir_evento(eventos)
        elif eventos == 17:
            if not ataque_pirata():
                continue
            añadir_evento(eventos)
        elif eventos == 18:
            if not falla_navegacion():
                continue
            añadir_evento(eventos)
        elif eventos == 19:
            if not destructor_alienigena():
                continue
            añadir_evento(eventos)
        elif eventos == 20:
            if not tormenta_particulas():
                continue
            añadir_evento(eventos)
        elif eventos == 21:
            if not fuente_energia_desconocida():
                continue
            añadir_evento(eventos)
        elif eventos == 22:
            if not cortocircuito_sistemas():
                continue
            añadir_evento(eventos)
        elif eventos == 23:
            if not energia_cometa():
                continue
            añadir_evento(eventos)
        elif eventos == 24:
            if not dron_imperio():
                continue
            añadir_evento(eventos)
        break
    print()
    input("Presiona Enter para continuar...")
    


## Eventos aleatorios que aumentan los recursos
def asteroide_metalico():
    """Evento que otorga suministros y moral."""
    print("¡Has encontrado un asteroide metálico rico en recursos!")
    recursos.actualizar_recurso("suministros", 15)
    recursos.actualizar_recurso("moral", 15)
    return True

def salto_gravitacional():
    """Evento que reduce la distancia restante (avance gratuito)."""
    print("Un campo gravitacional te impulsa cientos de kilómetros hacia adelante.")
    recursos.actualizar_recurso("distancia", 100)
    return True

def refugio_cosmico():
    """Evento que otorga moral y reduce días restantes (descanso eficiente)."""
    print("Encuentras un refugio cósmico donde la tripulación descansa bien.")
    print()
    opcion = input("¿Deseas aprovechar el refugio para mejorar la moral y reducir un día de viaje? (s/n): ").lower()
    if opcion == 'n':
        print("Decides no aprovechar el refugio. La tripulación se siente un poco desanimada.")
        recursos.actualizar_recurso("moral", -25)
        return True
    elif opcion == 's':
        print("Aprovechas el refugio. La tripulación se siente renovada y descansada.")
        recursos.actualizar_recurso("moral", 25)
        recursos.actualizar_recurso("dias_restantes", -1)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

#Eventos aleatorios que reducen los recursos
def tormenta_cosmica_():
    """Evento que reduce integridad o suministros."""
    print("¡En el camino te has topado con una tormenta cósmica!")
    print()
    eleccion = input("¿Deseas esquivarla (1) o atravesarla (2)? ")
    
    if eleccion == '1':
        recurso = random.choice("cd")
        if recurso == "c":
            print("Has perdido algo de combustible al esquivar la tormenta.")
            recursos.actualizar_recurso("combustible", -20)
        else:
            print("Has perdido algunos días al esquivar la tormenta.")
            recursos.actualizar_recurso("dias_restantes", -3)
        return True
    elif eleccion == '2':
        suerte = random.randint(1, 100)
        if suerte >= 50:
            print("Has logrado atravesar la tormenta sin daños mayores.")
        else:
            print("La tormenta ha causado daños significativos a tu nave, y ha afectado sus sistemas electrónicos.")
            recursos.actualizar_recurso("integridad", -40)
            recursos.actualizar_recurso("energia", -35)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

## Eventos de pérdida de recursos
def tormenta_cosmica_repentina():
    """Evento que reduce integridad y energía."""
    print("¡Una tormenta cósmica ha aparecido repentinamente y ha dañado tu nave!")
    recursos.actualizar_recurso("integridad", -25)
    recursos.actualizar_recurso("energia", -15)
    return True

## Eventos que sacrifican determinados suministros para mejorar otros recursos
def repartir_suministros():
    """Evento para mejorar la moral a costa de suministros."""
    print("Has decidido visitar los camarotes para ver a la tripulación.")
    if recursos.moral <= 50:
        print("Observas a la tripulación desmotivada. Podrías aumentar la ración de suministros de hoy para elevar un poco los ánimos.")
        print()
        eleccion = input("¿Deseas aumentar la ración de suministros? (s/n): ").lower()
        
        if eleccion == 's':
            print("Has aumentado la ración de suministros, mejorando la moral de la tripulación.")
            recursos.actualizar_recurso("suministros", -40)
            recursos.actualizar_recurso("moral", 40)
            return True
        elif eleccion == 'n':
            print("Decides no aumentar la ración de suministros.")
            suerte = random.randint(1, 100)
            if suerte <= 50:
                print("La moral de la tripulación ha disminuido debido a la falta de atención.")
                recursos.actualizar_recurso("moral", -40)
            else:
                print("La moral de la tripulación se mantiene estable.")
            return True
        else:
            input("Opción no válida. Presiona Enter para continuar...")
            return False
    else:
        print("La moral de la tripulación es alta, no es necesario aumentar la ración de suministros.")
        return True

def abandonar_tripulacion():
    """Evento donde abandonamos parte de la tripulación para ahorrar suministros."""
    print("Ha habido un problema en la gestión de recursos y se ha decidido que parte de la tripulación debe abandonar la nave para ahorrar suministros.")
    print()
    eleccion = input("¿Deseas que parte de la tripulación abandone la nave? (s/n): ").lower()
    
    if eleccion == 's':
        print("Parte de la tripulación ha abandonado la nave, ahorrando suministros pero reduciendo la moral.")
        recursos.actualizar_recurso("moral", -30)
        return True
    elif eleccion == 'n':
        print("Decides no abandonar a la tripulación, La tripulación se alegra de tu decisión y confía más en ti.")
        print("Sin embargo, los suministros se han vuelto críticos debido a la sobrecarga de la tripulación.")
        recursos.actualizar_recurso("moral", 10)
        recursos.actualizar_recurso("suministros", -40)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False
          
## Eventos para ganar combustible
def encontrar_combustible():
    """Evento que otorga combustible."""
    print("¡Has encontrado un depósito de combustible flotando en el espacio!")
    recursos.actualizar_recurso("combustible", 25)
    return True

def ganar_combustible_moral():
    """Evento que otorga combustible y moral."""
    print("¡Un miembro de la tripulación ha encontrado una manera de optimizar el uso del combustible!")
    recursos.actualizar_recurso("combustible", 20)
    recursos.actualizar_recurso("moral", 20)
    return True
    
def minar_combustible():
    """Evento que permite minar combustible a costa de suministros."""
    print("Has encontrado un asteroide rico en combustible.")
    print()
    eleccion = input("¿Deseas minar el combustible? (s/n): ").lower()
    
    if eleccion == "s":
        print("Has minado combustible, pero has consumido algunos suministros en el proceso.")
        recursos.actualizar_recurso("combustible", 40)
        recursos.actualizar_recurso("suministros", -25)
        return True
    elif eleccion == "n":
        print("Decides no minar el combustible.")
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

def estacion_de_servicio():
    """Evento que permite restablecer integridad a costa de unos días"""
    print("Te has encontrado con una estación de servicio aliada, mientras te dispones a recargar algo de combustible rápidamente")
    print("Consciente de tu situación, la estación decide hacer una reparación gratis, lo negativo es que tardarán un par de días en hacerlo.")
    print()
    eleccion = input("¿Aceptas la reparación? (s/n): ").lower()
    
    if eleccion == "s":
        print("Has aceptado, además del combustible repararán tu casco.")
        recursos.actualizar_recurso("combustible", 50)
        recursos.actualizar_recurso("integridad", 50)
        recursos.actualizar_recurso("dias_restantes", -4)
        return True
    elif eleccion == "n":
        print("Has rechazado amablemente la solicitud, no tienes tiempo que perder, te surten una cantidad básica de combustible")
        recursos.actualizar_recurso("combustible", 25)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

## Eventos para ganar recursos
def ganar_energia():
    """Evento que otorga energía."""
    print("¡Has encontrado una fuente de energía renovable en el espacio!")
    recursos.actualizar_recurso("energia", 20)
    return True

def ganar_oxigeno():
    """Evento que otorga oxígeno."""
    print("¡Has descubierto una reserva de oxígeno en un asteroide cercano!")
    recursos.actualizar_recurso("oxigeno", 20)
    return True

def ganar_suministros():
    """Evento que otorga suministros."""
    print("¡Has encontrado un cargamento abandonado de suministros!")
    recursos.actualizar_recurso("suministros", 20)
    return True



#eventos de batalla

#asalto a la nave

def asalto_enemigo():
    """Evento donde enemigos abordan la nave."""
    print("¡Un grupo enemigo ha abordado tu nave!")
    print("La tripulación está luchando por defenderse.")

    recursos.actualizar_recurso("suministros", -25)
    recursos.actualizar_recurso("moral", -20)

    print("Los enemigos robaron suministros.")
    print("La moral de la tripulación ha bajado.")

    azar = random.randint(1, 2)

    if azar == 1:
        print("Logras expulsar a los invasores.")
        recursos.actualizar_recurso("moral", 20)
    else:
        print("Los invasores escaparon sin ser detenidos.")
    return True

#emboscada de drones

def drones_hostiles():
    """Evento donde drones hostiles atacan la nave."""
    print("Unos drones hostiles aparecen alrededor de tu nave.")
    print("No puedes evitar el ataque.")

    recursos.actualizar_recurso("integridad", -20)
    recursos.actualizar_recurso("energia", -20)

    print("Los drones atacaron tu nave.")
    print("Perdiste integridad y energía.")

    azar = random.randint(1, 3)

    if azar == 1:
        recursos.actualizar_recurso("suministros", 25)
        print("Destruiste un dron y recuperaste piezas útiles.")
    return True

#ataque pirata espacial

def ataque_pirata():
    """Evento en donde unos piratas espaciales atacan la nave."""
    print("¡Unos piratas espaciales están atacando tu nave!")
    print("1. Pelear")
    print("2. Huir")
    print()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        suerte = random.randint(1,100)
        print("Decidiste pelear contra los piratas.")
        if suerte > 80:
            print("Por suerte los piratas no estuvieron preparados y no fueron rival para ti y tu nave.")
            recursos.actualizar_recurso("energia", -20)
            recursos.actualizar_recurso("suministros", 20)
            print("Lograste conseguir algunos suministros de sus restos.")
        elif suerte >= 35:
            print("Luego de una larga batalla, logras hacerte con la victoria sin recibir mucho daño en tu casco")
            print("Recuperas algunos suministros de los restos flotantes en el campo de batalla")
            recursos.actualizar_recurso("energia", -20)
            recursos.actualizar_recurso("integridad", -25)
            recursos.actualizar_recurso("suministros", 15)
        elif suerte > 10:
            print("Los piratas eran desertores del Imperio con tecnología avanzada")
            print("La batalla estuvo difícil pero lograste hacerte con la victoria")
            print("Recuperas algunos suministros de los restos flotantes en el campo de batalla")
            recursos.actualizar_recurso("energia", -35)
            recursos.actualizar_recurso("integridad", -50)
            recursos.actualizar_recurso("suministros", 30)
        else:
            print("Has perdido la batalla y tuviste que huir rápidamente")
            recursos.actualizar_recurso("integridad",-50)
            recursos.actualizar_recurso("energia", -35)
            recursos.actualizar_recurso("combustible", -20)
        return True
    elif opcion == "2":
        print("Decides huir rápidamente.")
        recursos.actualizar_recurso("combustible", -20)
        print("Gastaste combustible para escapar.")
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

#falla navegación

def falla_navegacion():
    """Evento que reduce energía y puede causar perdida de días."""
    print("¡Ha ocurrido una falla en el sistema de navegación!")
    print("El sistema te pide que elijas entre reiniciar o intentar reparar manualmente.")
    print()
    eleccion = input("¿Reiniciar sistema (1) o reparar manualmente (2)?: ")

    if eleccion == "1":
        print("Reiniciaste el sistema, pero consumió energía.")
        recursos.actualizar_recurso("energia", -20)
        return True
    elif eleccion == "2":
        print("Intentas repararlo manualmente, pero tardas varios días.")
        recursos.actualizar_recurso("dias_restantes", -3)
        recursos.actualizar_recurso("energia", -10)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False


#destructor alienígena

def destructor_alienigena():
    """Enfrentas un destructor alienígena"""
    print("¡Un destructor alienígena se dispone a abrir fuego contra tu nave!")
    print()
    eleccion = input("¿Usar escudos (1) o atacar directamente (2)?: ")

    if eleccion == "1":
        recursos.actualizar_recurso("energia", -20)
        suerte = random.randint(1, 100)
        if suerte >= 50:
            print("¡Absorbes parte del ataque y la nave enemiga se retira! Pierdes energía, pero ganas moral!")
            recursos.actualizar_recurso("moral", 15)
        else:
            print("Los escudos fallan parcialmente y recibes daño.")
            recursos.actualizar_recurso("integridad", -35)
        return True
    elif eleccion == "2":
        suerte = random.randint(1, 100)
        if suerte >= 70:
            print("¡Ataque directo exitoso! La nave enemiga cae y recuperas suministros y combustible!")
            recursos.actualizar_recurso("suministros", 35)
            recursos.actualizar_recurso("combustible", 30)
        else:
            print("El ataque falla parcialmente y tu nave recibe daño.")
            recursos.actualizar_recurso("integridad", -30)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

#tormenta de partículas

def tormenta_particulas():
    """Una tormenta de partículas puede dañar o cargar tu nave según cómo reacciones."""
    print("¡Una tormenta de partículas se aproxima!")
    print()
    eleccion = input("¿Activar escudos (1) o canalizar energía para cargar la nave (2)?: ")
    
    if eleccion == '1':
        print("Proteges la nave, pero consumes energía de los escudos.")
        recursos.actualizar_recurso("energia", -30)
        return True
    elif eleccion == '2':
        suerte = random.randint(1, 100)
        if suerte >= 60:
            print("¡La tormenta carga parcialmente tus sistemas! Obtienes energía extra.")
            recursos.actualizar_recurso("energia", 30)
        else:
            print("Intentas cargar energía, pero la tormenta causa daños graves.")
            recursos.actualizar_recurso("energia", -25)
            recursos.actualizar_recurso("integridad", -20)
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

#fuente de energía desconocida

def fuente_energia_desconocida():
    """Encuentras una fuente de energía inestable."""
    print("¡Has encontrado una fuente de energía desconocida flotando en el espacio!")
    print()
    eleccion = input("¿Deseas conectarte y extraer energía (s/n)?: ").lower()
    
    if eleccion == 's':
        suerte = random.randint(1, 100)
        if suerte >= 40:
            print("¡Éxito! La nave obtiene energía extra sin problemas.")
            recursos.actualizar_recurso("energia", 30)
        else:
            print("La fuente era inestable, tu nave sufre daños al intentar extraer energía.")
            recursos.actualizar_recurso("energia", -20)
            recursos.actualizar_recurso("integridad", -15)
        return True
    elif eleccion == 'n':
        print("Decides no arriesgarte y continúas tu viaje.")
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False



#corto circuito en los sistemas

def cortocircuito_sistemas():
    """Un fallo eléctrico reduce la energía de la nave."""
    print("¡Un cortocircuito en los sistemas eléctricos reduce tu energía!")
    recursos.actualizar_recurso("energia", -30)
    print("Se ha reducido un '30%' de energía debido al cortocircuito.")
    return True


#energía de un cometa



def energia_cometa():
    """Un cometa cercano emite partículas que tu nave puede aprovechar."""
    print("¡Un cometa pasa cerca de tu nave y emite partículas energéticas!")
    print()
    eleccion = input("¿Deseas aprovechar la energía del cometa (s/n)?: ").lower()
    
    if eleccion == 's':
        suerte = random.randint(1,100)
        if suerte >= 65:
            print("¡Exitoso! Obtienes un buen aumento de energía.")
            recursos.actualizar_recurso("energia", 45)
        elif suerte >= 35:
            print("No fuiste lo suficientemente rápido para alcanzar el cometa.")
            recursos.actualizar_recurso("moral",-10)
        else:
            print("Un mal cálculo hace que el cometa choque con la nave y la dañe un poco.")
            recursos.actualizar_recurso("integridad", -15)
        return True
    elif eleccion == 'n':
        print("Decides no arriesgarte. Continúas tu viaje sin cambios.")
        return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False

def dron_imperio():
    """Evento de pelea con un dron de reconocimiento que puede afectar los días y la integridad"""
    print("Te consigues un dron de reconocimiento del Imperio, patrullando la zona")
    print("Si te descubre la flota podría alcanzarte antes de lo que esperabas; por eso decides esconderte")
    print("Pero podrías destruirlo y retrasar el avance de la flota un tiempo")
    print()
    opcion = input("¿Qué decides, lo destruirás (s/n)?: ").lower()
    
    suerte = random.randint(1,100)
    
    if opcion == "s":
        if suerte >= 50:
            print("Logras acertarle un golpe crítico, con esto el Imperio tardará en comprobar esta zona.")
            recursos.actualizar_recurso("dias_restantes", 4)
        elif suerte >= 25:
            print("El dron de reconocimiento tenía armas y te causó un poco de daño antes de ser destruido.")
            recursos.actualizar_recurso("dias_restantes", 4)
            recursos.actualizar_recurso("integridad", -15)
        else:
            print("Antes de que alcanzaras el dron, este logra huir. Ahora tienes menos tiempo antes que el imperio te localice")
            recursos.actualizar_recurso("dias_restantes", -4)
        return True
    elif opcion == "n":
            print("Te escondes en un cinturón de asteroides cercano.")
            print("El dron luego de un día se va y te deja la vía libre")
            recursos.actualizar_recurso("dias_restantes", 1)
            return True
    else:
        input("Opción no válida. Presiona Enter para continuar...")
        return False