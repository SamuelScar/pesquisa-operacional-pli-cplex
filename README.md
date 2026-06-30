# Pesquisa Operacional - PLI

Implementacao em Python de modelos classicos de Programacao Linear Inteira usando Docplex e CPLEX.

O projeto resolve cinco problemas:

- `PFCM`: Problema de Fluxo de Custo Minimo.
- `PFM`: Problema de Fluxo Maximo.
- `PCM`: Problema do Caminho Minimo.
- `PT`: Problema do Transporte.
- `PD`: Problema da Designacao.

## Premissa das entradas

Cada problema possui um arquivo fixo chamado `in.txt` dentro da propria pasta.

O codigo assume que esse arquivo ja esta correto e segue exatamente a estrutura esperada. Por isso, os leitores de entrada apenas convertem o conteudo do arquivo para estruturas em Python, sem validacoes adicionais.

Para testar outro caso, altere o `in.txt` da pasta do problema.

## Estrutura

Cada problema fica em sua propria pasta e segue a mesma divisao:

- `entrada.py`: le o `in.txt` e converte os dados para Python.
- `modelagem.py`: monta o modelo matematico no Docplex.
- `saida.py`: imprime os dados lidos e o resultado da solucao.
- `main.py`: le o `in.txt`, monta o modelo, chama o CPLEX e imprime a saida.
- `in.txt`: entrada fixa do problema.
- `README.md`: explica o problema e a modelagem usada.


## Como executar

Use Docker para executar os modelos.

Formato geral:

```bash
docker compose run --rm app python <problema>/main.py
```

Comandos por problema:

```bash
docker compose run --rm app python PFCM/main.py
docker compose run --rm app python PFM/main.py
docker compose run --rm app python PCM/main.py
docker compose run --rm app python PT/main.py
docker compose run --rm app python PD/main.py
```

## Comparacao com LINGO

Os arquivos `in.txt` foram ajustados para os exemplos dos slides. Os valores otimos esperados para comparacao sao:

- `PFCM`: 184.
- `PT`: 1330.
- `PD`: 96.
- `PCM`: 22.
- `PFM`: 19.

## Limite do CPLEX Community

A versao Community do CPLEX possui limite de 1000 variaveis e 1000 restricoes.

Nos modelos de grafo, cada aresta normalmente gera uma variavel, entao entradas muito grandes podem ultrapassar esse limite.
