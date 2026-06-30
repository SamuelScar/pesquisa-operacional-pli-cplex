def imprimir_dados(dados) -> None:
    print("Dados do PD:")
    print(f"Agentes: {len(dados.custos)}")
    print(f"Tarefas: {len(dados.custos)}")


def imprimir_resultado(solucao, dados, designacoes: list[list]) -> None:
    if solucao is None:
        print("Sem solucao")
        return

    print(f"\nCusto minimo = {solucao.objective_value:.0f}")
    print("\nDesignacoes:")

    for agente, linha in enumerate(designacoes, start=1):
        for tarefa, variavel in enumerate(linha, start=1):
            if solucao.get_value(variavel) > 0.5:
                custo = dados.custos[agente - 1][tarefa - 1]
                print(f"Agente {agente} -> tarefa {tarefa}: custo {custo}")
