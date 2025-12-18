import constantes
import validaciones


def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones"""

    opcion = input(
        constantes.MSG_MENU
    )

    return opcion


def pedir_opcion():
    """Solicita al usuario un numero entero entre 1 y 7.

    La función continua hasta que se ingrese un número válido.

    POSTCONDICIONES:
        - Devuelve una opcion válida del menú o finaliza el programa si la opcion es el 7."""

    while True:

        opcion_elegida = mostrar_menu_principal().strip()

        if opcion_elegida == "**":

            print(constantes.MSG_INPUT_INVALIDO)

            continue

        if not opcion_elegida.isdigit():

            print(constantes.MSG_INPUT_INVALIDO)

            continue

        opcion_elegida = int(opcion_elegida)

        if 0 < opcion_elegida < 8:

            return opcion_elegida

        print(constantes.MSG_INPUT_INVALIDO)


def pedir_nombre_apellido():
    """Solicita al usuario una cadena que puede contener hasta 30 caracteres.

    La función continua hasta que se ingrese una cadena válida.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 1

    POSTCONDICIONES: Retorna una cadena que contiene solo letras y espacios."""

    while True:

        nombre_apellido = input(constantes.MSG_NOMBRE_APELLIDO).strip()

        if nombre_apellido == "**":
            return None

        if validaciones.es_nombre_completo_valido(nombre_apellido):

            return nombre_apellido

        print(constantes.MSG_NOMBRE_INVALIDO)


def pedir_dni(mensaje=constantes.MSG_DNI_POR_DEFECTO):
    """Solicita al usuario un DNI con el formato XX.YYY.ZZZ, donde XX, YYY y ZZZ son valores numéricos.

    La función continua hasta que se ingrese el formato y los caracteres válidos.

    POSTCONDICIONES:
    - `dni` es un entero positivo de 8 digitos sin incluir puntos."""

    while True:

        dni = input(mensaje)

        if dni == "**":
            return None

        if validaciones.es_dni_valido(dni):

            dni_sin_puntos = validaciones.limpiar_dni(dni)

            return int(dni_sin_puntos)

        print(constantes.MSG_DNI_INVALIDO)


def pedir_monto():
    """Solicita al usuario que ingrese un entero.
    La función continua hasta que se ingrese un entero mayor o igual a 100.

    POSTCONDICIONES:
    - `monto` es un entero mayor o igual a 100"""

    while True:
        monto = input(constantes.MSG_INGRESE_MONTO)

        if monto == "**":
            return None

        if validaciones.es_monto_valido(monto):
            return int(monto)

        print(constantes.MSG_MONTO_INVALIDO)



def pedir_interes():
    """Solicita al usuario un entero mayor o igual a 5

    La función continua hasta que el input sea válido.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 4 y posteriormente se debe ingresar un DNI válido.

    POSTCONDICIONES:
    - Devuelve un entero mayor o igual a 5."""

    while True:

        interes = input(constantes.MSG_INGRESE_INTERES)

        if interes == "**":
            return None

        if validaciones.es_interes_valido(interes):

            return int(interes)

        print(constantes.MSG_TASA_INTERES_INVALIDA)


def mostrar_prestamos(usuarios: dict, dni: int):
    """Imprime los prestamos solicitados por el usuario con los siguientes datos:
    ID, monto total del prestamo, tasa de interés,total pendiente a pagar, total de impuestos a pagar,
    capital a pagar, total pagado de impuestos, total pagado de intereses y total pagado del capital.

    PRECONDICIONES:
    - El diccionario `usuarios[dni]` debe contener el diccionario 'prestamos'`

    POSTCONDICIONES:
    - Imprime los préstamos solicitados por el usuario."""

    prestamos = usuarios[dni]["prestamos"]

    for id_prestamo, prestamo in prestamos.items():

        print(
            constantes.PRESTAMO_TEMPLATE.format(
                id_prestamo=id_prestamo,
                monto_total=prestamo["monto_total"],
                tasa_interes=prestamo["tasa_interes"],
                total_pendiente=prestamo["total_pendiente"],
                total_impuestos=prestamo["total_impuestos"],
                total_pagado_impuestos=prestamo["total_pagado_impuestos"],
                total_intereses=prestamo["total_intereses"],
                total_pagado_intereses=prestamo["total_pagado_intereses"],
                capital_total=prestamo["capital_total"],
                total_pagado_capital=prestamo["total_pagado_capital"],
            )
        )


def pedir_monto_prestamo(usuarios: dict, dni: int)-> int:
    """Solicita al usuario un entero mayor a 1.

    La función continua hasta que el input sea mayor o igual a 1 y el saldo del usuario
    sea mayor o igual al monto ingresado.

    PRECONDICIONES:
        - El diccionario `usuarios[dni]` debe contener el diccionario 'prestamos'` y
        se debe haber seleccionado el ID del préstamo a pagar.
    """

    while True:
        monto = input(constantes.MSG_MONTO_A_ABONAR_PRESTAMO)

        if monto == "**":
            return None

        if not monto.isdigit() or "."  in monto:

            print(constantes.MSG_MONTO_INVALIDO)

        else:

            monto = int(monto)

            if monto < constantes.ABONO_MINIMO_PRESTAMO:

                print(constantes.MSG_MONTO_INVALIDO)

            elif monto > usuarios[dni]["saldo"]:

                print(constantes.MSG_SALDO_INSUFICIENTE)

                return None

            else:
                return monto
