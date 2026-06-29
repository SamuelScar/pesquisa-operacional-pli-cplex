from dataclasses import dataclass

from comum.entrada import ler_matriz_inteiros, limpar_linhas
from comum.validacao import validar_valores_nao_negativos


@dataclass(frozen=True)
class DadosDesignacao:
    custos: list[list[int]]


def ler_entrada(conteudo: str) -> DadosDesignacao:
    """Le a matriz de custos do problema de designacao."""
    linhas = limpar_linhas(conteudo)
    if len(linhas) < 2:
        raise ValueError("A entrada deve informar a quantidade e a matriz de custos.")

    quantidade = int(linhas[0])
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    custos = ler_matriz_inteiros(
        linhas[1:],
        quantidade,
        quantidade,
        "A matriz de custos deve ter uma linha por agente.",
        "A matriz de custos deve ser quadrada.",
    )
    validar_valores_nao_negativos(
        (custo for linha in custos for custo in linha),
        "Os custos nao podem ser negativos.",
    )

    return DadosDesignacao(custos)
