from dataclasses import dataclass

from comum.entrada import limpar_linhas
from comum.validacao import validar_extremos_aresta, validar_quantidade


@dataclass(frozen=True)
class Aresta:
    origem: int
    destino: int
    custo: int
    capacidade: int


def ler_entrada(conteudo: str) -> tuple[int, list[int], list[Aresta]]:
    """Le o grafo, os saldos dos vertices e os dados das arestas."""
    linhas = limpar_linhas(conteudo)
    if len(linhas) < 2:
        raise ValueError("A entrada deve informar vertices, arestas e saldos.")

    numero_vertices, numero_arestas = map(int, linhas[0].split())
    saldos = list(map(int, linhas[1].split()))

    validar_quantidade(
        len(saldos),
        numero_vertices,
        "A quantidade de saldos deve ser igual ao numero de vertices.",
    )
    if sum(saldos) != 0:
        raise ValueError("A soma dos saldos deve ser zero.")

    linhas_arestas = linhas[2:]
    validar_quantidade(
        len(linhas_arestas),
        numero_arestas,
        "A quantidade de arestas informada nao bate com a entrada.",
    )

    arestas = []
    for linha in linhas_arestas:
        origem, destino, custo, capacidade = map(int, linha.split())
        validar_extremos_aresta(origem, destino, numero_vertices)

        if capacidade < 0:
            raise ValueError("A capacidade da aresta nao pode ser negativa.")

        arestas.append(Aresta(origem, destino, custo, capacidade))

    return numero_vertices, saldos, arestas
