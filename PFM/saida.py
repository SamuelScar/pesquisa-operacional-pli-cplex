from docplex.mp.model import Model

from comum.saida import (
    imprimir_cabecalho_variaveis_arestas,
    imprimir_linha_variavel_aresta,
    imprimir_status_solucao,
)


def imprimir_dados(
    numero_vertices: int,
    origem_fluxo: int,
    destino_fluxo: int,
    arestas: list,
) -> None:
    print("Verificacao da leitura dos dados:")
    print(
        f"Vertices: {numero_vertices} | Arestas: {len(arestas)} | "
        f"Origem: {origem_fluxo} | Destino: {destino_fluxo}"
    )

    print("\nArestas:")
    print(f"{'Indice':>6} | {'Origem':>6} | {'Destino':>7} | {'Cap.':>5}")
    print("-" * 36)
    for indice, aresta in enumerate(arestas, start=1):
        print(
            f"{indice:>6} | {aresta.origem:>6} | "
            f"{aresta.destino:>7} | {aresta.capacidade:>5}"
        )


def imprimir_resultado(
    modelo: Model,
    solucao,
    fluxo_maximo,
    fluxos: list,
    arestas: list,
) -> None:
    if not imprimir_status_solucao(modelo, solucao):
        return

    print(f"Fluxo maximo = {solucao.get_value(fluxo_maximo):.0f}")

    fluxos_positivos = []
    for indice, (aresta, fluxo) in enumerate(zip(arestas, fluxos), start=1):
        valor = solucao.get_value(fluxo)
        if valor > 0:
            fluxos_positivos.append((indice, aresta, fluxo, valor))

    print("\nFluxos positivos:")
    imprimir_cabecalho_variaveis_arestas()
    for indice, aresta, fluxo, valor in fluxos_positivos:
        imprimir_linha_variavel_aresta(indice, fluxo, aresta, valor)

    print(f"Arestas sem fluxo: {len(arestas) - len(fluxos_positivos)}")
