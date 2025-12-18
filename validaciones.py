import constantes


def es_nombre_completo_valido(nombre_apellido: str)-> bool:
    """Chequea que el formato del nombre y apellido sea válido"""

    return 0 < len(nombre_apellido) <= 30 and all(char.isalpha() or char.isspace() for char in nombre_apellido)


def limpiar_dni(dni:str) -> str:
    """Saca los puntos que tiene el DNI"""

    return dni.replace(".", "")


def es_dni_valido(dni: str)-> bool:
    """Chequea que el formato del DNI ingresado sea válido"""

    dni_separado = dni.split(".")

    if len(dni_separado) == 3 and all(parte.isdigit() for parte in dni_separado):

        dni_sin_puntos = limpiar_dni(dni)

        if len(dni_sin_puntos) == 8:

            return True

        return False

    return False


def es_monto_valido(monto: str)-> bool:
    """Chequea que el monto ingresado por el usuario sea válido"""

    if not monto.isdigit():
        return False

    if "." in monto:
        return False

    monto = int(monto)

    if monto < constantes.MONTO_MINIMO:
        return False

    return True


def es_interes_valido(interes: str)-> bool:
    """Chequea que la tasa de interes ingresada sea válida"""

    if not interes.isdigit():

        return False

    interes = int(interes)

    if interes < constantes.TASA_MINIMA:

        return False

    return True
