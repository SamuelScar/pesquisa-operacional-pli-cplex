def imprimir_resumo_execucao(modelo) -> None:
    print("\n--------Informacoes da Execucao:----------\n")
    print(f"#Var: {modelo.number_of_variables}")
    print(f"#Restricoes: {modelo.number_of_constraints}")


def imprimir_status_solucao(modelo, solucao) -> bool:
    imprimir_resumo_execucao(modelo)

    if solucao is None:
        print("\nStatus da FO: No Solution")
        return False

    print(f"\nStatus da FO: {modelo.solve_details.status}")
    return True


def imprimir_lista(titulo: str, valores: list[int]) -> None:
    print(f"\n{titulo}:")
    print(f"{'Indice':>6} | {'Valor':>6}")
    print("-" * 17)
    for indice, valor in enumerate(valores, start=1):
        print(f"{indice:>6} | {valor:>6}")


def imprimir_matriz(
    titulo: str,
    rotulo_linha: str,
    prefixo_linha: str,
    prefixo_coluna: str,
    matriz: list[list[int]],
) -> None:
    print(f"\n{titulo}:")
    cabecalho = f"{rotulo_linha} | " + " | ".join(
        f"{prefixo_coluna}{indice + 1:>3}" for indice in range(len(matriz[0]))
    )
    print(cabecalho)
    print("-" * len(cabecalho))

    for indice, linha in enumerate(matriz, start=1):
        valores = " | ".join(f"{valor:>4}" for valor in linha)
        print(f"{prefixo_linha}{indice:>5} | {valores}")


def imprimir_cabecalho_variaveis_arestas(rotulo_valor: str = "Valor") -> None:
    print(
        f"{'Indice':>6} | {'Variavel':<14} | "
        f"{'Aresta':<9} | {rotulo_valor:>5}"
    )
    print("-" * 45)


def imprimir_linha_variavel_aresta(indice: int, variavel, aresta, valor: float) -> None:
    print(
        f"{indice:>6} | {variavel.name:<14} | "
        f"{aresta.origem}->{aresta.destino:<5} | {valor:>5.0f}"
    )
