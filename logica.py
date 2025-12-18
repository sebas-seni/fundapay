import constantes
import usuario

def crear_diccionario(usuarios: dict, dni: int , nombre: str):
    """Crea un diccionario asociado al dni del usuario que crea la cuenta,
    con los campos 'nombre' y 'saldo'.

    PRECONDICIONES:
    - Se debe haber ingresado un nombre y DNI valido."""

    usuarios[dni] = {"nombre": nombre, "saldo": 0}
    print(constantes.MSG_CUENTA_CREADA)


def crear_cuenta(usuarios: dict):
    """Solicita al usuario un nombre, apellido y DNI válidos.

    PRECONDICIONES:
    -`pedir_opcion()` debe retornar 1

    POSTCONDICIONES:
    - Si previamente no existe la cuenta, se crea un diccionario `usuarios[dni]`
    que contiene el nombre, apellido y saldo en cuenta del usuario.
     """

    nombre = usuario.pedir_nombre_apellido()

    if not nombre:
        return

    dni = usuario.pedir_dni()

    if dni is None:
        return

    if dni in usuarios:

        print(constantes.MSG_CUENTA_EXISTE.format(nombre=usuarios[dni]["nombre"]))

    else:
        crear_diccionario(usuarios, dni, nombre)


def aumentar_saldo(usuarios: dict, dni: int, monto: int):
    """Aumenta el saldo asociado al DNI según el monto ingresado

    PRECONDICIONES:
    - La cuenta debe estar creada.
    - Se debe ingresar un DNI válido
    - El monto debe ser válido


    #Ver si agrego post

    """

    usuarios[dni]["saldo"] += monto


def ingresar_dinero(usuarios: dict):
    """Solicita un DNI y un monto válido.

    PRECONDICIONES:
    -  `pedir_opcion()` debe retornar 2.

    POSTCONDICIONES:
    - Si existe el diccionario `usuarios[dni]` y el monto es válido, aumenta el saldo de la cuenta.
    - Imprime el mensaje 'Los ${monto} fueron acreditados en la cuenta de {nombre} correctamente'"""

    dni = usuario.pedir_dni()

    if dni is None:
        return

    if dni in usuarios:

        monto = usuario.pedir_monto()

        if monto is None:
            return

        aumentar_saldo(usuarios, dni, monto)

        print(
            constantes.MSG_INGRESO_ACREDITADO.format(
                monto=monto, nombre=usuarios[dni]["nombre"]
            )
        )
    else:
        print(constantes.MSG_NO_EXISTE_CUENTA)


def crear_campo_transferencia(usuarios, dni_origen, dni_destino, monto):
    """Crea una lista dentro de `usuarios[dni_origen]` y `usuarios[dni_destino]` llamada 'transferencias'.
    A la lista dentro de `usuarios[dni_origen]` y `usuarios[dni_destino]`
    se agrega un diccionario con el tipo de transferencia, el monto de la misma,
    el dni de quien o a quien mando la transferencia respectivamente y el nombre de quien o a quien
    mando la transferencia respectivamente.

    PRECONDICIONES:
    - Al menos dos cuentas deben haber sido creadas correctamente.

    POSTCONDICIONES:
    - Los usuarios involucrados contienen una lista con los datos de la transferencia."""
    usuarios[dni_origen].setdefault("transferencias", [])
    usuarios[dni_destino].setdefault("transferencias", [])

    transferencias_origen = usuarios[dni_origen]["transferencias"]

    transferencias_destino = usuarios[dni_destino]["transferencias"]

    transferencias_origen.append(
        {
            "tipo": "saliente",
            "monto": monto,
            "dni_origen": dni_origen,
            "dni_destino": dni_destino,
            "nombre": usuarios[dni_destino]["nombre"],
        }
    )

    transferencias_destino.append(
        {
            "tipo": "entrante",
            "monto": monto,
            "dni_origen": dni_origen,
            "dni_destino": dni_destino,
            "nombre": usuarios[dni_origen]["nombre"],
        }
    )


def manejar_saldo_transferencia(usuarios, dni_origen, dni_destino, monto):
    """Resta el saldo a la cuenta la cual transfirió el dinero (cuenta de origen) y aumenta el saldo
    de la cuenta a la cual fue transferido el dinero (cuenta de destino)

    PRECONDICIONES:
    - Ambas cuentas deben existir
    - Ambos DNI deben ser válidos
    - El monto debe ser válido
    """

    usuarios[dni_origen]["saldo"] -= monto
    usuarios[dni_destino]["saldo"] += monto


