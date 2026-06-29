# PD - Problema da Designacao

## O que e

O Problema da Designacao busca alocar agentes a tarefas com o menor custo total.

Cada agente deve receber uma tarefa, e cada tarefa deve ser atribuida a um unico agente.

## Como resolvemos

Modelamos o problema como uma PLI com matriz quadrada de custos.

Variavel de decisao:

- `x_ij`: indica se o agente `i` foi designado para a tarefa `j`.

Funcao objetivo:

- Minimizar a soma dos custos das designacoes escolhidas.

Restricoes:

- Cada agente deve receber exatamente uma tarefa.
- Cada tarefa deve receber exatamente um agente.
- As variaveis sao binarias.

## Fluxo da resolucao

1. `main.py` recebe o arquivo de entrada.
2. `entrada.py` le a matriz de custos.
3. `entrada.py` valida a quantidade de agentes/tarefas, a matriz quadrada e os custos.
4. `modelagem.py` cria uma variavel binaria para cada par agente-tarefa.
5. `modelagem.py` monta a funcao objetivo e as restricoes de designacao.
6. O CPLEX resolve o modelo minimizando o custo total.
7. `saida.py` imprime os dados lidos, o custo minimo e as designacoes realizadas.

## Formato do arquivo `in.txt`

```txt
N
custos_do_agente_1
...
custos_do_agente_N
```

Onde:

- `N`: numero de agentes e tarefas.
- As linhas seguintes formam a matriz quadrada de custos.

## Execucao

```bash
docker compose run --rm app python PD/main.py PD/in.txt
```
