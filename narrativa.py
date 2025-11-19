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
    print("Esquivas rapidamente los interceptores del imperio, luego de un rato, gracias a la maniobrabilidad del spectre logras llegar lejos de la batalla.")
    menus.clear_screen()
    ascii.narrativa()
    print("No se informo la ubicacion de la base que recibiria los planos, solo se indico el sistema estelar destino AXKB-1001.")
    print("Fijas el rumbo a AXKB-1001, y te preparas para tu viaje...")
    input("Presiona Enter para continuar...")


def narrar_segunda_parte():
    ascii.narrativa()
    print("Las alarmas se disparan, advirtiéndote. Estás siendo esperado. El Imperio sabía que escaparían. \nUna flota de reconocimiento imperial liderada por el destructor Venganza Silenciosa emerge de la negrura y te persigue. No quieren una gran batalla, solo capturarlos y los planos.")
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
    print("""De repente, un disparo te alcanza. Sientes cómo el impacto sacude tu nave. El hiperimpulsor está dañado. Tu tripulación se desespera. \nLa distancia se reduce. Vordus está a punto de alcanzarte, pero en ese momento, una señal débil y encriptada llega a tu comunicador. "Necesitan ayuda?" LLega una flota rebelde de tamaño considerable que obliga al general Vordus a retirarse.""")
    print(""""Jaja, una pequeña flota de reconocimiento no podra acabar con las fuerzas del general Kaelen Var". Logras reparar los daños en el hiperpropulsor y te dan una nueva orden: "Volveran con una fuerza de asalto , dirigete a la base secreta en el Planeta Proton-9, nosotros debemos dispersarnos rapidamente" """)
    input("Presiona Enter para continuar...")
    menus.clear_screen()
    ascii.narrativa()
    print("Con las reparaciones de emergencia realizadas y con el destino claro, te diriges rapidamente al planeta Proton-9.")
    input("Presiona Enter para continuar...")

def narrar_cuarta_parte():
    ascii.narrativa()
    print("LLegas al sistema AXKB-1001 hogar del planeta Proton-9. Sabes que el destructor Venganza Silenciosa te sigue de cerca, entrando en el sistema. \nTe falta poco para llegar, tu tripulacion esta ansiosa. Debes llegar rapido a tu destino, antes de que tu sombra, el General Vordus, te encuentre. \nTodo depende de ti.")
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
    ascii.narrativa()
    print("Un pitido lastimero anuncia la sentencia final: los tanques de combustible están vacíos. La fragata pierde velocidad, los motores gimen y se apagan.")
    print("A través de la ventana principal, las luces del Destructor Imperial Venganza Silenciosa se agigantan, sus cañones turboláser brillando con intención asesina.")
    print("La huida ha terminado. Los gritos de tu equipo se ahogan en la desesperación al ver los haces de luz del tractor envolver vuestra nave, inmóvil y condenada.")
    print("Los planos de la Estrella de la Muerte serán recuperados por el Imperio, y tu destino, sellado.")
    print("\n>>> MISIÓN FRACASADA: ATRAPADO Y CAPTURADO")
    input("Presiona Enter para terminar...")

def final_integridad():
    ascii.narrativa()
    print("Escuchas un chirrido agudo, seguido del sonido más aterrador de todos: el del aire escapando. El casco ha cedido bajo el fuego enemigo.")
    print("Las grietas se expanden por la cabina, y la presión interna cae en picada. El frío te envuelve y las luces parpadean por última vez.")
    print("Tu respiración se convierte en escarcha. Ya no hay escape. La nave se desgarra alrededor de tu equipo.")
    print("\n>>> MISIÓN FRACASADA: FRAGATA DESTRUIDA")
    input("Presiona Enter para terminar...")

def final_oxigeno():
    ascii.narrativa()
    print("El indicador de O₂ está en rojo intermitente, una burla cruel. Notas el mareo, la euforia extraña que precede al colapso.")
    print("Intentas enviar un mensaje, pero tus dedos son lentos y pesados. El mundo se vuelve borroso, los colores se distorsionan.")
    print("Lo último que ves es el rostro de tu copiloto, antes de que el sueño eterno del espacio te reclame.")
    print("\n>>> MISIÓN FRACASADA: ASFIXIA EN EL VACÍO")
    input("Presiona Enter para terminar...")

def final_energia():
    ascii.narrativa()
    print("La cabina se sume en una oscuridad total. La energía de los escudos y los motores se ha agotado por completo. Estás a la deriva.")
    print("A lo lejos, las luces del Destructor Venganza Silenciosa te envuelven. Estás indefenso. Capturado.")
    print("Los planos de la Estrella de la Muerte caerán en manos del Imperio. Tu sacrificio fue en vano.")
    print("\n>>> MISIÓN FRACASADA: ENTREGADO AL ENEMIGO")
    input("Presiona Enter para terminar...")

def final_dias():
    ascii.narrativa()
    print("El reloj de la misión ha superado el límite. El punto de encuentro de la Alianza Rebelde ha sido abandonado.")
    print("La flota no podía esperar más. Estás varado, y la transmisión de los planos nunca llegó a tiempo para cambiar el rumbo de la guerra.")
    print("Ahora solo queda la espera, la certeza de que nadie vendrá.")
    print("\n>>> MISIÓN FRACASADA: TARDE PARA EL RESCATE")
    input("Presiona Enter para terminar...")

def final_moral():
    ascii.narrativa()
    print("Los murmullos se convierten en gritos y los gritos en abierta rebelión. Tu equipo ha perdido toda esperanza.")
    print("Un motín estalla en la bodega. La lucha interna por el último escape es brutal y caótica. La misión se ha derrumbado por dentro.")
    print("Con el corazón destrozado, ves cómo el último miembro leal cae. La fragata cae en manos de desertores. El plan Rebelde ha sido traicionado.")
    print("\n>>> MISIÓN FRACASADA: TRAICIÓN Y DESESPERACIÓN")
    input("Presiona Enter para terminar...")

def final_suministros():
    ascii.narrativa()
    print("El último paquete de raciones fue consumido hace días. El cansancio se convierte en agotamiento. La mente se nubla por la sed.")
    print("Ya no puedes operar los controles con precisión. La debilidad te obliga a tumbarte en el suelo frío de la cabina.")
    print("La Resistencia se desvanece contigo. No fue el enemigo quien te derrotó, fue la necesidad más básica.")
    print("\n>>> MISIÓN FRACASADA: AGOTAMIENTO Y HAMBRE")
    input("Presiona Enter para terminar...")

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
    elif opcion == "dias":
        final_dias
    else:
        return
    input("Presione enter para continuar.")