# PFM - Problema de Fluxo Maximo

## O que e

O Problema de Fluxo Maximo busca enviar a maior quantidade possivel de fluxo de uma origem ate um destino.

A rede e formada por vertices e arestas direcionadas. Cada aresta possui uma capacidade maxima.

## Como resolvemos

Modelamos o problema como uma PLI em um grafo direcionado.

Variaveis de decisao:

- `x_ij`: quantidade inteira de fluxo enviada pela aresta `i -> j`.
- `fluxo_maximo`: quantidade total enviada da origem ao destino.

Funcao objetivo:

- Maximizar `fluxo_maximo`.

Restricoes:

- A origem deve ter saida liquida igual ao fluxo maximo.
- O destino deve ter entrada liquida igual ao fluxo maximo.
- Os demais vertices devem conservar fluxo.
- O fluxo de cada aresta deve ficar entre zero e sua capacidade maxima.
- As variaveis de fluxo sao inteiras.

## Fluxo da resolucao

1. `main.py` recebe o arquivo de entrada.
2. `entrada.py` le os vertices, a origem, o destino e as arestas.
3. `entrada.py` valida origem, destino, vertices das arestas e capacidades.
4. `modelagem.py` cria a variavel `fluxo_maximo` e as variaveis de fluxo das arestas.
5. `modelagem.py` monta as restricoes de conservacao de fluxo.
6. O CPLEX resolve o modelo maximizando o fluxo total.
7. `saida.py` imprime os dados lidos, o fluxo maximo e as arestas com fluxo positivo.

## Formato do arquivo `in.txt`

```txt
N M
origem destino
origem_aresta destino_aresta capacidade
...
```

Onde:

- `N`: numero de vertices.
- `M`: numero de arestas.
- A segunda linha informa a origem e o destino do fluxo.
- Cada aresta possui origem, destino e capacidade maxima.

## Execucao

```bash
docker compose run --rm app python PFM/main.py PFM/in.txt
```
