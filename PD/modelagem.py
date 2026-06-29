from docplex.mp.model import Model

from comum.modelagem import criar_modelo
from entrada import DadosDesignacao


def montar_modelo(dados: DadosDesignacao) -> tuple[Model, list[list]]:
    modelo = criar_modelo("PD")
    quantidade = len(dados.custos)
    designacoes = [
        [
            modelo.binary_var(name=f"x_{agente + 1}_{tarefa + 1}")
            for tarefa in range(quantidade)
        ]
        for agente in range(quantidade)
    ]

    modelo.minimize(
        modelo.sum(
            dados.custos[agente][tarefa] * designacoes[agente][tarefa]
            for agente in range(quantidade)
            for tarefa in range(quantidade)
        )
    )

    for agente in range(quantidade):
        tarefas_do_agente = modelo.sum(
            designacoes[agente][tarefa] for tarefa in range(quantidade)
        )
        modelo.add_constraint(
            tarefas_do_agente == 1,
            ctname=f"designacao_agente_{agente + 1}",
        )

    for tarefa in range(quantidade):
        agentes_da_tarefa = modelo.sum(
            designacoes[agente][tarefa] for agente in range(quantidade)
        )
        modelo.add_constraint(
            agentes_da_tarefa == 1,
            ctname=f"designacao_tarefa_{tarefa + 1}",
        )

    return modelo, designacoes
