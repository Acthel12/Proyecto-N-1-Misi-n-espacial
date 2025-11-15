oxigeno = 100
combustible = 100
integridad = 100
energia = 100
dias_restantes = 0
dias_transcurridos = 0
moral = 100
suministros = 100
distancia_a_destino = 0 

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

def validar_recursos():
    """Verifica si algún recurso ha llegado a cero o si los días han llegado a su límite."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros

    # Comprobaciones críticas: si cualquiera de estos recursos llega a 0, la misión falla
    if oxigeno <= 0:
        print("Oxígeno agotado. Fin de la misión.")
        return False
    if combustible <= 0:
        print("Combustible agotado. Fin de la misión.")
        return False
    if energia <= 0:
        print("Energía agotada. Fin de la misión.")
        return False
    if integridad <= 0:
        print("Integridad de la nave crítica. Fin de la misión.")
        return False
    if suministros <= 0:
        print("Suministros agotados. Fin de la misión.")
        return False
    if moral <= 0:
        print("Moral de la tripulación completamente baja. Fin de la misión.")
        return False

    # Si los días restantes llegan a 0 después de haber transcurrido al menos un día, la misión termina.
    if dias_restantes <= 0 and dias_transcurridos > 0:
        print("Se han agotado los días de la misión. Fin de la misión.")
        return False

    return True

def actualizar_recurso(recurso, cantidad):
    """Actualiza un recurso específico en una cantidad dada."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros, distancia_a_destino
    
    if recurso == "oxigeno":
        oxigeno = max(0, min(100, oxigeno + cantidad))
        if oxigeno / int(oxigeno) != 1:
            oxigeno = round(oxigeno, 2)
        else:
            oxigeno = int(oxigeno)            
    elif recurso == "combustible":
        combustible = max(0, min(100, combustible + cantidad))
        if combustible / int(combustible) != 1:
            combustible = round(combustible, 2)
        else:
            combustible = int(combustible)
    elif recurso == "energia":
        energia = max(0, min(100, energia + cantidad))
        if energia / int(energia) != 1:
            energia = round(energia, 2)
        else:
            energia = int(energia)
    elif recurso == "integridad":
        integridad = max(0, min(100, integridad + cantidad))
        if integridad / int(integridad) != 1:
            integridad = round(integridad, 2)
        else:
            integridad = int(integridad)
    elif recurso == "dias":
        # Avanzar días: aumentar dias_transcurridos y reducir dias_restantes.
        # cantidad puede ser positiva (avanzar) o negativa (retroceder/corregir).
        dias_transcurridos = max(0, dias_transcurridos + cantidad)
        # Restar los días avanzados de los días restantes; si cantidad es negativa, se suman.
        dias_restantes = max(0, dias_restantes - cantidad)
    elif recurso == "suministros":
        suministros = max(0, min(100, suministros + cantidad))
        if suministros / int(suministros) != 1:
            suministros = round(suministros, 2)
        else:
            suministros = int(suministros)
    elif recurso == "moral":
        moral = max(0, min(100, moral + cantidad))
        if moral / int(moral) != 1:
            moral = round(moral, 2)
        else:
            moral = int(moral)
    elif recurso == "distancia":
        distancia_a_destino = max(0, distancia_a_destino + cantidad)

        
def reiniciar_recursos():
    """Reinicia todos los recursos a sus valores iniciales."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros, distancia_a_destino
    oxigeno = 100
    combustible = 100
    energia = 100
    integridad = 100
    suministros = 100
    dias_restantes = 0
    dias_transcurridos = 0
    moral = 100
    distancia_a_destino = 0