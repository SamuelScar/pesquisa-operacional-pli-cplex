from docplex.mp.model import Model

from comum.saida import (
    imprimir_cabecalho_variaveis_arestas,
    imprimir_linha_variavel_aresta,
    imprimir_status_solucao,
)


def imprimir_dados(
    numero_vertices: int,
    origem_caminho: int,
    destino_caminho: int,
    arestas: list,
) -> None:
    print("Verificacao da leitura dos dados:")
    print(
        f"Vertices: {numero_vertices} | Arestas: {len(arestas)} | "
        f"Origem: {origem_caminho} | Destino: {destino_caminho}"
    )

    print("\nArestas:")
    print(f"{'Indice':>6} | {'Origem':>6} | {'Destino':>7} | {'Custo':>5}")
    print("-" * 37)
    for indice, aresta in enumerate(arestas, start=1):
        print(
            f"{indice:>6} | {aresta.origem:>6} | "
            f"{aresta.destino:>7} | {aresta.custo:>5}"
        )


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
    modelo: Model,
    solucao,
    origem_caminho: int,
    destino_caminho: int,
    escolhas: list,
    arestas: list,
) -> None:
    if not imprimir_status_solucao(modelo, solucao):
        return

    print(f"Custo minimo = {solucao.objective_value:.0f}")

    arestas_escolhidas = [
        aresta
        for aresta, escolha in zip(arestas, escolhas)
        if solucao.get_value(escolha) > 0.5
    ]
    caminho = montar_caminho(origem_caminho, destino_caminho, arestas_escolhidas)

    print(f"Caminho: {' -> '.join(map(str, caminho))}")
    print("\nArestas escolhidas:")
    imprimir_cabecalho_variaveis_arestas("Custo")

    for indice, (aresta, escolha) in enumerate(zip(arestas, escolhas), start=1):
        if solucao.get_value(escolha) <= 0.5:
            continue

        imprimir_linha_variavel_aresta(indice, escolha, aresta, aresta.custo)
