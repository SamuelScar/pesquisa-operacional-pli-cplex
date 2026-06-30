from dataclasses import dataclass


@dataclass(frozen=True)
class Aresta:
    origem: int
    destino: int
    custo: int
    capacidade: int


def ler_entrada(conteudo: str) -> tuple[int, list[int], list[Aresta]]:
    """Le o grafo, os saldos dos vertices e os dados das arestas."""
    linhas = conteudo.splitlines()
    numero_vertices = int(linhas[0])
    saldos = list(map(int, linhas[1].split()))
    arestas = [Aresta(*map(int, linha.split())) for linha in linhas[2:]]

    return numero_vertices, saldos, arestas
