# PFM - Problema de Fluxo Maximo

## O que e

O Problema de Fluxo Maximo busca enviar a maior quantidade possivel de fluxo de uma origem ate um destino.

No nosso exemplo:

- A rede possui vertices e arestas direcionadas.
- Cada aresta possui uma capacidade maxima.
- O objetivo e descobrir quanto fluxo consegue sair da origem e chegar ao destino.

## Como resolvemos

O codigo monta uma PLI e deixa o CPLEX resolver.

A modelagem usada e:

- Variavel de decisao: fluxo enviado em cada aresta.
- Variavel principal: `fluxo_maximo`, que representa o total enviado.
- Objetivo: maximizar `fluxo_maximo`.
- Restricoes: respeitar capacidades e conservar fluxo nos vertices intermediarios.

Cada aresta vira uma variavel inteira:

```python
x_origem_destino_indice
```

Alem disso, o modelo cria:

```python
fluxo_maximo
```

Essa variavel e o valor que o CPLEX tenta deixar o maior possivel.

## Entrada

O programa sempre le o arquivo fixo:

```txt
PFM/in.txt
```

Formato:

```txt
N
origem destino
origem_aresta destino_aresta capacidade
...
```

Onde:

- `N`: quantidade de vertices.
- A segunda linha informa a origem e o destino do fluxo.
- Cada linha seguinte representa uma aresta com capacidade maxima.

## Fluxo do codigo

1. `main.py` le `PFM/in.txt`.
2. `entrada.py` transforma vertices, origem, destino e arestas em dados Python.
3. `modelagem.py` cria a variavel `fluxo_maximo`.
4. `modelagem.py` cria uma variavel de fluxo para cada aresta.
5. `modelagem.py` maximiza `fluxo_maximo`.
6. `modelagem.py` adiciona o balanco dos vertices.
7. O CPLEX resolve o modelo.
8. `saida.py` mostra o fluxo maximo e os fluxos positivos.

## Modelagem

Para cada vertice:

```txt
fluxo que sai - fluxo que entra = balanco
```

O balanco muda conforme o vertice:

- Origem: balanco `fluxo_maximo`, porque gera o fluxo.
- Destino: balanco `-fluxo_maximo`, porque recebe o fluxo.
- Outros vertices: balanco `0`, porque apenas repassam fluxo.

A funcao objetivo e:

```txt
maximizar fluxo_maximo
```

As capacidades entram diretamente no limite superior das variaveis das arestas.

## Resultado esperado

O exemplo vem dos slides do professor.

Valor otimo esperado para comparar com o LINGO:

```txt
19
```

## Execucao

Com Docker:

```bash
docker compose run --rm app python PFM/main.py
```

Sem Docker:

```bash
python PFM/main.py
```
