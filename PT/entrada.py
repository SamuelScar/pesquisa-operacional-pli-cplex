from dataclasses import dataclass


@dataclass(frozen=True)
class DadosTransporte:
    ofertas: list[int]
    demandas: list[int]
    custos: list[list[int]]


def ler_entrada(conteudo: str) -> DadosTransporte:
    """Le ofertas, demandas e matriz de custos do problema."""
    linhas = conteudo.splitlines()
    ofertas = list(map(int, linhas[0].split()))
    demandas = list(map(int, linhas[1].split()))
    custos = [list(map(int, linha.split())) for linha in linhas[2:]]

    return DadosTransporte(ofertas, demandas, custos)
