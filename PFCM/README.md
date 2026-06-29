# PFCM - Problema de Fluxo de Custo Minimo

## O que e

O Problema de Fluxo de Custo Minimo busca enviar fluxo por uma rede com o menor custo possivel.

Cada vertice pode representar uma oferta, uma demanda ou um ponto de transbordo. Cada aresta possui custo unitario e capacidade maxima.

## Como resolvemos

Modelamos o problema como uma PLI em um grafo direcionado.

Variavel de decisao:

- `x_ij`: quantidade inteira de fluxo enviada pela aresta `i -> j`.

Funcao objetivo:

- Minimizar a soma do custo de cada aresta multiplicado pelo fluxo enviado nela.

Restricoes:

- O balanco de cada vertice deve respeitar seu saldo.
- O fluxo de cada aresta deve ficar entre zero e sua capacidade maxima.
- As variaveis de fluxo sao inteiras.

## Fluxo da resolucao

1. `main.py` recebe o arquivo de entrada.
2. `entrada.py` le os vertices, saldos e arestas.
3. `entrada.py` valida a quantidade de saldos, a soma dos saldos, os vertices e as capacidades.
4. `modelagem.py` cria as variaveis de fluxo e monta a funcao objetivo.
5. `modelagem.py` adiciona as restricoes de balanco de fluxo em cada vertice.
6. O CPLEX resolve o modelo.
7. `saida.py` imprime os dados lidos, os fluxos e o valor da funcao objetivo.

## Formato do arquivo `in.txt`

```txt
N M
b1 b2 ... bN
origem destino custo capacidade
...
```

Onde:

- `N`: numero de vertices.
- `M`: numero de arestas.
- `b`: saldo de cada vertice.
- Saldo positivo representa oferta.
- Saldo negativo representa demanda.
- Saldo zero representa vertice de transbordo.
- Cada aresta possui origem, destino, custo unitario e capacidade maxima.

A soma dos saldos deve ser zero.

## Execucao

```bash
docker compose run --rm app python PFCM/main.py PFCM/in.txt
```
