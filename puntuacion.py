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
    print ( f"""
su puntuacion total en esta aventura fue de: {int(puntuacion_total) * 100} 
           """)

    