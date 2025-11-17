import recursos

def puntuacion_final():
    """Calcula y devuelve la puntuación final basada en los recursos restantes."""
    p_oxigneo = (recursos.oxigeno * 0.10) / 100
    p_combustible = (recursos.combustible * 0.10) / 100
    p_integridad = (recursos.integridad * 0.25) /100
    p_energia = (recursos.energia * 0.05)
    p_dias_restantes = (recursos.dias_restantes * 0.00)
    p_dias_transcurridos = ((100 - recursos.dias_transcurridos) * 0.05) /100 
    p_moral = (recursos.moral * 0.20) / 100
    p_suministros = (recursos.suministros * 0.15)
    p_distancia_a_destino = (1 - (recursos.distancia_a_destino / 2500) ) * 0.10
    
    puntuacion_total = p_oxigneo + p_combustible + p_integridad + p_energia + p_dias_restantes + p_dias_transcurridos + p_moral + p_suministros + p_distancia_a_destino  
    punt = puntuacion_total
    
    #diferentes tiopos de meajes para difrentes puntuaciones 
    if punt >= 1500 :
        print(f"Puntuación final: {punt}.")
        print("Su nombre resonará en los pasillos de la flota. "
              "En el silencio entre estrellas, los comandantes recordarán que, "
              "en esta misión, usted hizo lo imposible… y venció.")
    
    elif punt >= 800:
    
        print(f"Puntuación final: {punt}.")
        print("La misión exigió más de lo que cualquiera habría soportado, "
              "pero usted no cedió. La Alianza reconoce su valor; "
              "su avance marcó el camino para quienes lo seguirán.")

    elif punt >= 200:
        # Registro de una Derrota que Habla
        print(f"Puntuación final: {punt}.")
        print("El fuego enemigo fue implacable, y la misión se desmoronó ante su intensidad. "
              "Aun así, sus señales finales servirán como advertencia para la Alianza. "
              "Incluso en la caída, dejó un mensaje que puede salvar mundos.")

    else:
    
        print(f"Puntuación final: {punt}.")
        print("La ruta fue dura, la sombra del enemigo constante, y aun así logró regresar. "
              "Tal vez no todo salió según lo previsto… pero cada batalla sobrevivida "
              "escribe una nueva línea en la historia.")

    