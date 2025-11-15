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
                                menus.in_game_menu()
                        menus.fin_dia()


if __name__ == "__main__":
    main()
    