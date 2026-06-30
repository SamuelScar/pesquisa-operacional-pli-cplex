def imprimir_dados(dados) -> None:
    print("Dados do PT:")
    print(f"Origens: {len(dados.ofertas)}")
    print(f"Destinos: {len(dados.demandas)}")
    print(f"Ofertas: {dados.ofertas}")
    print(f"Demandas: {dados.demandas}")


def imprimir_resultado(solucao, dados, quantidades: list[list]) -> None:
    if solucao is None:
        print("Sem solucao")
        return

    print(f"\nCusto minimo = {solucao.objective_value:.0f}")
    print("\nTransportes positivos:")

    for origem, linha in enumerate(quantidades, start=1):
        for destino, variavel in enumerate(linha, start=1):
            valor = solucao.get_value(variavel)
            if valor > 0:
                print(f"Origem {origem} -> destino {destino}: {valor:.0f}")
