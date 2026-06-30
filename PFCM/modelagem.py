from docplex.mp.model import Model

from entrada import Aresta


def montar_modelo(
    numero_vertices: int,
    saldos: list[int],
    arestas: list[Aresta],
) -> tuple[Model, list]:
    modelo = Model(name="PFCM")

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

    # Objetivo: minimizar o custo total do fluxo enviado pela rede.
    modelo.minimize(
        modelo.sum(aresta.custo * fluxo for aresta, fluxo in zip(arestas, fluxos))
    )

    # Balanco de fluxo em cada vertice:
    # saida - entrada = saldo.
    # Saldo positivo representa oferta; saldo negativo representa demanda.
    for vertice in range(1, numero_vertices + 1):
        saida = modelo.sum(
            fluxo for aresta, fluxo in zip(arestas, fluxos) if aresta.origem == vertice
        )
        entrada = modelo.sum(
            fluxo for aresta, fluxo in zip(arestas, fluxos) if aresta.destino == vertice
        )
        modelo.add_constraint(
            saida - entrada == saldos[vertice - 1],
            ctname=f"balanco_vertice_{vertice}",
        )

    return modelo, fluxos
