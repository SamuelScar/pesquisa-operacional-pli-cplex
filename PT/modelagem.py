from docplex.mp.model import Model

from entrada import DadosTransporte


def montar_modelo(dados: DadosTransporte) -> tuple[Model, list[list]]:
    modelo = Model(name="PT")
    numero_origens = len(dados.ofertas)
    numero_destinos = len(dados.demandas)

    # Variavel x_ij: quantidade transportada da origem i para o destino j.
    quantidades = [
        [
            modelo.integer_var(lb=0, name=f"x_{origem + 1}_{destino + 1}")
            for destino in range(numero_destinos)
        ]
        for origem in range(numero_origens)
    ]

    # Objetivo: minimizar o custo total de transporte.
    modelo.minimize(
        modelo.sum(
            dados.custos[origem][destino] * quantidades[origem][destino]
            for origem in range(numero_origens)
            for destino in range(numero_destinos)
        )
    )

    # Cada origem deve enviar exatamente sua oferta.
    for origem, oferta in enumerate(dados.ofertas):
        total_origem = modelo.sum(
            quantidades[origem][destino] for destino in range(numero_destinos)
        )
        modelo.add_constraint(total_origem == oferta, ctname=f"oferta_origem_{origem + 1}")

    # Cada destino deve receber exatamente sua demanda.
    for destino, demanda in enumerate(dados.demandas):
        total_destino = modelo.sum(
            quantidades[origem][destino] for origem in range(numero_origens)
        )
        modelo.add_constraint(
            total_destino == demanda,
            ctname=f"demanda_destino_{destino + 1}",
        )

    return modelo, quantidades
