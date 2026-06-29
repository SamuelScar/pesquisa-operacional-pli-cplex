from docplex.mp.model import Model

from comum.modelagem import (
    criar_escolhas_por_aresta,
    criar_modelo,
    fluxo_saida_menos_entrada,
)
from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    origem_caminho: int,
    destino_caminho: int,
    arestas: list[Aresta],
) -> tuple[Model, list]:
    modelo = criar_modelo("PCM")
    escolhas = criar_escolhas_por_aresta(modelo, arestas)

    modelo.minimize(
        modelo.sum(aresta.custo * escolha for aresta, escolha in zip(arestas, escolhas))
    )

    for vertice in range(1, numero_vertices + 1):
        balanco = (
            1
            if vertice == origem_caminho
            else -1
            if vertice == destino_caminho
            else 0
        )
        modelo.add_constraint(
            fluxo_saida_menos_entrada(modelo, arestas, escolhas, vertice) == balanco,
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, escolhas
