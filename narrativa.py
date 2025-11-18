 #Funciones para narrar la misión 'Ultimátum Espacial'
import recursos
import ascii
import menus

#Recuerda que la terminal se limpia cada vez que se inicia un menu asi que si quieres que el usuario pueda ver lo que se dice tienes que añadir un input("(mensaje)")
#para que cuando le de a enter, pero esto lo vamos a ver cuando lo implimetemos en menu:

def narrar_primera_parte():
    ascii.narrativa()
    print("Estás en la fragata rebelde Corazón de Alderán junto con tu pequeño equipo de inteligencia. A tu alrededor, solo hay destrucción. El ruido de las alarmas perfora tus oídos y el aire huele a metal fundido. La batalla ha sido perdida.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("El equipo de asalto terrestre o  más bien, lo que queda de él, regresa a la nave con un único superviviente, un Jedi. \nÉl había traído el objetivo a costa de sus compañeros: el Módulo de Datos cifrado Clase Delta. Este contenía los planos completos que revelarían la debilidad del arma de destrucción masiva más reciente del imperio, la estrella de la muerte.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("""Con rapidez, tu y tu equipo acogen al Jedi herido y cansado. Simultáneamente, con mucho pesar, te conectas con el comandante y le explicas la situación, el te dice "ya sabes lo que tienes que hacer, la Alianza cuenta contigo, te deseo suerte." """)
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("Corren. Te abres paso entre escombros y llamas, sabiendo que cada paso es un segundo de vida para millones. Te lanzas junto con tu equipo y el Jedi a la cabina del interceptor, el Spectre, la última nave de escape. Tú eres quien lo pilota.")
    input("Presiona Enter para continuar...")


def narrar_segunda_parte():
    ascii.narrativa()
    print("Apenas has abandonado los restos de la fragata y avanzado un poco a tu destino, las alarmas se disparan, advirtiéndote. Estás siendo esperado. El Imperio sabía que escaparían. \nUna flota de reconocimiento imperial liderada por el destructor Venganza Silenciosa emerge de la negrura y te persigue. No quieren una gran batalla, solo capturarlos y los planos.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("Escuchas la voz fría y autoritaria del General Vordus en tu comunicador, ofreciéndote un ultimátum que sabes que no puedes aceptar. \nTienes poco tiempo, debes entregar los planos antes de que caigan en manos equivocadas.")
    input("Presiona Enter para continuar...")

def narrar_tercera_parte():
    ascii.narrativa()
    print("Estás esquivando. El Venganza Silenciosa te pisa los talones. \nTe obligan a desviarte a través de un denso campo de asteroides, y el destructor ha sembrado el camino con boyas de interdicción para atraparte en el espacio real. Debes pilotar con una precisión de cirujano.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("De repente, un disparo te alcanza. Sientes cómo el impacto sacude tu nave. El hiperimpulsor está dañado. Tu tripulación se desespera. \nLa distancia se reduce. Vordus está a punto de alcanzarte, pero en ese momento, una señal débil y encriptada llega a tu comunicador. \nTe dan una nueva orden: La base de Endor ha sido comprometida. Ve al planeta desconocido Proton-9.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("Debes dirigirte a esta estación de retransmisión abandonada. Tu misión ya no es escapar, sino transmitir los planos desde allí. Es la última carta de la Alianza. Es tu única oportunidad.")
    input("Presiona Enter para continuar...")

def narrar_cuarta_parte():
    ascii.narrativa()
    print("Te precipitas hacia la atmósfera de Proton-9. Sabes que el destructor Venganza Silenciosa te sigue de cerca, entrando en el sistema. \nLlegas al punto crítico: la nave se estabiliza para el aterrizaje. La transmisión debe comenzar ahora, antes de que tu sombra, el General Vordus, te encuentre. \nTodo depende de ti.")
    input("Presiona Enter para continuar...")

def narrar_final():
    ascii.narrativa()
    print("Con un último esfuerzo, logras transmitir los planos de la Estrella de la Muerte a la Alianza Rebelde desde Proton-9. La señal se envía justo cuando el destructor Venganza Silenciosa emerge de la atmósfera, incapaz de detenerte a tiempo.\nLa Alianza ahora tiene la información que necesita para planear un ataque decisivo contra el Imperio. Has cumplido tu misión, y aunque el camino ha sido arduo, tu valentía y determinación han salvado a millones.")
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("¡Felicidades, has completado la misión 'Ultimátum Espacial' con éxito!")
    input("Presiona Enter para continuar...")

def final_combustible():
    pass

def final_integridad():
    pass

def final_oxigeno():
    pass

def final_energia():
    pass

def final_dias():
    pass

def final_moral():
    pass

def final_suministros():
    pass

def narrativa_al_perder():
    opcion = recursos.comprobar_causa_de_gameover()
    if opcion == "combustible":
        final_combustible()
    elif opcion == "integridad":
        final_integridad()
    elif opcion == "dias":
        final_dias()
    elif opcion == "oxigeno":
        final_oxigeno()
    elif opcion == "energia":
        final_energia
    elif opcion == "moral":
        final_moral()
    elif opcion == "suministros":
        final_suministros()
    else:
        return
    input("Presione enter para continuar.")