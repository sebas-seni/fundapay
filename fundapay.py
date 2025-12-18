import logica
import usuario
import constantes


def main():

    usuarios = {}

    acciones = {
        1: logica.crear_cuenta,
        2: logica.ingresar_dinero,
        3: logica.transferir_dinero,
        4: logica.otorgar_prestamo,
        5: logica.pagar_prestamo,
        6: logica.ver_resumen,
    }

    while True:

        opcion = usuario.pedir_opcion()

        if opcion == constantes.SALIR:

            print(constantes.MSG_FIN)

            break

        accion = acciones.get(opcion)

        if accion:

            accion(usuarios)


if __name__ == "__main__":
    main()
