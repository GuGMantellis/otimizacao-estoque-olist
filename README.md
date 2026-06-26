# 📦 Análise de Estoque e Previsão de Demanda com Python

Esse projeto nasceu de uma dúvida bem prática: **como usar dados históricos de vendas para tomar decisões melhores de estoque?**

Peguei a base pública da Olist (mais de 100 mil pedidos reais do e-commerce brasileiro) e construí uma análise completa — desde a limpeza dos dados até uma previsão de demanda com Machine Learning.

---

## O que esse projeto faz

- **Entende os dados**: carrega e inspeciona as tabelas de pedidos, produtos e clientes
- **Limpa o que precisa ser limpo**: datas, valores nulos, pedidos cancelados
- **Curva ABC**: classifica as categorias de produtos por receita (quem gera 80% do faturamento?)
- **Sazonalidade**: mostra como as vendas variam ao longo do tempo e da semana
- **Previsão**: usa o Prophet (biblioteca da Meta) pra projetar os próximos 60 dias de demanda
- **Conclusões**: ao final tem um relatório com recomendações práticas pra gestão de estoque

---

## Tecnologias usadas

| Biblioteca | Pra quê |
|-----------|---------|
| `pandas` | Manipulação e limpeza dos dados |
| `numpy` | Cálculos numéricos |
| `matplotlib` | Geração dos gráficos |
| `seaborn` | Estilo visual dos gráficos |
| `prophet` | Previsão de séries temporais |

---

## Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/guguemantellis/otimizacao-estoque-olist.git
cd otimizacao-estoque-olist
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Recomendo criar um ambiente virtual antes:
> ```bash
> python -m venv .venv
> .venv\Scripts\activate   # Windows
> ```

### 3. Baixe o dataset

O dataset é público e gratuito no Kaggle:

👉 [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Depois de baixar, extrai os `.csv` na pasta `data/` do projeto.

### 4. Rode o notebook

```bash
jupyter notebook analise_estoque_olist.ipynb
```

Executa as células de cima pra baixo. Os gráficos e CSVs de resultado vão aparecer na pasta `output/` automaticamente.

---

## Estrutura

```
📁 projeto/
├── analise_estoque_olist.ipynb   ← notebook principal
├── requirements.txt
├── setup.py                      ← instala deps e cria as pastas
├── data/                         ← coloque os CSVs do Kaggle aqui
└── output/                       ← gerado ao rodar o notebook
    ├── 01_faturamento_mensal.png
    ├── 02_vendas_por_dia.png
    ├── 03_curva_abc.png
    ├── 04_top_categorias_a.png
    ├── 05_previsao_prophet.png
    ├── 06_componentes_sazonalidade.png
    ├── curva_abc_completa.csv
    └── previsao_demanda.csv
```

---

## Dataset

**Brazilian E-Commerce Public Dataset by Olist**  
Dados reais de pedidos realizados no Brasil entre 2016 e 2018.  
Licença: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

## Resultados

Alguns dos insights que esse projeto consegue gerar:

- Quais categorias de produto concentram a maior parte da receita (Curva ABC)
- Em quais épocas do ano a demanda tende a aumentar ou cair
- Uma projeção quantitativa de demanda para os próximos 60 dias com intervalo de confiança

Esses resultados podem ser usados diretamente pra orientar compras, negociação com fornecedores e gestão de estoque.
