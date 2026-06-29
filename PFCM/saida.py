from docplex.mp.model import Model

from comum.saida import (
    imprimir_cabecalho_variaveis_arestas,
    imprimir_linha_variavel_aresta,
    imprimir_status_solucao,
)


def imprimir_dados(numero_vertices: int, saldos: list[int], arestas: list) -> None:
    print("Verificacao da leitura dos dados:")
    print(f"Vertices: {numero_vertices} | Arestas: {len(arestas)}")
    saldos_relevantes = [
        (vertice, saldo)
        for vertice, saldo in enumerate(saldos, start=1)
        if saldo != 0
    ]
    total_transbordo = numero_vertices - len(saldos_relevantes)

    print("\nSaldos diferentes de zero:")
    print(f"{'Vertice':>7} | {'Saldo':>6}")
    print("-" * 18)
    for vertice, saldo in saldos_relevantes:
        print(f"{vertice:>7} | {saldo:>6}")
    print(f"Vertices de transbordo: {total_transbordo}")

    print("\nArestas:")
    print(
        f"{'Indice':>6} | {'Origem':>6} | {'Destino':>7} | "
        f"{'Custo':>5} | {'Cap.':>5}"
    )
    print("-" * 45)
    for indice, aresta in enumerate(arestas, start=1):
        print(
            f"{indice:>6} | {aresta.origem:>6} | {aresta.destino:>7} | "
            f"{aresta.custo:>5} | {aresta.capacidade:>5}"
        )


def imprimir_resultado(modelo: Model, solucao, fluxos: list, arestas: list) -> None:
    if not imprimir_status_solucao(modelo, solucao):
        return

    print("Variaveis de decisao:")
    imprimir_cabecalho_variaveis_arestas()

    for indice, (aresta, fluxo) in enumerate(zip(arestas, fluxos), start=1):
        imprimir_linha_variavel_aresta(
            indice,
            fluxo,
            aresta,
            solucao.get_value(fluxo),
        )

    print(f"\nFuncao Objetivo Valor = {solucao.objective_value:.0f}")
