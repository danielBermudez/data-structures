import prueba
entrada = open("Eurotrip.txt")
paises = [" "]
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
        viajes.append([paises.index(origen), paises.index(destino),int(peso.strip())])


entrada.close()

print(paises)
print(viajes)
prueba.floyd_warshall(len(viajes),viajes)









