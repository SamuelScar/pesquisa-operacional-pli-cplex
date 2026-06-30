# Pesquisa Operacional - PLI

Implementacao em Python de modelos classicos de Programacao Linear Inteira usando Docplex e CPLEX.

O projeto resolve cinco problemas:

- `PFCM`: Problema de Fluxo de Custo Minimo.
- `PFM`: Problema de Fluxo Maximo.
- `PCM`: Problema do Caminho Minimo.
- `PT`: Problema do Transporte.
- `PD`: Problema da Designacao.

Cada pasta possui seu proprio `README.md` com a explicacao do problema, entrada, modelagem e resultado esperado para comparacao com o LINGO.

## Estrutura

Cada problema segue a mesma organizacao:

- `entrada.py`: le o `in.txt` da propria pasta.
- `modelagem.py`: monta o modelo no Docplex.
- `saida.py`: imprime o resultado de forma resumida.
- `main.py`: organiza a execucao.
- `in.txt`: entrada fixa usada no exemplo.

O codigo assume que os arquivos `in.txt` estao corretos e prontos para uso, sem validacoes extras de leitura.

## Como executar

Use Docker na raiz do projeto. O `--build` prepara a imagem com as dependencias antes de executar:

```bash
docker compose run --rm --build app python <problema>/main.py
```

Exemplos:

```bash
docker compose run --rm --build app python PFCM/main.py
docker compose run --rm --build app python PFM/main.py
docker compose run --rm --build app python PCM/main.py
docker compose run --rm --build app python PT/main.py
docker compose run --rm --build app python PD/main.py
```

## Observacao

A versao Community do CPLEX possui limite de 1000 variaveis e 1000 restricoes.


