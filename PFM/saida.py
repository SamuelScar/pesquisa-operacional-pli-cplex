def imprimir_dados(
    numero_vertices: int,
    origem_fluxo: int,
    destino_fluxo: int,
    arestas: list,
) -> None:
    print("Dados do PFM:")
    print(f"Vertices: {numero_vertices}")
    print(f"Origem: {origem_fluxo}")
    print(f"Destino: {destino_fluxo}")
    print(f"Arestas: {len(arestas)}")


def imprimir_resultado(solucao, fluxo_maximo, fluxos: list, arestas: list) -> None:
    if solucao is None:
        print("Sem solucao")
        return

    print(f"\nFluxo maximo = {solucao.get_value(fluxo_maximo):.0f}")
    print("\nFluxos positivos:")

    for aresta, fluxo in zip(arestas, fluxos):
        valor = solucao.get_value(fluxo)
        if valor > 0:
            print(f"{aresta.origem} -> {aresta.destino}: {valor:.0f}")
