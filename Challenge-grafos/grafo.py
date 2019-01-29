import lzma

import prueba

paises = []
rutasRes =[]
def cargarFloydWarshall(nombre):
    viajes =  []
    paisesconRutas = []
    entrada = open(nombre)
    for linea in entrada:
        # procesar línea
        if(linea.find(",") == -1):

            paises.append(linea.strip())
        else:

            relacion =linea.split(',')
            origen = relacion[0]
            destino = relacion[1]
            peso = relacion[2]
            paisesconRutas.append(origen)
            paisesconRutas.append(destino)
            viajes.append([paises.index(origen)+1, paises.index(destino)+1,int(peso.strip())])
    paisesconRutas = set(paisesconRutas)
    entrada.close()
    resultado = prueba.floyd_warshall((len(paisesconRutas)),viajes)
    return  resultado





# print(paises)

# print(len(paises))
def persistencia(resultado):
    with open("rutas.xz", "wb") as f:
        # f.write(prueba.floyd_warshall((len(paisesconRutas)),viajes)[0].encode('utf-8'))
        with lzma.open(f, "w") as lzf:
            for n in range(len(resultado)):
                ruta = resultado[n].split(",")
                rutasConNombres=[]
                rutaConNombres = " "
                for p in range(len(ruta)):
                    if(p != 2 and p < (len(ruta)-1)):

                            rutaConNombres += (paises[(int(ruta[p])-1)]+",")
                    elif (p == (len(ruta)-1)):
                        if(ruta[p] == str(100 )):
                            rutaConNombres += ("N/A")
                        else:
                            rutaConNombres += (paises[(int(ruta[p])-1)])

                    else:
                        rutaConNombres +=(ruta[p]+ ",")



                rutasConNombres.append(rutaConNombres)
                # print(rutaConNombres)
                for n in range(len(rutaConNombres)):
                    lzf.write((rutaConNombres[n] ).encode('utf-8'))
        with open("paises.xz", "wb") as f:
            # f.write(prueba.floyd_warshall((len(paisesconRutas)),viajes)[0].encode('utf-8'))
            with lzma.open(f, "w") as lzf:
                for n in range(len(paises)):
                    lzf.write((paises[n] + " ").encode('utf-8'))


def cargarDatosComprimidos():
    with lzma.open("rutas.xz") as f:
        salida = f.read().decode('utf-8').split()



    for i in range(len(salida)):
        rutasRes.append(salida[i].split(","))
    print(rutasRes)


    with lzma.open("paises.xz") as f:
        file_content = f.read()

    paises =file_content.decode('utf-8').split()
    print(paises)
    print("carga de datos completa")
    return paises


def buscarPunto1(pais):
    resultado = []
    for i in range(len(rutasRes)):
        if(rutasRes[i][0]== pais):
            resultado.append(rutasRes[i])
    if(len(resultado) == 0):
        return [["No routes found"]]
    else:
        return  resultado

def buscarPunto2(paises):
    resultado = []
    for i in range(len(rutasRes)):
        if(rutasRes[i][0]== paises[0] and  rutasRes[i][1]== paises[1]):
            resultado.append(rutasRes[i])

    if(len(resultado) == 0):
        return [["No routes found"]]
    else:
        return  resultado


# cargarDatosComprimidos()











