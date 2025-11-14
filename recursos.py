oxigeno = 100
combustible = 100
integridad = 100
energia = 100
dias_restantes = 0
dias_transcurridos = 0
moral = 100
suministros = 100

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
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros
    
    if recurso == "oxigeno":
        oxigeno = max(0, min(100, oxigeno + cantidad))
    elif recurso == "combustible":
        combustible = max(0, min(100, combustible + cantidad))
    elif recurso == "energia":
        energia = max(0, min(100, energia + cantidad))
    elif recurso == "integridad":
        integridad = max(0, min(100, integridad + cantidad))
    elif recurso == "dias":
        # Avanzar días: aumentar dias_transcurridos y reducir dias_restantes.
        # cantidad puede ser positiva (avanzar) o negativa (retroceder/corregir).
        dias_transcurridos = max(0, dias_transcurridos + cantidad)
        # Restar los días avanzados de los días restantes; si cantidad es negativa, se suman.
        dias_restantes = max(0, dias_restantes - cantidad)
    elif recurso == "suministros":
        suministros = max(0, min(100, suministros + cantidad))
    elif recurso == "moral":
        moral = max(0, min(100, moral + cantidad))
        
def reiniciar_recursos():
    """Reinicia todos los recursos a sus valores iniciales."""
    global oxigeno, combustible, energia, integridad, dias_restantes, dias_transcurridos, moral, suministros
    oxigeno = 100
    combustible = 100
    energia = 100
    integridad = 100
    suministros = 100
    dias_restantes = 0
    dias_transcurridos = 0
    moral = 100