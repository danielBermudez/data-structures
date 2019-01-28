from math import inf
from itertools import product


def floyd_warshall(n, edge):
    rutas =[]

    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt  = [[0]   * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u-1][v-1] = w
        nxt[u-1][v-1] = v-1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j]  = nxt[i][k]
    # print("pair     dist    path")
    for i, j in product(rn, repeat=2):
        if i != j:

            path = [i]
            bandera = 0
            while path[-1] != j  and bandera == 0:
                ruta = []
                if(len(path)> 10):
                    rutas.append("%d,%d,%d,%s"
                                % (i + 1, j + 1,0,100))
                    # print("%d,%d,%4d,%s"
                    #       % (i + 1, j + 1,0," no se encontro una ruta posible"))
                    bandera = 1
                else:
                    path.append(nxt[path[-1]][j])

            if bandera ==0:
                rutas.append("%d,%d,%d,%s"
                 % (i + 1, j + 1,dist[i][j],",".join(str(p + 1) for p in path)))
                # print("%d,%d,%4d%s"
                #       % (i + 1, j + 1,dist[i][j],",".join(str(p + 1) for p in path)))


    return(rutas)






