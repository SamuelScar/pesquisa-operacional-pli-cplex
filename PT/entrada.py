from dataclasses import dataclass

from comum.entrada import ler_matriz_inteiros, limpar_linhas
from comum.validacao import validar_quantidade, validar_valores_nao_negativos


@dataclass(frozen=True)
class DadosTransporte:
    ofertas: list[int]
    demandas: list[int]
    custos: list[list[int]]


def ler_entrada(conteudo: str) -> DadosTransporte:
    """Le ofertas, demandas e matriz de custos do problema."""
    linhas = limpar_linhas(conteudo)
    if len(linhas) < 3:
        raise ValueError("A entrada deve informar origens, destinos, ofertas e demandas.")

    numero_origens, numero_destinos = map(int, linhas[0].split())
    ofertas = list(map(int, linhas[1].split()))
    demandas = list(map(int, linhas[2].split()))

    validar_quantidade(
        len(ofertas),
        numero_origens,
        "A quantidade de ofertas deve ser igual ao numero de origens.",
    )
    validar_quantidade(
        len(demandas),
        numero_destinos,
        "A quantidade de demandas deve ser igual ao numero de destinos.",
    )
    if sum(ofertas) != sum(demandas):
        raise ValueError("A soma das ofertas deve ser igual a soma das demandas.")
    validar_valores_nao_negativos(
        ofertas + demandas,
        "Ofertas e demandas nao podem ser negativas.",
    )

    custos = ler_matriz_inteiros(
        linhas[3:],
        numero_origens,
        numero_destinos,
        "A matriz de custos deve ter uma linha por origem.",
        "Cada linha de custos deve ter uma coluna por destino.",
    )
    validar_valores_nao_negativos(
        (custo for linha in custos for custo in linha),
        "Os custos nao podem ser negativos.",
    )

    return DadosTransporte(ofertas, demandas, custos)
