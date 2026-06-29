from collections.abc import Callable
from pathlib import Path
import sys


def limpar_linhas(conteudo: str) -> list[str]:
    return [
        linha_limpa
        for linha in conteudo.splitlines()
        if (linha_limpa := linha.split("#", 1)[0].strip())
    ]


def obter_conteudo_entrada() -> str:
    return (
        Path(sys.argv[1]).read_text(encoding="utf-8-sig")
        if len(sys.argv) > 1
        else sys.stdin.read()
    )


def ler_dados_entrada(ler_entrada: Callable[[str], object]):
    try:
        return ler_entrada(obter_conteudo_entrada())
    except ValueError as erro:
        print(f"Erro na entrada: {erro}")
        raise SystemExit(1) from erro


def ler_matriz_inteiros(
    linhas: list[str],
    numero_linhas: int,
    numero_colunas: int,
    erro_linhas: str,
    erro_colunas: str,
) -> list[list[int]]:
    if len(linhas) != numero_linhas:
        raise ValueError(erro_linhas)

    matriz = [list(map(int, linha.split())) for linha in linhas]
    if any(len(linha) != numero_colunas for linha in matriz):
        raise ValueError(erro_colunas)

    return matriz
