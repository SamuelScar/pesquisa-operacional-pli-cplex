from docplex.mp.model import Model

from comum.configuracao import LIMITE_TEMPO_SEGUNDOS


def criar_modelo(nome: str) -> Model:
    modelo = Model(name=nome)
    modelo.set_time_limit(LIMITE_TEMPO_SEGUNDOS)
    return modelo


def criar_fluxos_por_aresta(modelo: Model, arestas: list) -> list:
    return [
        modelo.integer_var(
            lb=0,
            ub=aresta.capacidade,
            name=f"x_{aresta.origem}_{aresta.destino}_{indice}",
        )
        for indice, aresta in enumerate(arestas, start=1)
    ]


def criar_escolhas_por_aresta(modelo: Model, arestas: list) -> list:
    return [
        modelo.binary_var(name=f"x_{aresta.origem}_{aresta.destino}_{indice}")
        for indice, aresta in enumerate(arestas, start=1)
    ]


def fluxo_saida_menos_entrada(
    modelo: Model,
    arestas: list,
    variaveis: list,
    vertice: int,
):
    saida = modelo.sum(
        variavel
        for aresta, variavel in zip(arestas, variaveis)
        if aresta.origem == vertice
    )
    entrada = modelo.sum(
        variavel
        for aresta, variavel in zip(arestas, variaveis)
        if aresta.destino == vertice
    )
    return saida - entrada
