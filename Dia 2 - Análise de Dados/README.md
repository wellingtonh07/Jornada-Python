# Análise de Cancelamentos de Clientes

Este projeto realiza uma análise exploratória de dados (EDA) para identificar os principais fatores que levam ao cancelamento de clientes em uma empresa de telecomunicações. Utilizando Python e bibliotecas como pandas e Plotly, buscamos entender padrões de comportamento e propor ações para reduzir o churn.

## Objetivos

- Importar e limpar a base de dados de cancelamentos.
- Visualizar e compreender as informações disponíveis.
- Identificar problemas e inconsistências nos dados.
- Analisar a taxa de cancelamento e os fatores que a influenciam.
- Propor soluções para reduzir o churn com base nos insights obtidos.

## Tecnologias Utilizadas

- Python 3.x
- pandas
- Plotly
- Jupyter Notebook

## Estrutura do Projeto

- `cancelamentos_sample.csv` — Base de dados com informações sobre os clientes e seus status de cancelamento.
- `inicial.ipynb` — Notebook contendo todo o processo de análise e visualização dos dados.
- `README.md` — Este arquivo, com informações sobre o projeto.

## Etapas da Análise

1. **Importação e Visualização dos Dados**
   - Leitura da base de dados utilizando pandas.
   - Remoção de colunas irrelevantes, como `CustomerID`.
   - Visualização inicial para compreensão das informações disponíveis.

2. **Limpeza dos Dados**
   - Identificação e remoção de valores nulos.
   - Correção de formatos inadequados em colunas específicas.

3. **Análise Exploratória**
   - Cálculo da taxa de cancelamento geral.
   - Geração de gráficos interativos para cada variável, segmentando por status de cancelamento.
   - Identificação de padrões, como:
     - Clientes com mais de 4 ligações para o call center têm maior probabilidade de cancelar.
     - Clientes com contratos mensais apresentam maior taxa de cancelamento.
     - Atrasos superiores a 20 dias estão correlacionados com cancelamentos.

4. **Propostas de Ação**
   - Implementar alertas para clientes que ligam frequentemente para o call center.
   - Oferecer incentivos para migração de contratos mensais para anuais.
   - Estabelecer notificações para clientes com atrasos superiores a 10 dias.

5. **Reavaliação da Taxa de Cancelamento**
   - Após aplicar os filtros baseados nas propostas de ação, a taxa de cancelamento é recalculada para avaliar a eficácia das medidas sugeridas.

## Resultados Esperados

Através da implementação das ações propostas, espera-se uma redução significativa na taxa de cancelamento, melhorando a retenção de clientes e aumentando a receita da empresa.

## Contribuições

Contribuições são bem-vindas! Se você deseja sugerir melhorias ou reportar problemas, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

*Nota: A base de dados utilizada neste projeto é uma amostra fictícia para fins educacionais.*

---
