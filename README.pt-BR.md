[🇺🇸 English Version](README.md)

# 🏙️ Análise de Preços no Airbnb — Nova York

## Sobre o Projeto

Este projeto apresenta uma **Análise Exploratória de Dados (EDA)** completa das listagens do Airbnb na cidade de Nova York. O objetivo principal é compreender os principais fatores que influenciam os preços das listagens e identificar padrões relevantes relacionados ao tipo de acomodação, localização, avaliações e disponibilidade.

Além da análise em notebook, o projeto inclui um **dashboard interativo desenvolvido com Streamlit**, permitindo que os usuários explorem o dataset por meio de filtros e visualizações.

Este projeto foi desenvolvido não apenas como exercício técnico, mas também como um **projeto de portfólio** com foco em demonstrar habilidades analíticas práticas, narrativa com dados e organização de projeto.

---

## 💼 Contexto de Negócio

A precificação é uma das variáveis mais importantes em marketplaces de aluguel de curta duração. Entender como os preços das listagens variam por região, tipo de acomodação, volume de avaliações e disponibilidade pode apoiar melhores decisões estratégicas para anfitriões, analistas e stakeholders do marketplace.

Esta análise busca responder perguntas práticas como:

- Quais tipos de acomodação têm preços mais altos?
- Quais áreas de Nova York concentram as listagens premium?
- Listagens com muitas avaliações estão associadas a preços mais baixos ou mais altos?
- Como a disponibilidade da listagem se relaciona com o comportamento dos preços?
- Quais bairros se destacam em termos de preço médio?

---

## 🎯 Objetivo

Analisar os dados de listagens do Airbnb para identificar padrões de precificação e gerar insights de negócio a partir do dataset.

---

## 📂 Dataset

| Campo | Detalhes |
|---|---|
| **Fonte** | New York City Airbnb Open Data |
| **Arquivo original** | `AB_NYC_2019.csv` |
| **Arquivo processado** | `airbnb_cleaned.csv` |

---

## 🛠️ Ferramentas e Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Pillow

---

## 📁 Estrutura do Projeto

```bash
airbnb-price-analysis
│
├── app.py
├── README.md
├── README.pt-BR.md
├── requirements.txt
├── .gitignore
│
├── data
│   ├── raw
│   │   └── AB_NYC_2019.csv
│   └── processed
│       └── airbnb_cleaned.csv
│
├── images
│   ├── correlacao.png
│   ├── distribuicao_precos.png
│   ├── mapa_geografico_precos.png
│   ├── nyc_map.jpg
│   ├── outliers_preco.png
│   ├── preco_por_regiao.png
│   ├── preco_por_tipo.png
│   ├── reviews_vs_preco.png
│   └── top10_bairros_preco.png
│
└── notebooks
    └── airbnb_eda.ipynb
```

---

## 🔄 Fluxo do Projeto

O projeto foi desenvolvido nas seguintes etapas:

1. Carregamento dos dados
2. Entendimento dos dados e inspeção inicial
3. Limpeza e pré-processamento dos dados
4. Análise exploratória dos dados
5. Visualização das principais variáveis e relações
6. Geração de insights de negócio
7. Criação do dashboard interativo com Streamlit

---

## 🧹 Preparação dos Dados

A etapa de pré-processamento incluiu:

- Inspeção dos tipos de dados
- Tratamento de valores ausentes
- Remoção de colunas irrelevantes
- Tratamento de valores extremos para análise de preços
- Criação de um dataset limpo para análise e uso no dashboard

---

## ❓ Principais Perguntas da Análise

- Qual tipo de acomodação tem o maior preço médio?
- Quais regiões concentram as listagens mais caras?
- Existe relação entre preço e número de avaliações?
- Como a disponibilidade se relaciona com os preços das listagens?
- Quais bairros têm os maiores preços médios?

---

## 🔍 Análises Exploratórias Principais

### 1. Distribuição de Preços
Uma análise de distribuição foi utilizada para entender o comportamento geral dos preços das listagens e identificar padrões de assimetria e concentração.

### 2. Identificação de Outliers
Boxplots foram utilizados para identificar valores extremos na variável de preço e melhorar a qualidade da análise visual.

