from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from comum.entrada import ler_dados_entrada
from entrada import ler_entrada
from modelagem import montar_modelo
from saida import imprimir_dados, imprimir_resultado


def main() -> None:
    numero_vertices, saldos, arestas = ler_dados_entrada(ler_entrada)

    imprimir_dados(numero_vertices, saldos, arestas)
    modelo, fluxos = montar_modelo(numero_vertices, saldos, arestas)
    solucao = modelo.solve(log_output=False)
    imprimir_resultado(modelo, solucao, fluxos, arestas)


if __name__ == "__main__":
    main()

