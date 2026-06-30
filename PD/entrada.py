from dataclasses import dataclass


@dataclass(frozen=True)
class DadosDesignacao:
    custos: list[list[int]]


def ler_entrada(conteudo: str) -> DadosDesignacao:
    """Le a matriz de custos do problema de designacao."""
    linhas = conteudo.splitlines()
    custos = [list(map(int, linha.split())) for linha in linhas]

    return DadosDesignacao(custos)
