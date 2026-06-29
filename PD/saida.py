from docplex.mp.model import Model

from comum.saida import imprimir_matriz, imprimir_status_solucao


def imprimir_dados(dados) -> None:
    print("Verificacao da leitura dos dados:")
    print(f"Agentes: {len(dados.custos)} | Tarefas: {len(dados.custos)}")
    imprimir_matriz("Custos", "Agente", "A", "T", dados.custos)


def imprimir_resultado(modelo: Model, solucao, dados, designacoes: list[list]) -> None:
    if not imprimir_status_solucao(modelo, solucao):
        return

    print(f"Custo minimo = {solucao.objective_value:.0f}")

    print("\nDesignacoes realizadas:")
    print(f"{'Agente':>6} | {'Tarefa':>6} | {'Custo':>5}")
    print("-" * 29)

    for agente, linha in enumerate(designacoes):
        for tarefa, variavel in enumerate(linha):
            if solucao.get_value(variavel) <= 0.5:
                continue

            print(
                f"{agente + 1:>6} | {tarefa + 1:>6} | "
                f"{dados.custos[agente][tarefa]:>5}"
            )