def transferir_dinero(usuarios: dict):
    """Solicita al usuario el dni de quien transfiere y hacia quien transfiere.
    Posteriormente se solicita el monto de la transferencia, el cual debe estar disponible en el saldo de la cuenta.
    Si los datos son correctos, se resta el monto en la cuenta de origen y se suman en la cuenta de destino.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 3.

    POSTCONDICIONES:
    - Se crea el diccionario con los datos de la transferencia
    - El saldo de la cuenta de origen disminuye y la de destino aumenta segun el monto ingresado.
    - Se imprime el mensaje:
    'Los ${monto} fueron transferidos desde la cuenta de {nombre_origen} a la de {nombre_destino} correctamente'"""

    dni_origen = usuario.pedir_dni("Ingrese DNI origen: ")

    if dni_origen is None:
        return

    if not dni_origen in usuarios:

        print(constantes.MSG_NO_EXISTE_CUENTA)

        return


    dni_destino = usuario.pedir_dni("Ingrese DNI destino: ")

    if dni_destino is None:
        return

    if not dni_destino in usuarios:

        print(constantes.MSG_NO_EXISTE_CUENTA)
        return

    monto = usuario.pedir_monto()

    if monto is None:
        return

    if usuarios[dni_origen]["saldo"] < monto:

        print(constantes.MSG_MONTO_NO_DISPONIBLE)
        return

    manejar_saldo_transferencia(usuarios, dni_origen, dni_destino, monto)

    crear_campo_transferencia(usuarios, dni_origen, dni_destino, monto)

    print(
        constantes.MSG_TRANSFERENCIA_EXITOSA.format(
            monto=monto,
            nombre_origen=usuarios[dni_origen]["nombre"],
            nombre_destino=usuarios[dni_destino]["nombre"],
        )
    )


def calcular_intereses_impuestos(monto: int, tasa_interes: int)-> tuple[int, int , int]:
    """Calcula los interses e impuestos del préstamo

    PRECONDICIONES:
    - El monto debe ser válido
    - La tasa de interés debe ser válida
    """

    total_intereses = monto * tasa_interes // 100

    impuestos = int(monto * 0.2)

    monto_con_interes = (100 + tasa_interes) * monto // 100

    return total_intereses, impuestos, monto_con_interes

def crear_campo_prestamo(usuarios: dict, dni: int, monto: int, tasa_interes: int):
    """Aumenta el saldo de la cuenta según el monto seleccionado.
    Se crea el campo de 'prestamos' con su respectivo ID e información.

    PRECONDICIONES:
    - Debe existir la cuenta
    - El monto debe ser válido
    - La tasa de interés debe ser válida
    """

    total_intereses, impuestos, monto_con_interes = calcular_intereses_impuestos(monto, tasa_interes)

    usuarios[dni]["saldo"] += monto

    if "prestamos" not in usuarios[dni]:
        usuarios[dni]["prestamos"] = {}

    prestamos = usuarios[dni]["prestamos"]

    id_prestamo = len(prestamos) + 1

    prestamos[id_prestamo] = {
        "monto_total": monto_con_interes + impuestos,
        "tasa_interes": tasa_interes,
        "total_pendiente": monto_con_interes + impuestos,
        "total_impuestos": impuestos,
        "total_pagado_impuestos": 0,
        "total_intereses": total_intereses,
        "total_pagado_intereses": 0,
        "capital_total": monto,
        "total_pagado_capital": 0,
    }


def otorgar_prestamo(usuarios: dict):
    """Solicita al usuario un DNI válido. Si el DNI existe, se le pide al usuario
     una tasa de interés válida y un monto válido.
    Se calcula el interés, los impuestos y se aumenta el saldo del usuario segun el monto ingresado.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 4.

    POSTCONDICIONES:
    - El saldo de la cuenta que solicita el préstamo aumenta según el monto ingresado.
    - Se crea el diccionario `usuarios[dni]["prestamos"]` , si no existe, que contiene todos los datos del préstamo.
    - Se imprime el mensaje:
    'Préstamo acreditado correctamente. El balance de la cuenta de {nombre} es de ${balance}'"""

    dni = usuario.pedir_dni()

    if dni is None:
        return

    if not dni in usuarios:

        print(constantes.MSG_NO_EXISTE_CUENTA)

        return

    tasa_interes = usuario.pedir_interes()

    if tasa_interes is None:
        return

    monto = usuario.pedir_monto()

    if monto is None:
        return

    crear_campo_prestamo(usuarios, dni, monto, tasa_interes)

    print(
        constantes.MSG_PRESTAMO_CREADO.format(
            nombre=usuarios[dni]["nombre"], balance=usuarios[dni]["saldo"]
        )
    )


