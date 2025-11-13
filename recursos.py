oxigeno = 100
combustible = 100
energia = 100
integridad = 100
dias = 0
moral = 100

def mostrar_recursos():
    """Muestra los recursos actuales del jugador."""
    print(f"Oxígeno: {oxigeno}%")
    print(f"Combustible: {combustible}%")
    print(f"Energía: {energia}%")
    print(f"Integridad de la nave: {integridad}%")
    print(f"Días restantes: {dias}")
    print(f"Moral de la tripulación: {moral}%")
    
def actualizar_recurso(recurso, cantidad):
    """Actualiza un recurso específico en una cantidad dada."""
    global oxigeno, combustible, energia, integridad, dias, moral
    
    if recurso == "oxigeno":
        oxigeno = max(0, min(100, oxigeno + cantidad))
    elif recurso == "combustible":
        combustible = max(0, min(100, combustible + cantidad))
    elif recurso == "energia":
        energia = max(0, min(100, energia + cantidad))
    elif recurso == "integridad":
        integridad = max(0, min(100, integridad + cantidad))
    elif recurso == "dias":
        dias = max(0, dias + cantidad)
    elif recurso == "moral":
        moral = max(0, min(100, moral + cantidad))
        
def reiniciar_recursos():
    """Reinicia todos los recursos a sus valores iniciales."""
    global oxigeno, combustible, energia, integridad, dias, moral
    oxigeno = 100
    combustible = 100
    energia = 100
    integridad = 100
    dias = 0
    moral = 100