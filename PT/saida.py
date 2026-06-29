from docplex.mp.model import Model

from comum.saida import imprimir_lista, imprimir_matriz, imprimir_status_solucao


def imprimir_dados(dados) -> None:
    print("Verificacao da leitura dos dados:")
    print(
        f"Origens: {len(dados.ofertas)} | Destinos: {len(dados.demandas)} | "
        f"Total: {sum(dados.ofertas)}"
    )
    imprimir_lista("Ofertas", dados.ofertas)
    imprimir_lista("Demandas", dados.demandas)
    imprimir_matriz("Custos", "Origem", "O", "D", dados.custos)


def imprimir_resultado(modelo: Model, solucao, dados, quantidades: list[list]) -> None:
    if not imprimir_status_solucao(modelo, solucao):
        return

    print(f"Custo minimo = {solucao.objective_value:.0f}")

    print("\nTransportes realizados:")
    print(f"{'Origem':>6} | {'Destino':>7} | {'Qtd.':>5} | {'Custo':>5}")
    print("-" * 36)

    for origem, linha in enumerate(quantidades):
        for destino, variavel in enumerate(linha):
            valor = solucao.get_value(variavel)
            if valor <= 0:
                continue

            print(
                f"{origem + 1:>6} | {destino + 1:>7} | "
                f"{valor:>5.0f} | {dados.custos[origem][destino]:>5}"
            )
