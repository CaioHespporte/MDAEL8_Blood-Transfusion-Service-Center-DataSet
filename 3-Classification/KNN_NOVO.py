from math import sqrt
# função de cálculo de distância
def distancia_euclidiana(vet1, vet2):
    distancia = 0
    for i in range(len(vet1)-1):
        distancia += (vet1[i]-vet2[i])**2
    distancia = sqrt(distancia)
    return distancia

#funcao retorna k vizinhos mais proximos
def retorna_vizinhos(base_treinamento, amostra_teste, num_vizinhos):
    distancias = list()
    for linha_treinamento in base_treinamento:
        dist = distancia_euclidiana(amostra_teste, linha_treinamento)
        distancias.append((linha_treinamento, dist))
#ordenação das distancias de forma crescente 
    distancias.sort(key = lambda tup: tup[1])
#retorna os vizinhos mais proximos
    vizinhos = list()
    for i in range(num_vizinhos):
        vizinhos.append(distancias[i][0])
    return vizinhos

#funcao de predição/classificação
def classifica(base_treinamento, amostra_teste, num_vizinhos):
    vizinhos = retorna_vizinhos(base_treinamento, amostra_teste, num_vizinhos)
    rotulos = [v[-1] for v in vizinhos]
    predicao = max(set(rotulos), key=rotulos.count)
    return predicao

dataset = [[2.7, 2.5, 0],
        [1.4, 2.3, 0],
        [3.3, 3.4, 0],
        [1.3, 1.8, 0],
        [3.0, 3.0, 0],
        [7.6, 2.7, 1],
        [5.3, 2.0, 1],
        [6.9, 1.7, 1],
        [8.6, -0.2, 1],
        [7.6, 3.5, 1]]

amostra = [2.4, 2.6, 0]
predicao = classifica(dataset, amostra, 3)
print('Resultado da Classificação')
print('Rótulo esperado %d, Rótulo predição %d' %(amostra[-1], predicao))