from docplex.mp.model import Model

from entrada import DadosDesignacao


def montar_modelo(dados: DadosDesignacao) -> tuple[Model, list[list]]:
    modelo = Model(name="PD")
    quantidade = len(dados.custos)

    # Variavel x_ij: 1 se o agente i for designado para a tarefa j; 0 caso contrario.
    designacoes = [
        [
            modelo.binary_var(name=f"x_{agente + 1}_{tarefa + 1}")
            for tarefa in range(quantidade)
        ]
        for agente in range(quantidade)
    ]

    # Objetivo: minimizar o custo total das designacoes escolhidas.
    modelo.minimize(
        modelo.sum(
            dados.custos[agente][tarefa] * designacoes[agente][tarefa]
            for agente in range(quantidade)
            for tarefa in range(quantidade)
        )
    )

    # Cada agente deve executar exatamente uma tarefa.
    for agente in range(quantidade):
        tarefas_do_agente = modelo.sum(
            designacoes[agente][tarefa] for tarefa in range(quantidade)
        )
        modelo.add_constraint(
            tarefas_do_agente == 1,
            ctname=f"designacao_agente_{agente + 1}",
        )

    # Cada tarefa deve receber exatamente um agente.
    for tarefa in range(quantidade):
        agentes_da_tarefa = modelo.sum(
            designacoes[agente][tarefa] for agente in range(quantidade)
        )
        modelo.add_constraint(
            agentes_da_tarefa == 1,
            ctname=f"designacao_tarefa_{tarefa + 1}",
        )

    return modelo, designacoes
