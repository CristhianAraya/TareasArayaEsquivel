# Tarea 1 MT-7003
# Cristhian Araya Chaves y Greivin Esquivel Salazar
# 15/08/2025

# Librerias

import string  # Utilizado en count_char
import math  # Utilizado en multiplo_2

# Primer metodo "count_char"

# Este primer metodo recibe cadena que es una variable
# tipo string de largo indefinido mientras que caracter
# es un string con solo un miembro.
# El metodo cuenta cuantas veces caracter se encuentra en cadena.


def count_char(cadena, caracter):
    # Verifica que Cadena sea string
    if not isinstance(cadena, str):
        # E-CHAINNOTSTR y -100 son un codigo de error unico
        # print("E-NOTSTR\nNone") # Error: no es string
        return -100, None

    # Verifica que caracter sea string
    if not isinstance(caracter, str):
        # E-CHARNOTSTR y -300 son un codigo de error unico
        # print("E-NOTSTR\nNone") # Error: no es string
        return -300, None

    # Verifica que el carácter tenga longitud 1
    if len(caracter) != 1:
        # E-LENCHAR -300 son un codigo de error unico
        # print("E-LENCHAR\nNone") # Error: más de un carácter
        return -300, None

    # Verifica que todos los caracteres en Cadena y Caracter sean válidos
    # Las funciones string.ascii_letter y string.digits
    # provienen de la libreria string
    caracteres_validos = string.ascii_letters + string.digits + "Ññ"
    if not all(c in caracteres_validos for c in cadena):
        # E-CHAINNOTCHAR y -200 son un codigo de error unico
        # print("E-CHAINNOTCHAR\nNone") # Error: caracteres no válidos
        return -200, None

    if caracter not in caracteres_validos:
        # E-CHARNOTCHAR y -300 son un codigo de error unico
        # print("E-CHARNOTCHAR\nNone") # Error: caracteres no válidos
        return -300, None

    # Cuenta cuántas veces aparece el carácter
    Presencia = cadena.count(caracter)

    # Imprime el resultado según la cantidad
    # S-CHARCOUNT y 0 son un código de éxito único
    if Presencia == 1:
        # Éxito: una vez
        return 0, Presencia
        # print("S-CHARCOUNT\n"+caracter+" aparece "+str(Presencia)+" vez.")
    else:
        # Éxito: varias veces
        return 0, Presencia
        # print("S-CHARCOUNT\n"+caracter+" aparece "+str(Presencia)+" veces.")

# Segundo método "multiplo_2"

# multiplo_2 es un metodo que recibe base que es un interger
# de valor arbitrario y multiplo que es un valor unico que
# puede ser 1,2,4,8 o 16.
# Se busca multiplicar base por multiplo sin utilizar
# + * y/o for y que arroje el resultado


def multiplo_2(base, multiplo):
    # Verifica que tanto base como multiplo sean int
    if not isinstance(base, int) or not isinstance(multiplo, int):
        # E-NOTINT y -400 son un codigo de error unico
        # print("E-NOTINT\nNone") # Error: no es interger
        return -400, None

    Valores_m = (1, 2, 4, 8, 16)  # Son los valores de verificacion de multiplo

    # Verifica que multiplo esta entre Valores_m
    if multiplo not in Valores_m:
        return -500, None

    # Esta funcion busca utilizar el concepto de desplazar a la derecha
    # Como se estudio en las ALU de digital
    def multiplicacion(b, m):

        # Se utiliza la funcion de logaritmo de la libreria math con el fin de
        # Obtener la cantidad de bits que se ha de desplazar base
        multiplicador = math.log2(m)

        resultado = b << (int(multiplicador))
        # print(resultado)
        return resultado

    resultado = multiplicacion(base, multiplo)
    print(resultado)

    return 0, resultado

# Nota final: Los prints comentados se utilizaron
# en un principio para verificar la respuesta
# correcta ante distintos valores introducidos
