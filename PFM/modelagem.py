from docplex.mp.model import Model

from comum.modelagem import (
    criar_fluxos_por_aresta,
    criar_modelo,
    fluxo_saida_menos_entrada,
)
from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    origem_fluxo: int,
    destino_fluxo: int,
    arestas: list[Aresta],
) -> tuple[Model, list, object]:
    modelo = criar_modelo("PFM")
    fluxo_maximo = modelo.integer_var(lb=0, name="fluxo_maximo")
    fluxos = criar_fluxos_por_aresta(modelo, arestas)

    modelo.maximize(fluxo_maximo)

    for vertice in range(1, numero_vertices + 1):
        balanco = (
            fluxo_maximo
            if vertice == origem_fluxo
            else -fluxo_maximo
            if vertice == destino_fluxo
            else 0
        )
        modelo.add_constraint(
            fluxo_saida_menos_entrada(modelo, arestas, fluxos, vertice) == balanco,
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, fluxos, fluxo_maximo
