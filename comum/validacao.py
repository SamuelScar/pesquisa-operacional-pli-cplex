from collections.abc import Iterable


def validar_quantidade(atual: int, esperada: int, mensagem: str) -> None:
    if atual != esperada:
        raise ValueError(mensagem)


def validar_valores_nao_negativos(valores: Iterable[int], mensagem: str) -> None:
    if any(valor < 0 for valor in valores):
        raise ValueError(mensagem)


def validar_vertice(vertice: int, numero_vertices: int, descricao: str) -> None:
    if not 1 <= vertice <= numero_vertices:
        raise ValueError(f"{descricao} invalido: {vertice}.")


def validar_extremos_aresta(origem: int, destino: int, numero_vertices: int) -> None:
    validar_vertice(origem, numero_vertices, "Vertice de origem")
    validar_vertice(destino, numero_vertices, "Vertice de destino")
