# PT - Problema do Transporte

## O que e

O Problema do Transporte busca distribuir produtos de origens para destinos com o menor custo total.

Cada origem possui uma oferta. Cada destino possui uma demanda. Cada rota entre origem e destino possui um custo unitario.

## Como resolvemos

Modelamos o problema como uma PLI com matriz de custos.

Variavel de decisao:

- `x_ij`: quantidade inteira transportada da origem `i` para o destino `j`.

Funcao objetivo:

- Minimizar a soma do custo de cada rota multiplicado pela quantidade transportada nela.

Restricoes:

- Cada origem deve enviar exatamente sua oferta.
- Cada destino deve receber exatamente sua demanda.
- As quantidades transportadas sao inteiras e nao negativas.

## Fluxo da resolucao

1. `main.py` recebe o arquivo de entrada.
2. `entrada.py` le ofertas, demandas e matriz de custos.
3. `entrada.py` valida os tamanhos das listas, o equilibrio entre oferta e demanda e os custos.
4. `modelagem.py` cria uma variavel de quantidade para cada par origem-destino.
5. `modelagem.py` monta a funcao objetivo e as restricoes de oferta e demanda.
6. O CPLEX resolve o modelo minimizando o custo total.
7. `saida.py` imprime os dados lidos, o custo minimo e os transportes realizados.

## Formato do arquivo `in.txt`

```txt
O D
oferta_1 ... oferta_O
demanda_1 ... demanda_D
custos_da_origem_1
...
custos_da_origem_O
```

Onde:

- `O`: numero de origens.
- `D`: numero de destinos.
- A segunda linha informa as ofertas.
- A terceira linha informa as demandas.
- As linhas seguintes formam a matriz de custos.

A soma das ofertas deve ser igual a soma das demandas.

## Execucao

```bash
docker compose run --rm app python PT/main.py PT/in.txt
```
