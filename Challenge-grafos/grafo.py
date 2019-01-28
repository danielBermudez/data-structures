import lzma

import prueba
entrada = open("Eurotrip.txt")
paises = []
paisesconRutas = []
viajes =  []


for linea in entrada:
    viaje = []


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

# print(paises)

# print(len(paises))
resultado = prueba.floyd_warshall((len(paisesconRutas)),viajes)
print(resultado)

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
                        rutaConNombres += ("No se encontro una ruta posible")
                    else:
                        rutaConNombres += (paises[(int(ruta[p])-1)])

                else:
                    rutaConNombres +=(ruta[p]+ ",")



            rutasConNombres.append(rutaConNombres)
            # print(rutaConNombres)
            for n in range(len(rutaConNombres)):
                 lzf.write((rutaConNombres[n] ).encode('utf-8'))



with lzma.open("rutas.xz") as f:
    file_content = f.read()

print(file_content.decode('utf-8'))

with open("paises.xz", "wb") as f:
    # f.write(prueba.floyd_warshall((len(paisesconRutas)),viajes)[0].encode('utf-8'))
    with lzma.open(f, "w") as lzf:
        for n in range(len(paises)):
            lzf.write((paises[n] + "\n").encode('utf-8'))

with lzma.open("paises.xz") as f:
    file_content = f.read()
print(file_content.decode('utf-8'))







