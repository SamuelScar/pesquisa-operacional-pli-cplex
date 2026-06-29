from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from comum.entrada import ler_dados_entrada
from entrada import ler_entrada
from modelagem import montar_modelo
from saida import imprimir_dados, imprimir_resultado


def main() -> None:
    numero_vertices, origem_caminho, destino_caminho, arestas = ler_dados_entrada(
        ler_entrada
    )

    imprimir_dados(numero_vertices, origem_caminho, destino_caminho, arestas)
    modelo, escolhas = montar_modelo(
        numero_vertices,
        origem_caminho,
        destino_caminho,
        arestas,
    )
    solucao = modelo.solve(log_output=False)
    imprimir_resultado(
        modelo,
        solucao,
        origem_caminho,
        destino_caminho,
        escolhas,
        arestas,
    )


if __name__ == "__main__":
    main()

