import menus
import eventos
import recursos

def main():
        while True:
                menus.principal()
                while recursos.validar_recursos():
                        menus.inicio_dia()
                        menus.in_game_menu()
                        for i in range(menus.eventos_diarios):
                                menus.clear_screen()
                                print(f"=== EVENTO DIARIO ({i + 1} de {menus.eventos_diarios })===")
                                eventos.evento_aleatorio()
                                if not recursos.validar_recursos() :
                                    break
                                menus.in_game_menu()
                        if not recursos.validar_recursos():
                                menus.game_over()
                                break
                        menus.fin_dia()
                        if recursos.distancia_a_destino == 0:
                                menus.victoria()
                                break
                

if __name__ == "__main__":
    main()
    