### 3. Preço por Tipo de Acomodação
Uma análise comparativa dos preços das listagens por `room_type` foi realizada para avaliar como o tipo de acomodação afeta a precificação.

### 4. Preço Médio por Região
Os preços médios foram analisados por `neighbourhood_group` para destacar os bairros mais caros.

### 5. Avaliações vs. Preço
Uma análise de dispersão foi utilizada para inspecionar a relação entre a popularidade das listagens e os níveis de preço.

### 6. Distribuição Geográfica de Preços
As listagens foram plotadas geograficamente sobre um mapa de Nova York para visualizar a concentração espacial de preços.

### 7. Top Bairros por Preço Médio
Um ranking por bairro foi criado para identificar clusters de precificação premium em nível local.

---

## 💡 Principais Insights

- Listagens do tipo **casa/apartamento inteiro** tendem a ter os maiores preços médios
- **Manhattan** concentra as listagens mais caras
- Listagens com **mais avaliações** tendem a apresentar padrões de preço mais competitivos
- **Localização** é um dos principais fatores de variação de preço
- A análise por bairro revela **diferenças significativas mesmo dentro do mesmo borough**

---

## 🚀 Extensões Analíticas Avançadas

### 1. Segmentação de Preço por Borough e Tipo de Quarto
Combinar ambas as dimensões para identificar como o comportamento de preços muda dentro de cada borough por tipo de acomodação.

### 2. Índice Premium por Bairro
Criar um índice premium comparando o preço médio de cada bairro com a média geral da cidade.

### 3. Preço por Estadia Mínima
Criar métricas derivadas como:
- `price_per_minimum_stay = price * minimum_nights`
- `price_per_night_minimum = price / minimum_nights`

### 4. Análise de Anfitriões Profissionais
Utilizar o número de listagens por anfitrião como proxy para identificar anfitriões comerciais ou profissionais.

### 5. Análise de Intensidade de Avaliações
Segmentar listagens por categorias de volume de avaliações ou quartis e comparar preços médios.

### 6. Segmentação por Disponibilidade
Criar faixas de disponibilidade e comparar preços entre grupos de baixa, média e alta disponibilidade.

### 7. Análise Numérica com Foco em Correlação
Expandir a análise de relações numéricas envolvendo preço, disponibilidade, noites mínimas e atividade de avaliações.

---

## 📊 Dashboard

O projeto inclui um **dashboard interativo desenvolvido com Streamlit**. Os usuários podem filtrar listagens por região, tipo de acomodação, faixa de preço, número de avaliações e disponibilidade.

### Principais Funcionalidades do Dashboard

- Cards de KPI com métricas resumidas
- Visualização da distribuição de preços
- Preço por tipo de acomodação
- Preço médio por região
- Análise de avaliações vs. preço
- Distribuição geográfica das listagens no mapa de NYC
- Top 10 bairros por preço médio
- Tabela de dados filtrados com opção de download em CSV

---

## 📓 Notebook

A versão em notebook da análise está disponível em:

```
notebooks/airbnb_eda.ipynb
```

Contém:

- Inspeção do dataset
- Etapas de pré-processamento
- Análise exploratória
- Visualizações
- Conclusões e insights de negócio

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/Jp98-dev/airbnb-price-analysis.git
```

### 2. Entrar na pasta do projeto
```bash
cd airbnb-price-analysis
```

### 3. Criar e ativar um ambiente virtual
```bash
python -m venv .venv
```

**No Windows:**
```bash
.venv\Scripts\activate
```

**No macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 5. Executar o dashboard Streamlit
```bash
streamlit run app.py
```

---

## ✅ Resultados

Este projeto demonstra habilidades práticas em:

- Limpeza de dados
- Análise exploratória de dados
- Raciocínio orientado a features
- Geração de insights de negócio
- Visualização de dados
- Desenvolvimento de dashboards
- Organização de projeto para apresentação em portfólio

---

## 🔮 Melhorias Futuras

Possíveis próximos passos para este projeto incluem:

- Implementar as extensões analíticas avançadas listadas acima
- Adicionar resumos estatísticos mais ricos
- Melhorar o layout e o acabamento visual do dashboard
- Fazer o deploy do app Streamlit online
- Expandir a análise com modelagem preditiva

---

## 👤 Autor

**João Paulo Araújo Maciel**