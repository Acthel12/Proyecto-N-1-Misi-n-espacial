import recursos


def multiplicador_por_dificultad():
    if recursos.dificultad == "Fácil":
        return 0.9
    if recursos.dificultad == "Normal":
        return 1
    if recursos.dificultad == "Difícil":
        return 1.15

def puntuacion_final():
    """Calcula y devuelve la puntuación final basada en los recursos restantes."""
    p_oxigneo = (recursos.oxigeno * 0.10) / 100
    p_combustible = (recursos.combustible * 0.10) / 100
    p_integridad = (recursos.integridad * 0.30) /100
    p_energia = (recursos.energia * 0.05)/100
    p_dias_transcurridos = ((100 - recursos.dias_transcurridos) * 0.05) /100 
    p_moral = (recursos. moral * 0.25) / 100
    p_suministros = (recursos.suministros * 0.15)/100
    
    puntuacion_total = p_oxigneo + p_combustible + p_integridad + p_energia + p_dias_transcurridos + p_moral + p_suministros  
    punt = int(puntuacion_total * 1000 * multiplicador_por_dificultad())
    
    #diferentes tipos de mensajes para diferentes puntuaciones 
    if punt >= 1150 :
        print(f"Puntuación final: {punt}.")
        print("Su nombre resonará en los pasillos de la flota. \n"
              "En el silencio entre estrellas, los comandantes recordarán que, \n"
              "en esta misión, usted hizo lo imposible… y venció.")
    
    elif punt >= 1000:
    
        print(f"Puntuación final: {punt}.")
        print("La misión exigió más de lo que cualquiera habría soportado,\n"
              "pero usted no cedió. La Alianza reconoce su valor;\n"
              "su avance marcó el camino para quienes lo seguirán.")

    else:
    
        print(f"Puntuación final: {punt}.")
        print("La ruta fue dura, la sombra del enemigo constante, y aún así logró regresar. \n"
              "Tal vez no todo salió según lo previsto… pero cada batalla sobrevivida \n"
              "escribe una nueva línea en la historia.")

