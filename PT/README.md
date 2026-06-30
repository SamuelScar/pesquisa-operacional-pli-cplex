# PT - Problema do Transporte

## O que e

O Problema do Transporte busca distribuir produtos de origens para destinos com o menor custo possivel.

No nosso exemplo:

- Cada origem possui uma oferta.
- Cada destino possui uma demanda.
- Cada rota origem-destino possui um custo unitario.
- A soma das ofertas deve atender a soma das demandas.

## Como resolvemos

O codigo monta uma PLI e deixa o CPLEX resolver.

A modelagem usada e:

- Variavel de decisao: quantidade enviada de cada origem para cada destino.
- Objetivo: minimizar o custo total de transporte.
- Restricoes: cada origem envia sua oferta e cada destino recebe sua demanda.

Cada par origem-destino vira uma variavel inteira:

```python
x_origem_destino
```

Por exemplo, `x_1_2` representa quanto sera enviado da origem `1` para o destino `2`.

## Entrada

O programa sempre le o arquivo fixo:

```txt
PT/in.txt
```

Formato:

```txt
oferta_1 oferta_2 ... oferta_O
demanda_1 demanda_2 ... demanda_D
custos_da_origem_1
...
custos_da_origem_O
```

Onde:

- A primeira linha informa as ofertas.
- A segunda linha informa as demandas.
- As linhas seguintes formam a matriz de custos.
- Cada linha da matriz representa uma origem.
- Cada coluna da matriz representa um destino.

## Fluxo do codigo

1. `main.py` le `PT/in.txt`.
2. `entrada.py` transforma ofertas, demandas e custos em dados Python.
3. `modelagem.py` cria uma variavel para cada rota origem-destino.
4. `modelagem.py` minimiza o custo total.
5. `modelagem.py` adiciona as restricoes de oferta.
6. `modelagem.py` adiciona as restricoes de demanda.
7. O CPLEX resolve o modelo.
8. `saida.py` mostra os transportes realizados e o custo minimo.

## Modelagem

Para cada origem:

```txt
soma do que ela envia = oferta da origem
```

Para cada destino:

```txt
soma do que ele recebe = demanda do destino
```

A funcao objetivo e:

```txt
minimizar soma(custo da rota * quantidade transportada)
```

## Resultado esperado

O exemplo vem dos slides do professor.

Valor otimo esperado para comparar com o LINGO:

```txt
1330
```

## Execucao

Com Docker:

```bash
docker compose run --rm app python PT/main.py
```

Sem Docker:

```bash
python PT/main.py
```
