def run():
    numeros=[3,54,32,1,5,0,5]
    ordenado=[]
    for item in range(len(numeros)):
        menor=numeros[0]
        print(item)
        for j in numeros:
            if menor<=j:
                pass
            else:
                menor=j
        ordenado.append(menor)
        numeros.remove(menor)
    print('ordenado {}'.format(ordenado))


if __name__=='__main__':
    run()