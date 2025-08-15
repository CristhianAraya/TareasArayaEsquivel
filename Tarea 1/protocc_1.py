import string

# Primer metodo "count_char"
# La funcion count_char recibe los dos parametros solicitados Cadena y Caracter


def count_char(Cadena, Caracter):
    # Se verifica si Cadena y caracter son un string
    if isinstance(Cadena, str) and isinstance(Caracter, str):
        # Itera el bucle el largo que tenga Cadena
        for i in range(len(Cadena)):
            # Revisa caracter por caracter de cadena o caracter para ver
            # si esta incluido en las letras y numeros ascii
            validos = string.ascii_letters + string.digits + "Ññ"
            if Cadena[i] in validos and Caracter in validos:
                continue

            else:
                # Este es el codigo de error unico para cuando
                # no hay un caracter del abecedario o un
                # digito en Cadena o caracter
                print("E-NOTCHAR\nNone")
                return

    else:
        # Este es el codigo de error unico para cuando Cadena no sea un string
        print("E-NOTSTR\nNone")

        return
    # Variable que cuenta cuantas veces se encuenta Caracter en Cadena
    Presencia = 0

    if len(Caracter) > 1:
        # Codigo de error unico para cuando hay mas de 1 caracter
        print("E-LENCHAR\nNone")
        return

    else:

        # Recorre Cadena y verifica si Caracter aparece y cuantas veces
        for i in range(len(Cadena)):

            if Cadena[i] == Caracter:

                Presencia += 1

    if Presencia == 1:

        print("S-CHARCOUNT\n"+Caracter+" aparece "+str(Presencia)+" vez.")

    else:

        print("S-CHARCOUNT\n"+Caracter+" aparece "+str(Presencia)+" veces.")


count_char("ueuew", "p")

