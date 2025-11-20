oxigeno = 100
combustible = 100
integridad = 100
energia = 100
dias_restantes = 0
dias_transcurridos = 0
moral = 100
suministros = 100
distancia_a_destino = 0
distancia_recorrida = 0 
distancia_evento = 0 #Tenia algunas ideas para esto pero al final no lo implementamos lo dejo para un futuro si sigo con este proyecto por los jajas

def mostrar_recursos():
    """Muestra los recursos actuales del jugador."""
    print(f"Oxígeno: {oxigeno}%")
    print(f"Combustible: {combustible}%")
    print(f"Energía: {energia}%")
    print(f"Integridad de la nave: {integridad}%")
    print(f"Suministros: {suministros}%")
    print(f"Días restantes: {dias_restantes}")
    print(f"Días transcurridos: {dias_transcurridos}")
    print(f"Moral de la tripulación: {moral}%")
    print(f"Distancia al destino: {distancia_a_destino} años luz")
    print(f"Distancia recorrida: {distancia_recorrida} años luz")

def validar_recursos():
    """Verifica si algún recurso ha llegado a cero o si los días han llegado a su límite."""

    # Comprobaciones críticas: si cualquiera de estos recursos llega a 0, la misión falla
    if oxigeno <= 0:
        return False
    if combustible <= 0:
        return False
    if energia <= 0:
        return False
    if integridad <= 0:
        return False
    if suministros <= 0:
        return False
    if moral <= 0:
        return False

    # Si los días restantes llegan a 0 después de haber transcurrido al menos un día, la misión termina.
    if dias_restantes <= 0 and dias_transcurridos > 0:
        return False

    return True

def actualizar_recurso(recurso, cantidad):
    """Actualiza un recurso específico en una cantidad dada."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros, distancia_a_destino, distancia_recorrida, distancia_evento
    
    if recurso == "oxigeno":
        oxigeno = max(0, min(100, oxigeno + cantidad))
        if oxigeno - int(oxigeno) != 0:
            oxigeno = round(oxigeno, 2)
        else:
            oxigeno = int(oxigeno)            
    elif recurso == "combustible":
        combustible = max(0, min(100, combustible + cantidad))
        if combustible - int(combustible) != 0:
            combustible = round(combustible, 2)
        else:
            combustible = int(combustible)
    elif recurso == "energia":
        energia = max(0, min(100, energia + cantidad))
        if energia - int(energia) != 0:
            energia = round(energia, 2)
        else:
            energia = int(energia)
    elif recurso == "integridad":
        integridad = max(0, min(100, integridad + cantidad))
        if integridad - int(integridad) != 0:
            integridad = round(integridad, 2)
        else:
            integridad = int(integridad)
    elif recurso == "dias_restantes":
        dias_restantes = max(0, dias_restantes + cantidad)
    elif recurso == "dias":
        # Avanzar días: aumentar dias_transcurridos y reducir dias_restantes.
        # cantidad puede ser positiva (avanzar) o negativa (retroceder/corregir).
        dias_transcurridos = max(0, dias_transcurridos + cantidad)
        # Restar los días avanzados de los días restantes; si cantidad es negativa, se suman.
        dias_restantes = max(0, dias_restantes - cantidad)
    elif recurso == "suministros":
        suministros = max(0, min(100, suministros + cantidad))
        if suministros - int(suministros) != 0:
            suministros = round(suministros, 2)
        else:
            suministros = int(suministros)
    elif recurso == "moral":
        moral = max(0, min(100, moral + cantidad))
        if moral - int(moral) != 0:
            moral = round(moral, 2)
        else:
            moral = int(moral)
    elif recurso == "distancia":
        distancia_a_destino = max(0, distancia_a_destino - cantidad)
        distancia_recorrida = max(0, distancia_recorrida + cantidad)
        if distancia_a_destino - int(distancia_a_destino) != 0:
            distancia_a_destino = round(distancia_a_destino, 2)
        else:
            distancia_a_destino = int(distancia_a_destino)
        if distancia_recorrida - int(distancia_recorrida) != 0:
            distancia_recorrida = round(distancia_recorrida, 2)
        else:
            distancia_recorrida = int(distancia_recorrida)
    elif recurso == "distancia_evento":
        distancia_evento = max(0, distancia_evento + cantidad)

def comprobar_causa_de_gameover():
    """Comprueba qué recurso llegó a 0 y devuelve cuál es el recurso que causó el gameover"""
    if oxigeno <= 0:
        return "oxigeno"
    elif combustible <= 0:
        return "combustible"
    elif energia <= 0:
        return "energia"
    elif integridad <= 0:
        return "integridad"
    elif suministros <= 0:
        return "suministros"
    elif moral <= 0:
        return "moral"
    
    # Si los días restantes llegan a 0 después de haber transcurrido al menos un día, la misión termina.
    elif dias_restantes <= 0 and dias_transcurridos > 0:
        return "dias"
    
    else:
        print("No debió perder el juego, por favor reporte esto al equipo desarrollador")
        print()
        input("Presione enter para continuar.")
        return "none"
        
def reiniciar_recursos():
    """Reinicia todos los recursos a sus valores iniciales."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros, distancia_a_destino, distancia_recorrida, distancia_evento
    oxigeno = 100
    combustible = 100
    energia = 100
    integridad = 100
    suministros = 100
    dias_restantes = 0
    dias_transcurridos = 0
    moral = 100
    distancia_a_destino = 0
    distancia_recorrida = 0 
    distancia_evento = 0

