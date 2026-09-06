# imdb-spark

Solução do Trabalho Prático do Módulo 3 (Soluções de Big Data e Data Lake) do
Bootcamp Engenheiro de Dados - XP Educação.

O objetivo é exercitar leitura, limpeza e análise de dados com a API de
DataFrames do Apache Spark (PySpark), a partir de uma amostra dos dados públicos
do IMDB.

## Dados

O trabalho usa dois arquivos do IMDB:

- `title_basics.tsv` — metadados dos títulos (nome, tipo, ano, duração, gênero).
- `title_ratings.tsv` — nota média e número de votos de cada título.

Descrição completa dos campos: https://www.imdb.com/interfaces/

### Por que os arquivos não estão no repositório

Os `.tsv` **não são versionados** (veja `.gitignore`). Motivos:

- Tamanho: o `title_basics.tsv` tem ~700 MB, acima do recomendado para o Git e
  além do limite de arquivo do GitHub. Versionar dados brutos incha o histórico
  e não é boa prática — o repositório guarda código, não dataset.
- Reprodutibilidade: os dados são públicos e baixáveis a qualquer momento na
  fonte oficial, então não há motivo para duplicá-los aqui.

### Como baixar

Baixe os datasets na fonte oficial do IMDB: https://datasets.imdbws.com/

Selecione os arquivos `title.basics.tsv.gz` e `title.ratings.tsv.gz`, descompacte e
coloque-os na raiz do projeto renomeados como `title_basics.tsv` e
`title_ratings.tsv`.

## Estrutura

imdb-spark/
├── imdb_analisys.ipynb # notebook com as análises (questões resolvidas)
├── title_basics.tsv # (não versionado — baixar)
├── title_ratings.tsv # (não versionado — baixar)
├── .gitignore
├── LICENSE
└── README.md


## Requisitos

- Python 3.11+
- Apache Spark 4.x / PySpark
- Jupyter

```bash
pip install pyspark jupyter
```

## Como executar

Abra o `imdb_analisys.ipynb` em um ambiente com suporte a Jupyter (VS Code com a
extensão Python/Jupyter, JupyterLab ou Jupyter Notebook) e execute as células.

Se for usar o Jupyter pela linha de comando:

```bash
pip install notebook   # ou: pip install jupyterlab
jupyter notebook imdb_analisys.ipynb
```

A `SparkSession` fica ativa entre as células — os arquivos são lidos uma vez e
cada questão roda de forma independente.

## Observações técnicas

- Os arquivos são TSV (separador `\t`) e usam `\N` como marcador de nulo, tratado
  na leitura com `nullValue="\\N"`.
- `df_titles` e `df_ratings` são unidos por `tconst` (join inner) quando a análise
  depende da nota; consultas sobre o catálogo completo usam `df_titles`
  diretamente, para não perder títulos sem avaliação.
- Alguns enunciados usam "filme" de forma ampla; onde a consulta abrange todos os
  `titleType` do IMDB (não só `movie`), o termo foi tratado como "título".

## Licença

MIT - veja o arquivo LICENSE.
