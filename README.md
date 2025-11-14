# Proyecto-N-1 — Misi-n espacial

Proyecto Nº1: simulador sencillo de gestión de recursos para una misión espacial.

Descripción
- Juego/simulador en el que se controlan recursos de una nave (oxígeno, combustible, energía, integridad, suministros, moral) y se gestionan días de misión.

Requisitos
- Python 3.8+ (recomendado)
- No hay dependencias externas obligatorias para el núcleo (archivo recursos.py).

Instalación
- Clona este repositorio y sitúate en la carpeta del proyecto:
  - git clone <repositorio>
  - cd "c:\Users\Usuario\Documents\Proyectos\Proyecto-N-1-Misi-n-espacial"

Ejecución
- Si tienes un script principal (por ejemplo `main.py`), ejecútalo con:
  - python main.py
- Para probar las funciones de recursos desde REPL o un script:
  - from recursos import mostrar_recursos, actualizar_recurso, validar_recursos, reiniciar_recursos
  - mostrar_recursos()

Estructura del proyecto
- recursos.py — Lógica y estado de los recursos de la misión.
  - Variables principales: oxigeno, combustible, energia, integridad, suministros, moral, dias_restantes, dias_transcurridos
  - Funciones:
    - mostrar_recursos(): imprime el estado actual de los recursos.
    - validar_recursos(): verifica condiciones de fallo (recursos a 0 o días agotados).
    - actualizar_recurso(recurso, cantidad): modifica recursos; para avanzar días usar recurso "dias".
    - reiniciar_recursos(): restablece los valores iniciales.
- README.md — (este archivo) documentación básica.

Uso rápido (ejemplos)
- Avanzar 1 día:
  - actualizar_recurso("dias", 1)
- Reducir oxígeno en 10:
  - actualizar_recurso("oxigeno", -10)
- Mostrar estado:
  - mostrar_recursos()
- Comprobar si la misión continúa:
  - if not validar_recursos(): print("Misión finalizada")

