from docplex.mp.model import Model


def imprimir_dados(numero_vertices: int, saldos: list[int], arestas: list) -> None:
    print("Dados do PFCM:")
    print(f"Vertices: {numero_vertices}")
    print(f"Saldos: {saldos}")
    print(f"Arestas: {len(arestas)}")


def imprimir_resultado(modelo: Model, solucao, fluxos: list, arestas: list) -> None:
    if solucao is None:
        print("Sem solucao")
        return

    print("\nFluxos positivos:")
    for aresta, fluxo in zip(arestas, fluxos):
        valor = solucao.get_value(fluxo)
        if valor > 0:
            print(f"{aresta.origem} -> {aresta.destino}: {valor:.0f}")

    print(f"\nCusto minimo = {solucao.objective_value:.0f}")
