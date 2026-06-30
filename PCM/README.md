# PCM - Problema do Caminho Minimo

## O que e

O Problema do Caminho Minimo busca encontrar o caminho de menor custo entre uma origem e um destino.

No nosso exemplo:

- A rede possui vertices e arestas direcionadas.
- Cada aresta possui um custo.
- O objetivo e escolher quais arestas formam o caminho mais barato.

## Como resolvemos

O codigo monta uma PLI binaria e deixa o CPLEX resolver.

A modelagem usada e:

- Variavel de decisao: escolher ou nao cada aresta.
- Objetivo: minimizar o custo das arestas escolhidas.
- Restricoes: formar um caminho valido da origem ate o destino.

Cada aresta vira uma variavel binaria:

```python
x_origem_destino_indice
```

Ela pode valer:

- `1`: a aresta faz parte do caminho.
- `0`: a aresta nao faz parte do caminho.

## Entrada

O programa sempre le o arquivo fixo:

```txt
PCM/in.txt
```

Formato:

```txt
N
origem destino
origem_aresta destino_aresta custo
...
```

Onde:

- `N`: quantidade de vertices.
- A segunda linha informa a origem e o destino do caminho.
- Cada linha seguinte representa uma aresta com custo.

As arestas sao direcionadas. Se uma ligacao puder ser usada nos dois sentidos, as duas direcoes precisam aparecer no arquivo.

## Fluxo do codigo

1. `main.py` le `PCM/in.txt`.
2. `entrada.py` transforma vertices, origem, destino e arestas em dados Python.
3. `modelagem.py` cria uma variavel binaria para cada aresta.
4. `modelagem.py` minimiza o custo total das arestas escolhidas.
5. `modelagem.py` adiciona o balanco dos vertices.
6. O CPLEX resolve o modelo.
7. `saida.py` mostra o caminho escolhido e o custo minimo.

## Modelagem

Para cada vertice:

```txt
arestas escolhidas que saem - arestas escolhidas que entram = balanco
```

O balanco muda conforme o vertice:

- Origem: balanco `1`, porque o caminho sai dela.
- Destino: balanco `-1`, porque o caminho chega nela.
- Outros vertices: balanco `0`, porque se entra no caminho, tambem precisa sair.

A funcao objetivo e:

```txt
minimizar soma(custo da aresta * escolha da aresta)
```

## Resultado esperado

O exemplo vem dos slides do professor.

Valor otimo esperado para comparar com o LINGO:

```txt
22
```

## Execucao

Com Docker:

```bash
docker compose run --rm --build app python PCM/main.py
```

Sem Docker:

```bash
python PCM/main.py
```

