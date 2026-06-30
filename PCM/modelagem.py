from docplex.mp.model import Model

from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    origem_caminho: int,
    destino_caminho: int,
    arestas: list[Aresta],
) -> tuple[Model, list]:
    modelo = Model(name="PCM")

    # Variavel x_ij: 1 se a aresta i -> j fizer parte do caminho; 0 caso contrario.
    escolhas = [
        modelo.binary_var(name=f"x_{aresta.origem}_{aresta.destino}_{indice}")
        for indice, aresta in enumerate(arestas, start=1)
    ]

    # Objetivo: minimizar o custo total das arestas escolhidas.
    modelo.minimize(
        modelo.sum(aresta.custo * escolha for aresta, escolha in zip(arestas, escolhas))
    )

    # Balanco do caminho:
    # origem tem saida liquida 1, destino tem entrada liquida 1,
    # e os demais vertices conservam fluxo.
    for vertice in range(1, numero_vertices + 1):
        saida = modelo.sum(
            escolha
            for aresta, escolha in zip(arestas, escolhas)
            if aresta.origem == vertice
        )
        entrada = modelo.sum(
            escolha
            for aresta, escolha in zip(arestas, escolhas)
            if aresta.destino == vertice
        )
        balanco = (
            1
            if vertice == origem_caminho
            else -1
            if vertice == destino_caminho
            else 0
        )
        modelo.add_constraint(
            saida - entrada == balanco,
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, escolhas
