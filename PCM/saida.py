def imprimir_dados(
    numero_vertices: int,
    origem_caminho: int,
    destino_caminho: int,
    arestas: list,
) -> None:
    print("Dados do PCM:")
    print(f"Vertices: {numero_vertices}")
    print(f"Origem: {origem_caminho}")
    print(f"Destino: {destino_caminho}")
    print(f"Arestas: {len(arestas)}")


def montar_caminho(
    origem_caminho: int,
    destino_caminho: int,
    arestas_escolhidas: list,
) -> list[int]:
    proximos_vertices = {aresta.origem: aresta.destino for aresta in arestas_escolhidas}
    caminho = [origem_caminho]
    vertice_atual = origem_caminho

    while vertice_atual != destino_caminho and vertice_atual in proximos_vertices:
        vertice_atual = proximos_vertices[vertice_atual]
        caminho.append(vertice_atual)

    return caminho


def imprimir_resultado(
    solucao,
    origem_caminho: int,
    destino_caminho: int,
    escolhas: list,
    arestas: list,
) -> None:
    if solucao is None:
        print("Sem solucao")
        return

    arestas_escolhidas = [
        aresta
        for aresta, escolha in zip(arestas, escolhas)
        if solucao.get_value(escolha) > 0.5
    ]
    caminho = montar_caminho(origem_caminho, destino_caminho, arestas_escolhidas)

    print(f"\nCusto minimo = {solucao.objective_value:.0f}")
    print(f"Caminho: {' -> '.join(map(str, caminho))}")
