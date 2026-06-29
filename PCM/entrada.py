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
    custo: int


def ler_entrada(conteudo: str) -> tuple[int, int, int, list[Aresta]]:
    """Le o grafo, a origem, o destino e o custo das arestas."""
    linhas = limpar_linhas(conteudo)
    if len(linhas) < 2:
        raise ValueError("A entrada deve informar vertices, arestas, origem e destino.")

    numero_vertices, numero_arestas = map(int, linhas[0].split())
    origem_caminho, destino_caminho = map(int, linhas[1].split())

    if origem_caminho == destino_caminho:
        raise ValueError("Origem e destino do caminho devem ser diferentes.")
    validar_vertice(origem_caminho, numero_vertices, "Origem do caminho")
    validar_vertice(destino_caminho, numero_vertices, "Destino do caminho")

    linhas_arestas = linhas[2:]
    validar_quantidade(
        len(linhas_arestas),
        numero_arestas,
        "A quantidade de arestas informada nao bate com a entrada.",
    )

    arestas = []
    for linha in linhas_arestas:
        origem, destino, custo = map(int, linha.split())
        validar_extremos_aresta(origem, destino, numero_vertices)

        if custo < 0:
            raise ValueError("O custo da aresta nao pode ser negativo.")

        arestas.append(Aresta(origem, destino, custo))

    return numero_vertices, origem_caminho, destino_caminho, arestas
