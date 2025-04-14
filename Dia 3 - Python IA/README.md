# Projeto: Classificação de Score de Crédito com Inteligência Artificial

Este projeto tem como objetivo desenvolver um modelo de Inteligência Artificial capaz de classificar o score de crédito de clientes em três categorias: **Ruim**, **Ok** e **Bom**. A iniciativa foi concebida para auxiliar instituições financeiras na avaliação de risco de crédito de seus clientes.

## Objetivos

- Analisar dados de clientes para identificar padrões que influenciam o score de crédito.
- Preparar os dados para treinamento de modelos de Machine Learning.
- Treinar e comparar diferentes modelos de classificação.
- Utilizar o modelo mais eficaz para prever o score de crédito de novos clientes.

## Tecnologias Utilizadas

- Python 3.x
- pandas
- scikit-learn

## Estrutura do Projeto

- `clientes.csv`: Base de dados com informações históricas de clientes e seus respectivos scores de crédito.
- `novos_clientes.csv`: Conjunto de dados com informações de novos clientes para os quais o score de crédito será previsto.
- `inicial.ipynb`: Notebook contendo todo o processo de análise, treinamento e previsão.

## Etapas do Projeto

1. **Importação e Visualização dos Dados**
   - Leitura dos dados utilizando pandas.
   - Visualização inicial para compreensão das variáveis disponíveis.

2. **Pré-processamento dos Dados**
   - Codificação de variáveis categóricas (`profissao`, `mix_credito`, `comportamento_pagamento`) utilizando `LabelEncoder`.
   - Separação dos dados em variáveis independentes (features) e dependente (target).

3. **Divisão dos Dados**
   - Separação dos dados em conjuntos de treino e teste utilizando `train_test_split`.

4. **Treinamento dos Modelos**
   - Treinamento de dois modelos de classificação: `RandomForestClassifier` e `KNeighborsClassifier`.

5. **Avaliação dos Modelos**
   - Avaliação da acurácia de cada modelo utilizando `accuracy_score`.
   - Seleção do modelo com melhor desempenho para previsões futuras.

6. **Previsão para Novos Clientes**
   - Aplicação do modelo selecionado para prever o score de crédito de novos clientes.
   - Adição das previsões à base de dados dos novos clientes.

## Resultados Esperados

Espera-se que o modelo treinado seja capaz de classificar corretamente o score de crédito dos clientes, auxiliando na tomada de decisões relacionadas à concessão de crédito e gerenciamento de risco.

## Contribuições

Contribuições são bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões de melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

*Nota: Os dados utilizados neste projeto são fictícios e destinados apenas para fins educacionais.*

---
