from docplex.mp.model import Model

from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    origem_fluxo: int,
    destino_fluxo: int,
    arestas: list[Aresta],
) -> tuple[Model, list, object]:
    modelo = Model(name="PFM")

    # Variavel F: valor total de fluxo enviado da origem ao destino.
    fluxo_maximo = modelo.integer_var(lb=0, name="fluxo_maximo")

    # Variavel x_ij: quantidade de fluxo enviada em cada aresta i -> j.
    # O limite superior e a capacidade maxima da propria aresta.
    fluxos = [
        modelo.integer_var(
            lb=0,
            ub=aresta.capacidade,
            name=f"x_{aresta.origem}_{aresta.destino}_{indice}",
        )
        for indice, aresta in enumerate(arestas, start=1)
    ]

    # Objetivo: maximizar o fluxo total que sai da origem e chega ao destino.
    modelo.maximize(fluxo_maximo)

    # Balanco de fluxo:
    # origem gera F, destino consome F, e os demais vertices conservam fluxo.
    for vertice in range(1, numero_vertices + 1):
        saida = modelo.sum(
            fluxo for aresta, fluxo in zip(arestas, fluxos) if aresta.origem == vertice
        )
        entrada = modelo.sum(
            fluxo for aresta, fluxo in zip(arestas, fluxos) if aresta.destino == vertice
        )
        balanco = (
            fluxo_maximo
            if vertice == origem_fluxo
            else -fluxo_maximo
            if vertice == destino_fluxo
            else 0
        )
        modelo.add_constraint(
            saida - entrada == balanco,
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, fluxos, fluxo_maximo
