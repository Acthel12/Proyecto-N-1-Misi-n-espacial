import recursos
import menus

def multiplicador_por_dificultad():
    if menus.dificultad == "Fácil":
        return 0.9
    if menus.dificultad == "Normal":
        return 1
    if menus.dificultad == "Dificil":
        return 1.15

def puntuacion_final():
    """Calcula y devuelve la puntuación final basada en los recursos restantes."""
    p_oxigneo = (recursos.oxigeno * 0.10) / 100
    p_combustible = (recursos.combustible * 0.10) / 100
    p_integridad = (recursos.integridad * 0.30) /100
    p_energia = (recursos.energia * 0.05)/100
    p_dias_restantes = (recursos.dias_restantes * 0.00)
    p_dias_transcurridos = ((100 - recursos.dias_transcurridos) * 0.05) /100 
    p_moral = (recursos. moral * 0.25) / 100
    p_suministros = (recursos.suministros * 0.15)/100
    
    puntuacion_total = p_oxigneo + p_combustible + p_integridad + p_energia + p_dias_restantes + p_dias_transcurridos + p_moral + p_suministros  
    punt = int(puntuacion_total * 1000 * 1)
    
    #diferentes tiopos de meajes para difrentes puntuaciones 
    if punt >= 1150 :
        print(f"Puntuación final: {punt}.")
        print("Su nombre resonará en los pasillos de la flota. "
              "En el silencio entre estrellas, los comandantes recordarán que, "
              "en esta misión, usted hizo lo imposible… y venció.")
    
    elif punt >= 1000:
    
        print(f"Puntuación final: {punt}.")
        print("La misión exigió más de lo que cualquiera habría soportado, "
              "pero usted no cedió. La Alianza reconoce su valor; "
              "su avance marcó el camino para quienes lo seguirán.")

#Esto no se va a utilizar por que  la puntuacion no se ejecuta cuando pierdes, podria cambiarse a un mensaje de que lo lograste a duras penas.
#    elif punt >= 200:
#        # Registro de una Derrota que Habla
#        print(f"Puntuación final: {punt}.")
#        print("El fuego enemigo fue implacable, y la misión se desmoronó ante su intensidad. "
#              "Aun así, sus señales finales servirán como advertencia para la Alianza. "
#              "Incluso en la caída, dejó un mensaje que puede salvar mundos.")

    else:
    
        print(f"Puntuación final: {punt}.")
        print("La ruta fue dura, la sombra del enemigo constante, y aun así logró regresar. "
              "Tal vez no todo salió según lo previsto… pero cada batalla sobrevivida "
              "escribe una nueva línea en la historia.")

