oxigeno = 100
combustible = 100
integridad = 100
dias = 0
moral = 100
suministros = 100

def mostrar_recursos():
    """Muestra los recursos actuales del jugador."""
    print(f"Oxígeno: {oxigeno}%")
    print(f"Combustible: {combustible}%")
    print(f"Energía: {energia}%")
    print(f"Integridad de la nave: {integridad}%")
    print(f"Suministros: {suministros}%")
    print(f"Días restantes: {dias}")
    print(f"Moral de la tripulación: {moral}%")

def validar_recursos():
    """Verifica si algún recurso ha llegado a cero o si los días han llegado a su límite."""
    global oxigeno, combustible, energia, integridad, dias, moral, suministros

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

    return True

def actualizar_recurso(recurso, cantidad):
    """Actualiza un recurso específico en una cantidad dada."""
    global oxigeno, combustible, energia, integridad, dias, moral, suministros
    
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
    elif recurso == "suministros":
        suministros = max(0, min(100, suministros + cantidad))
    elif recurso == "moral":
        moral = max(0, min(100, moral + cantidad))
        
def reiniciar_recursos():
    """Reinicia todos los recursos a sus valores iniciales."""
    global oxigeno, combustible, energia, integridad, dias, moral, suministros
    oxigeno = 100
    combustible = 100
    energia = 100
    integridad = 100
    suministros = 100
    dias = 0
    moral = 100