from pathlib import Path

from entrada import ler_entrada
from modelagem import montar_modelo
from saida import imprimir_dados, imprimir_resultado


def main() -> None:
    conteudo = Path(__file__).with_name("in.txt").read_text()
    dados = ler_entrada(conteudo)

    imprimir_dados(dados)
    modelo, designacoes = montar_modelo(dados)
    solucao = modelo.solve(log_output=False)
    imprimir_resultado(solucao, dados, designacoes)


if __name__ == "__main__":
    main()
