# PD - Problema da Designacao

## O que e

O Problema da Designacao busca escolher a melhor combinacao entre agentes e tarefas com o menor custo possivel.

No nosso exemplo:

- Cada agente deve executar uma tarefa.
- Cada tarefa deve ser executada por um agente.
- Cada combinacao agente-tarefa possui um custo.

## Como resolvemos

O codigo monta uma PLI binaria e deixa o CPLEX resolver.

A modelagem usada e:

- Variavel de decisao: escolher ou nao uma designacao agente-tarefa.
- Objetivo: minimizar o custo total das designacoes escolhidas.
- Restricoes: cada agente aparece uma vez e cada tarefa aparece uma vez.

Cada par agente-tarefa vira uma variavel binaria:

```python
x_agente_tarefa
```

Ela pode valer:

- `1`: agente foi escolhido para a tarefa.
- `0`: agente nao foi escolhido para a tarefa.

## Entrada

O programa sempre le o arquivo fixo:

```txt
PD/in.txt
```

Formato:

```txt
custos_do_agente_1
custos_do_agente_2
...
custos_do_agente_N
```

Onde:

- Cada linha representa um agente.
- Cada coluna representa uma tarefa.
- O valor na posicao da matriz e o custo daquela designacao.

## Fluxo do codigo

1. `main.py` le `PD/in.txt`.
2. `entrada.py` transforma a matriz de custos em dados Python.
3. `modelagem.py` cria uma variavel binaria para cada agente-tarefa.
4. `modelagem.py` minimiza o custo total.
5. `modelagem.py` garante uma tarefa para cada agente.
6. `modelagem.py` garante um agente para cada tarefa.
7. O CPLEX resolve o modelo.
8. `saida.py` mostra as designacoes escolhidas e o custo minimo.

## Modelagem

Para cada agente:

```txt
soma das tarefas escolhidas para ele = 1
```

Para cada tarefa:

```txt
soma dos agentes escolhidos para ela = 1
```

A funcao objetivo e:

```txt
minimizar soma(custo da designacao * variavel escolhida)
```

## Resultado esperado

O exemplo vem dos slides do professor.

Valor otimo esperado para comparar com o LINGO:

```txt
96
```

## Execucao

Com Docker:

```bash
docker compose run --rm app python PD/main.py
```

Sem Docker:

```bash
python PD/main.py
```
