# Pesquisa Operacional - PLI

Implementacao em Python de modelos classicos de Programacao Linear Inteira usando Docplex e CPLEX.

O projeto resolve cinco problemas:

- `PFCM`: Problema de Fluxo de Custo Minimo.
- `PFM`: Problema de Fluxo Maximo.
- `PCM`: Problema do Caminho Minimo.
- `PT`: Problema do Transporte.
- `PD`: Problema da Designacao.

## Estrutura

Cada problema fica em sua propria pasta e segue a mesma divisao:

- `entrada.py`: le e valida os dados de entrada.
- `modelagem.py`: monta o modelo matematico no Docplex.
- `saida.py`: imprime os dados lidos e o resultado da solucao.
- `main.py`: organiza o fluxo de execucao.
- `in.txt`: exemplo de entrada para o problema.
- `README.md`: explica o problema e a modelagem usada.

A pasta `comum` guarda apenas funcoes reutilizadas por mais de um problema.

## Como executar

Use Docker para executar os modelos. O comando sempre recebe o `main.py` do problema e o arquivo de entrada.

Formato geral:

```bash
docker compose run --rm app python <problema>/main.py <problema>/in.txt
```

Exemplo:

```bash
docker compose run --rm app python PFCM/main.py PFCM/in.txt
```

Comandos por problema:

```bash
docker compose run --rm app python PFCM/main.py PFCM/in.txt
docker compose run --rm app python PFM/main.py PFM/in.txt
docker compose run --rm app python PCM/main.py PCM/in.txt
docker compose run --rm app python PT/main.py PT/in.txt
docker compose run --rm app python PD/main.py PD/in.txt
```

## Entradas

Cada pasta possui um `in.txt` com um exemplo de entrada. Para testar outro caso, altere esse arquivo ou passe outro caminho no comando.

## Limite do CPLEX Community

A versao Community do CPLEX possui limite de 1000 variaveis e 1000 restricoes.

Nos modelos de grafo, cada aresta normalmente gera uma variavel, entao entradas muito grandes podem ultrapassar esse limite.
