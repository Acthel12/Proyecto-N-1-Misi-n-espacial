import menus
import eventos
import recursos

def juego():
    """Función principal del juego.
    Aquí se implementaría la lógica del juego."""
    print("El juego ha comenzado...")
    menus.configurar_dificultad()
    while recursos.validar_recursos():
        menus.inicio_dia()
        menus.in_game_menu()
        for i in range(menus.eventos_diarios):
            print(f"=== EVENTO DIARIO ({i + 1} de {menus.eventos_diarios })===")
            eventos.evento_aleatorio()
            menus.in_game_menu()
        menus.fin_dia()