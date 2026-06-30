from pathlib import Path

from entrada import ler_entrada
from modelagem import montar_modelo
from saida import imprimir_dados, imprimir_resultado


def main() -> None:
    conteudo = Path(__file__).with_name("in.txt").read_text()
    numero_vertices, origem_fluxo, destino_fluxo, arestas = ler_entrada(conteudo)

    imprimir_dados(numero_vertices, origem_fluxo, destino_fluxo, arestas)
    modelo, fluxos, fluxo_maximo = montar_modelo(
        numero_vertices,
        origem_fluxo,
        destino_fluxo,
        arestas,
    )
    solucao = modelo.solve(log_output=False)
    imprimir_resultado(solucao, fluxo_maximo, fluxos, arestas)


if __name__ == "__main__":
    main()
