def palindromo(palabra):
    try:
        if len(palabra)==0:
            raise ValueError("no se puede ingresar una cadena vacia")
        return palabra==palabra[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        respuesta=palindromo("")
    except TypeError:
        print('no se puede enviar valores no string')
    except IndexError:
        print("indice invalido")
    except NameError:
        print('no es el nombre')

if __name__== '__main__':
    run()