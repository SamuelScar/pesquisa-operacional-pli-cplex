# PFCM - Problema de Fluxo de Custo Minimo

## O que e

O Problema de Fluxo de Custo Minimo busca enviar unidades por uma rede pagando o menor custo possivel.

No nosso exemplo, a rede tem:

- Vertices com oferta, que precisam enviar fluxo.
- Vertices com demanda, que precisam receber fluxo.
- Vertices de transbordo, que apenas recebem e repassam fluxo.
- Arestas direcionadas, cada uma com custo e capacidade maxima.

## Como resolvemos

O codigo nao implementa Simplex manualmente. Ele monta o modelo matematico e deixa o CPLEX resolver.

A modelagem usada e:

- Variavel de decisao: fluxo enviado em cada aresta.
- Objetivo: minimizar o custo total do fluxo.
- Restricoes: respeitar o saldo de cada vertice e a capacidade das arestas.

Cada aresta vira uma variavel inteira:

```python
x_origem_destino_indice
```

Por exemplo, `x_2_3_1` representa o fluxo enviado pela aresta `2 -> 3`.

## Entrada

O programa sempre le o arquivo fixo:

```txt
PFCM/in.txt
```

Formato:

```txt
N
b1 b2 ... bN
origem destino custo capacidade
...
```

Onde:

- `N`: quantidade de vertices.
- `b1 b2 ... bN`: saldo de cada vertice.
- Saldo positivo: oferta.
- Saldo negativo: demanda.
- Saldo zero: transbordo.
- Cada linha seguinte representa uma aresta.

Exemplo:

```txt
2 3 2 30
```

Significa uma aresta `2 -> 3`, com custo `2` e capacidade `30`.

## Fluxo do codigo

1. `main.py` le `PFCM/in.txt`.
2. `entrada.py` transforma o texto em dados Python.
3. `modelagem.py` cria o modelo do CPLEX.
4. `modelagem.py` cria uma variavel para cada aresta.
5. `modelagem.py` minimiza o custo total.
6. `modelagem.py` adiciona o balanco de cada vertice.
7. O CPLEX resolve o modelo.
8. `saida.py` mostra os fluxos positivos e o custo minimo.

## Modelagem

Para cada vertice:

```txt
fluxo que sai - fluxo que entra = saldo do vertice
```

Entao:

- Vertice de oferta precisa enviar mais do que recebe.
- Vertice de demanda precisa receber mais do que envia.
- Vertice de transbordo precisa enviar tudo que recebe.

A funcao objetivo e:

```txt
minimizar soma(custo da aresta * fluxo da aresta)
```

As capacidades entram diretamente no limite superior das variaveis.

## Resultado esperado

O exemplo vem dos slides do professor.

Valor otimo esperado para comparar com o LINGO:

```txt
184
```

## Execucao

Com Docker:

```bash
docker compose run --rm --build app python PFCM/main.py
```

Sem Docker:

```bash
python PFCM/main.py
```

