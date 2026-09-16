# Classificação de Risco de FIAGRO utilizando Machine Learning

Projeto desenvolvido como Trabalho de Conclusão de Curso em Ciência da Computação na UTFPR, com o objetivo de investigar o uso de algoritmos de Machine Learning para classificação de risco de fundos FIAGRO negociados na B3.

O trabalho envolve desde a coleta e preparação dos dados financeiros até o treinamento, comparação e avaliação de diferentes modelos de classificação.

---

## Objetivo

Desenvolver uma abordagem baseada em Machine Learning capaz de classificar FIAGROs em três níveis de risco:

- Baixo
- Médio
- Alto

A classificação utiliza indicadores financeiros e métricas de risco extraídas de dados públicos dos fundos.

O objetivo principal foi avaliar se algoritmos de aprendizado supervisionado conseguem identificar padrões associados ao risco dos ativos e comparar o desempenho de diferentes técnicas de classificação.

---

## Modelos avaliados

Durante o projeto foram testados diferentes algoritmos de Machine Learning:

- Random Forest
- Support Vector Machine (SVM)
  - Kernel linear
  - Kernel RBF
- Multi-Layer Perceptron (MLP)
- k-Nearest Neighbors (k-NN)
- Naive Bayes

Entre os modelos avaliados, o Random Forest apresentou o melhor desempenho geral nos experimentos realizados.

---

## Definição do risco

O nível de risco dos fundos foi construído utilizando três métricas:

- Beta (β)
- Drawdown
- Variância

Essas métricas foram combinadas para gerar uma medida de risco utilizada posteriormente para dividir os ativos em três classes:

```text
Baixo
Médio
Alto
````

Essa classificação foi utilizada como variável alvo dos modelos supervisionados.

---

## Pipeline do projeto

O fluxo geral utilizado no trabalho foi:

```text
Dados públicos da B3
        ↓
Coleta e organização dos dados
        ↓
Construção dos indicadores financeiros
        ↓
Tratamento de valores extremos
        ↓
Análise de correlação
        ↓
Seleção de atributos
        ↓
Balanceamento das classes
        ↓
Normalização
        ↓
Treinamento dos modelos
        ↓
Avaliação e comparação
```

---

## Pré-processamento

O projeto utiliza diferentes técnicas de preparação dos dados antes do treinamento dos modelos.

### Tratamento de outliers

Valores extremos foram tratados utilizando o método IQR (Interquartile Range).

O objetivo foi reduzir a influência de observações muito distantes da distribuição principal dos dados.

### Balanceamento das classes

Como a distribuição dos níveis de risco não era necessariamente equilibrada, foi utilizado:

* SMOTE — Synthetic Minority Over-sampling Technique

O SMOTE gera novas amostras sintéticas das classes minoritárias para reduzir o viés do modelo em direção à classe dominante.

### Normalização

Algoritmos sensíveis à escala dos atributos utilizaram dados normalizados antes do treinamento.

Isso é particularmente importante para modelos como:

* SVM
* k-NN
* MLP

---

## Seleção de atributos

Para reduzir atributos pouco relevantes ou redundantes foram utilizadas diferentes estratégias.

### Correlação de Pearson

Foi analisada a relação entre os indicadores e a variável de risco.

Um critério utilizado durante os experimentos considerou atributos com:

```text
|r| > 0.30
```

Alguns indicadores apresentaram correlação relevante com o risco analisado.

### Recursive Feature Elimination

Também foi utilizado RFE (Recursive Feature Elimination) para selecionar subconjuntos de atributos considerados mais relevantes para os modelos.

O processo remove progressivamente atributos com menor contribuição até atingir o conjunto desejado.

---

## Random Forest

O Random Forest foi um dos principais modelos avaliados no projeto.

Uma das configurações utilizadas nos experimentos foi:

```python
RandomForestClassifier(
    n_estimators=100
)
```

Além da capacidade de classificação, o modelo também foi utilizado para analisar:

* importância dos atributos;
* comportamento das árvores;
* variáveis mais relevantes para a classificação.

Algumas árvores individuais também foram exportadas para análise visual.

---

## Redes Neurais

Também foi avaliado um modelo baseado em Multi-Layer Perceptron (MLP).

O modelo foi utilizado para verificar se uma rede neural totalmente conectada conseguiria capturar relações não lineares entre os indicadores financeiros e as classes de risco.

Exemplo de resultados observados durante os experimentos:

| Classe | F1-score |
| ------ | -------: |
| Alto   |     0.51 |
| Médio  |     0.45 |
| Baixo  |     0.68 |

Acurácia aproximada:

```text
56%
```

Esses resultados ajudaram a comparar o comportamento da rede neural com os demais classificadores.

---

## Avaliação dos modelos

Os modelos foram avaliados utilizando métricas de classificação como:

* Accuracy
* Precision
* Recall
* F1-score
* Matriz de confusão

Foi dada atenção especial ao F1-score, pois a existência de classes desbalanceadas torna a acurácia isolada insuficiente para avaliar adequadamente o desempenho.

---

## Tecnologias utilizadas

### Linguagem

* Python

### Machine Learning

* Scikit-learn
* Imbalanced-learn
* TensorFlow / Keras
* PyTorch

### Manipulação de dados

* Pandas
* NumPy

### Visualização

* Matplotlib
* Seaborn

### Coleta de dados

* Selenium

---

## Estrutura do repositório

A organização atual do projeto contém diretórios destinados aos diferentes experimentos e modelos:

```text
tcc/
├── Arvore/
├── SVM/
├── assets/
├── src/
└── README.md
```

### `src/`

Contém os principais códigos responsáveis por:

* preparação dos dados;
* treinamento dos modelos;
* avaliação;
* geração de resultados.

### `Arvore/`

Arquivos relacionados aos experimentos com modelos baseados em árvores e visualização das árvores treinadas.

### `SVM/`

Experimentos relacionados aos classificadores Support Vector Machine.

### `assets/`

Arquivos auxiliares utilizados na documentação e apresentação dos resultados.

---

## Principais desafios

Alguns dos principais desafios encontrados durante o desenvolvimento foram:

* construção de uma métrica consistente de risco;
* coleta e organização de dados financeiros públicos;
* tratamento de dados heterogêneos;
* seleção de atributos relevantes;
* desbalanceamento das classes;
* comparação justa entre algoritmos com características diferentes;
* interpretação dos resultados produzidos pelos modelos.

---

## Conceitos explorados

O projeto permitiu aplicar conceitos de diferentes áreas da Ciência da Computação e Ciência de Dados:

* Machine Learning supervisionado
* Feature Engineering
* Feature Selection
* Data Cleaning
* Class Imbalance
* Redes Neurais
* Support Vector Machines
* Ensemble Learning
* Análise estatística
* Automação de coleta de dados
* Avaliação de modelos

---

## Contexto acadêmico

Projeto desenvolvido como Trabalho de Conclusão de Curso do Bacharelado em Ciência da Computação da Universidade Tecnológica Federal do Paraná — UTFPR.

O trabalho explora a aplicação de técnicas de Machine Learning na análise de risco de ativos financeiros ligados ao agronegócio.

---

## Autor

**Erik Silva Maia**

* GitHub: [@ErikMaia](https://github.com/ErikMaia)
* LinkedIn: [Erik Silva Maia](https://www.linkedin.com/in/erik-silva-maia/)

---

## Status

TCC concluído.

O repositório permanece disponível como registro dos experimentos, metodologia e resultados obtidos durante o desenvolvimento do trabalho.

```

Eu usaria essa versão. Ela combina melhor com um projeto acadêmico e ainda funciona bem como portfólio técnico.
```
