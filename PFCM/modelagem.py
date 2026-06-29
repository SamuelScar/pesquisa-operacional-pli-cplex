from docplex.mp.model import Model

from comum.modelagem import (
    criar_fluxos_por_aresta,
    criar_modelo,
    fluxo_saida_menos_entrada,
)
from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    saldos: list[int],
    arestas: list[Aresta],
) -> tuple[Model, list]:
    modelo = criar_modelo("PFCM")
    fluxos = criar_fluxos_por_aresta(modelo, arestas)

    modelo.minimize(
        modelo.sum(aresta.custo * fluxo for aresta, fluxo in zip(arestas, fluxos))
    )

    for vertice in range(1, numero_vertices + 1):
        modelo.add_constraint(
            fluxo_saida_menos_entrada(modelo, arestas, fluxos, vertice)
            == saldos[vertice - 1],
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, fluxos
