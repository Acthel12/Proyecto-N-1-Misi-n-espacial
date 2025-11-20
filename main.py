import menus
import eventos
import recursos
import ascii

regresar_al_menu = False

def main():
        """Lógica principal del juego"""
        while True:
                menus.principal()
                while recursos.validar_recursos():
                        menus.inicio_dia()
                        regresar_al_menu = menus.in_game_menu()
                        if regresar_al_menu: 
                                break
                        for i in range(menus.eventos_diarios):
                                menus.clear_screen()
                                print(f"=== EVENTO DIARIO ({i + 1} de {menus.eventos_diarios})===")
                                ascii.evento_diario()
                                eventos.evento_aleatorio()
                                if not recursos.validar_recursos() :
                                    break
                                regresar_al_menu = menus.in_game_menu()
                                if regresar_al_menu:
                                    break
                        eventos.reiniciar_eventos()
                        if regresar_al_menu:
                                break
                        if not recursos.validar_recursos():
                                menus.game_over()
                                break
                        menus.motores()
                        menus.fin_dia()
                        if recursos.distancia_a_destino == 0:
                                menus.victoria()
                                break
                        if not recursos.validar_recursos():
                                menus.game_over()
                                break
                

if __name__ == "__main__":
    main()
    