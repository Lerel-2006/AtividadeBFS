
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}


def listarVizinhosVertice(grafo, vertice):
    lista = []

    if vertice in grafo:
        for v in grafo[vertice]:
            lista.append(v)

    return lista



def buscaEmLargura(grafo, inicio):
    visitados = []
    fila = []

    if inicio not in grafo:
        print("O vértice inicial não existe nesse grafo")
        return None

    fila = [inicio]

    while fila:
        atual = fila.pop(0)

        visitados.append(atual)

        vizinhos = listarVizinhosVertice(grafo, atual)

        for vizinho in vizinhos:
            if vizinho not in visitados:
                if vizinho not in fila:
                    fila.append(vizinho)

    return visitados


# BFS MENOR CAMINHO
def menorCaminhoBFS(grafo, inicio, destino):
    visitados = []

    fila = [
        {
            'vertice': inicio,
            'caminho': [inicio]
        }
    ]

    if inicio not in grafo or destino not in grafo:
        print("Os vértices não existem nesse grafo")
        return None

    while fila:
        item = fila.pop(0)

        atual = item['vertice']
        caminho = item['caminho']

        if atual == destino:
            return caminho

        visitados.append(atual)

        vizinhos = listarVizinhosVertice(grafo, atual)

        for vizinho in vizinhos:
            if vizinho not in visitados:

                jaEstaNaFila = False

                for item in fila:
                    if vizinho == item['vertice']:
                        jaEstaNaFila = True

                if not jaEstaNaFila:
                    novoCaminho = caminho.copy()
                    novoCaminho.append(vizinho)

                    fila.append({
                        'vertice': vizinho,
                        'caminho': novoCaminho
                    })

    return None


# MENU
while True:

    print("\n========== MENU BFS ==========")
    print("1 - Busca em Largura Padrão")
    print("2 - Encontrar Menor Caminho")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\nVértices disponíveis:", list(grafo.keys()))

        inicio = input("Digite o vértice inicial: ").upper()

        res = buscaEmLargura(grafo, inicio)

        if res != None:
            print("Ordem dos vértices visitados:", res)

    elif opcao == "2":

        print("\nVértices disponíveis:", list(grafo.keys()))

        inicio = input("Digite o vértice inicial: ").upper()
        destino = input("Digite o vértice destino: ").upper()

        res = menorCaminhoBFS(grafo, inicio, destino)

        if res != None:
            print("Menor caminho:", res)
            print("Quantidade de arestas:", len(res) - 1)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