def pagar_impuestos(prestamo: dict, monto: int) -> int:
    """La funcion resta el monto total de los impuestos del prestamo de lo que ya pagó el usuario de impuestos.
    Luego determina cuanto del monto disponible puede aplicarse a impuestos.

    PRECONDICIONES:
    - Debe existir un prestamo en la cuenta del usuario
    - Se debe haber ingresado un monto para pagar el préstamo.

    POSTCONDICIONES:
    - Retorna el monto que queda luego de pagar los impuestos."""

    restante_impuestos = (
        prestamo["total_impuestos"] - prestamo["total_pagado_impuestos"]
    )

    a_pagar_impuestos = min(monto, restante_impuestos)

    prestamo["total_pagado_impuestos"] += a_pagar_impuestos

    return monto - a_pagar_impuestos


def pagar_intereses(prestamo: dict, monto: int) -> int:
    """Se resta el monto total de los intereses de lo que ya pagó el usuario.
    Luego determina cuanto del monto disponible puede aplicarse a intereses.

    PRECONDICIONES:
    - Debe existir un prestamo en la cuenta del usuario
    - Se debe haber ingresado un monto para pagar el préstamo.

    POSTCONDICIONES:
    - Retorna el monto que queda luego de pagar los intereses."""

    restante_intereses = (
        prestamo["total_intereses"] - prestamo["total_pagado_intereses"]
    )

    a_pagar_intereses = min(monto, restante_intereses)

    prestamo["total_pagado_intereses"] += a_pagar_intereses

    return monto - a_pagar_intereses


def pagar_capital(prestamo: dict, monto: int) -> int:
    """Se resta el monto total del capital del prestamo de lo que ya pagó el usuario.
    Luego se determina cuanto del monto disponible puede aplicarse al capital.

    PRECONDICIONES:
    - Debe existir un prestamo en la cuenta del usuario
    - Se debe haber ingresado un monto para pagar el préstamo.

    POSTCONDICIONES:
    - Retorna el monto que queda luego de pagar el capital."""

    restante_capital = prestamo["capital_total"] - prestamo["total_pagado_capital"]

    a_pagar_capital = min(monto, restante_capital)

    prestamo["total_pagado_capital"] += a_pagar_capital

    return monto - a_pagar_capital


def calcular_total_pendiente(prestamo: dict):
    """Calcula el total pendiente que queda pagar del préstamo
    """

    prestamo["total_pendiente"] = (
        (prestamo["total_impuestos"] - prestamo["total_pagado_impuestos"])
        + (prestamo["total_intereses"] - prestamo["total_pagado_intereses"])
        + (prestamo["capital_total"] - prestamo["total_pagado_capital"])
    )


def pagar_prestamo(usuarios: dict):
    """Solicita al usuario un DNI válido. Si el DNI existe, se le pide al usuario que seleccione
    un préstamo y un monto a abonar.
    Si el monto es válido, se paga el préstamo y se actualizan los datos del préstamo.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 5.

    POSTCONDICIONES:
    - Se actualizan los datos del préstamo en el diccionario `usuarios[dni]["prestamos"]`.
    - Se imprime el mensaje: 'Préstamo pagado correctamente'.
    - Si no hay préstamos activos, se imprime el mensaje: 'No hay préstamos activos'.
    - Si el DNI no existe, se imprime el mensaje: 'No existe cuenta con ese DNI."""

    dni = usuario.pedir_dni()

    if dni is None:
        return

    if dni not in usuarios:
        print(constantes.MSG_NO_EXISTE_CUENTA)
        return

    prestamos = usuarios[dni].get("prestamos")

    if not prestamos:

        print(constantes.MSG_PRESTAMO_NO_ACTIVO)

        return


    print(
        constantes.SALDO_DISPONIBLE_TEMPLATE.format(
            monto=usuarios[dni]["saldo"]
            )
        )

    print(constantes.PRESTAMOS_PENDIENTES)

    usuario.mostrar_prestamos(usuarios, dni)

    id_prestamo = seleccionar_prestamo(prestamos)

    if id_prestamo is None:
        return

    monto = usuario.pedir_monto_prestamo(usuarios, dni)

    if monto is None:
        return

    aplicar_pago_prestamo(usuarios,dni ,id_prestamo, monto)


