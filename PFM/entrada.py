from dataclasses import dataclass

from comum.entrada import limpar_linhas
from comum.validacao import (
    validar_extremos_aresta,
    validar_quantidade,
    validar_vertice,
)


@dataclass(frozen=True)
class Aresta:
    origem: int
    destino: int
    capacidade: int


def ler_entrada(conteudo: str) -> tuple[int, int, int, list[Aresta]]:
    """Le o grafo, a origem, o destino e as capacidades das arestas."""
    linhas = limpar_linhas(conteudo)
    if len(linhas) < 2:
        raise ValueError("A entrada deve informar vertices, arestas, origem e destino.")

    numero_vertices, numero_arestas = map(int, linhas[0].split())
    origem_fluxo, destino_fluxo = map(int, linhas[1].split())

    if origem_fluxo == destino_fluxo:
        raise ValueError("Origem e destino do fluxo devem ser diferentes.")
    validar_vertice(origem_fluxo, numero_vertices, "Origem do fluxo")
    validar_vertice(destino_fluxo, numero_vertices, "Destino do fluxo")

    linhas_arestas = linhas[2:]
    validar_quantidade(
        len(linhas_arestas),
        numero_arestas,
        "A quantidade de arestas informada nao bate com a entrada.",
    )

    arestas = []
    for linha in linhas_arestas:
        origem, destino, capacidade = map(int, linha.split())
        validar_extremos_aresta(origem, destino, numero_vertices)

        if capacidade < 0:
            raise ValueError("A capacidade da aresta nao pode ser negativa.")

        arestas.append(Aresta(origem, destino, capacidade))

    return numero_vertices, origem_fluxo, destino_fluxo, arestas
