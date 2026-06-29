from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from comum.entrada import ler_dados_entrada
from entrada import ler_entrada
from modelagem import montar_modelo
from saida import imprimir_dados, imprimir_resultado


def main() -> None:
    dados = ler_dados_entrada(ler_entrada)

    imprimir_dados(dados)
    modelo, quantidades = montar_modelo(dados)
    solucao = modelo.solve(log_output=False)
    imprimir_resultado(modelo, solucao, dados, quantidades)


if __name__ == "__main__":
    main()

