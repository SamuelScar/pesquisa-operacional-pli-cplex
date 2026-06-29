# PCM - Problema do Caminho Minimo

## O que e

O Problema do Caminho Minimo busca encontrar o caminho de menor custo entre uma origem e um destino.

A rede e formada por vertices e arestas direcionadas. Cada aresta possui um custo.

## Como resolvemos

Modelamos o problema como uma PLI em um grafo direcionado.

Variavel de decisao:

- `x_ij`: indica se a aresta `i -> j` entra no caminho.

Funcao objetivo:

- Minimizar a soma dos custos das arestas escolhidas.

Restricoes:

- A origem deve ter uma unidade liquida de saida.
- O destino deve ter uma unidade liquida de entrada.
- Os demais vertices devem conservar fluxo.
- As variaveis sao binarias.

## Fluxo da resolucao

1. `main.py` recebe o arquivo de entrada.
2. `entrada.py` le os vertices, a origem, o destino e as arestas.
3. `entrada.py` valida origem, destino, vertices das arestas e custos.
4. `modelagem.py` cria uma variavel binaria para cada aresta.
5. `modelagem.py` monta a funcao objetivo e as restricoes de balanco nos vertices.
6. O CPLEX resolve o modelo minimizando o custo total.
7. `saida.py` imprime os dados lidos, o custo minimo e o caminho encontrado.

## Formato do arquivo `in.txt`

```txt
N M
origem destino
origem_aresta destino_aresta custo
...
```

Onde:

- `N`: numero de vertices.
- `M`: numero de arestas.
- A segunda linha informa a origem e o destino do caminho.
- Cada aresta possui origem, destino e custo.

As arestas sao tratadas como direcionadas. Para uma ligacao valer nos dois sentidos, informe as duas direcoes.

## Execucao

```bash
docker compose run --rm app python PCM/main.py PCM/in.txt
```
