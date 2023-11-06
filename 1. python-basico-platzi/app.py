from random import choice


# def generador_password():
#     print(""" GENERADOR DE CONTRASENIAS """)
#     passwor=[]
#     clave=[]
#     for i in range(1,3):
#         mayuscula = choice(['A', 'B', 'C', 'D', 'E'])
#         maniscula = choice(['f', 'g', 'h', 'i', 'j', 'k'])
#         numero = choice(['1', '2', '3', '4', '5'])
#         simbolos = choice(['@', '#', '$', '%'])
#         clave=mayuscula+maniscula+numero+simbolos
#         passwor.append(clave)
#         print(type(clave))
#     passwor="".join(passwor)
#     return passwor
def run():
#     password = generador_password()
#     print('contransenia {}'.format(password))
    # mensaje='hola, como esas, amiguito ,sabes que ,te amo'
    # print(mensaje)
    # mensaje=mensaje.split(sep=' ')
    # print(mensaje)
    
    # nombre='jhonatan maquera'
    nombre=['tito','solana','pedro','pedro']
    # nombre={
    #     "nombre":"jhonatan",
    #     "apellido":"maquera",
    #     "edad":32
    #     }
    # print(nombre.items())
    # print(nombre.title())
    # print(nombre.find('pedro'))
    print(nombre.index('pedro'))
    print(nombre)
if __name__ == '__main__':
    run()