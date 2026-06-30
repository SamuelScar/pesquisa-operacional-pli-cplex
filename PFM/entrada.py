from dataclasses import dataclass


@dataclass(frozen=True)
class Aresta:
    origem: int
    destino: int
    capacidade: int


def ler_entrada(conteudo: str) -> tuple[int, int, int, list[Aresta]]:
    """Le o grafo, a origem, o destino e as capacidades das arestas."""
    linhas = conteudo.splitlines()
    numero_vertices = int(linhas[0])
    origem_fluxo, destino_fluxo = map(int, linhas[1].split())
    arestas = [Aresta(*map(int, linha.split())) for linha in linhas[2:]]

    return numero_vertices, origem_fluxo, destino_fluxo, arestas