def seleccionar_prestamo(prestamos: dict) -> int:
    """Devuelve el ID del préstamo seleccionado.
    Si el ID ingresado no está en la lista o no es un número se vuelve a pedir un ID"""

    while True:

        num_prestamo = input("Seleccione prestamo: ")

        if num_prestamo == "**":
            return None

        if not num_prestamo.isdigit():

            print(constantes.MSG_SELECCION_INVALIDA)

            continue

        if not int(num_prestamo) in prestamos:

            print(constantes.MSG_SELECCION_INVALIDA)

            continue

        return int(num_prestamo)


def aplicar_pago_prestamo(usuarios: dict, dni: int, id_prestamo: int, monto: int) -> None:
    """Aplica el pago a un préstamo y descuenta el monto del saldo del usuario."""

    prestamo = usuarios[dni]["prestamos"][id_prestamo]

    monto_original = monto

    monto = pagar_impuestos(prestamo, monto)

    monto = pagar_intereses(prestamo, monto)

    monto = pagar_capital(prestamo, monto)

    calcular_total_pendiente(prestamo)

    monto_aplicado = monto_original - monto

    usuarios[dni]["saldo"] -= monto_aplicado

    print(constantes.MSG_PRESTAMO_PAGADO)


def formatear_dni(dni: str) -> str:
    """Convierte el DNI al formato: XX.YYY.ZZZ"""

    return f"{dni:,}".replace(",", ".")


def mostrar_transferencias(usuarios: dict, dni: int):
    """Muestra las ultimas 5 transferencias que realizó o recibió el usuario detallando el monto, nombre
    de la cuenta de destino o de origen y la cuenta de destino o de origen.
    Si el usuario no tiene transferencias que mostrar, se pasan a mostrar los préstamos.
    """

    if "transferencias" not in usuarios[dni] or not usuarios[dni]["transferencias"]:
        print(constantes.PRESTAMOS_PENDIENTES)

    else:
        transferencias = usuarios[dni]["transferencias"][-5:][::-1]

        for transferencia in transferencias:

            if transferencia["tipo"] == "entrante":
                print(
                    constantes.TRANSFERENCIA_ENTRANTE_TEMPLATE.format(
                        monto=transferencia["monto"],
                        nombre=transferencia["nombre"],
                        dni=formatear_dni(transferencia["dni_origen"]),
                    )
                )

            else:
                print(
                    constantes.TRANSFERENCIA_SALIENTE_TEMPLATE.format(
                        monto=transferencia["monto"],
                        nombre=transferencia["nombre"],
                        dni=formatear_dni(transferencia["dni_destino"]),
                    )
                )
        print(constantes.PRESTAMOS_PENDIENTES)


def ver_resumen(usuarios: dict):
    """Solicita al usuario un DNI válido. Si el DNI existe, muestra un resumen de la cuenta del usuario.
    El resumen incluye el nombre, saldo, últimas 5 transferencias y préstamos solicitados.

    PRECONDICIONES:
    - `pedir_opcion()` debe retornar 6.

    POSTCONDICIONES:
    - Imprime el resumen de la cuenta del usuario.
    - Si no existe la cuenta, imprime el mensaje: 'No existe cuenta con ese DNI"""

    dni = usuario.pedir_dni()

    if dni is None:
        return

    if dni not in usuarios:

        print(constantes.MSG_NO_EXISTE_CUENTA)

        return

    print(
        constantes.RESUMEN_TEMPLATE.format(
            nombre=usuarios[dni]["nombre"], saldo=usuarios[dni]["saldo"]
        )
    )

    mostrar_transferencias(usuarios, dni)

    if "prestamos" in usuarios[dni]:
        usuario.mostrar_prestamos(usuarios, dni)
