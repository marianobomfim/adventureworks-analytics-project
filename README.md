# 📊 Projeto de Análise de Vendas – AdventureWorks

Projeto de análise de dados utilizando **SQL Server**, **Python** e **Power BI**, com foco em modelagem analítica, ETL e visualização de dados para apoio à tomada de decisão.

---

## 🎯 Objetivo do Projeto

Construir uma base analítica de vendas a partir do banco **AdventureWorks**, aplicando regras de negócio e disponibilizando os dados para consumo direto no **Power BI**.

O projeto simula um cenário real de mercado, onde dados transacionais são transformados em uma tabela analítica para relatórios gerenciais e análises exploratórias.

---

## 🏗️ Arquitetura da Solução

**Fonte de Dados**
- SQL Server (AdventureWorks2022)

**ETL**
- SQL: joins e extração dos dados transacionais
- Python (Pandas + SQLAlchemy):
  - Tratamento de dados
  - Criação de colunas calculadas
  - Regras de negócio
  - Carga da tabela analítica

**Camada Analítica**
- Tabela: `dbo.fato_vendas_analitica`

**Visualização**
- Power BI conectado diretamente ao SQL Server

---

## 🗂️ Estrutura do Repositório



📁 projeto-de-analise-adventureworks
│
├── 📁 sql
│ └── query_fato_vendas.sql
│
├── 📁 python
│ └── etl_fato_vendas.py
│
├── 📁 powerbi
│ └── dashboard_vendas.pbix
│
└── README.md


---

## 📐 Regras de Negócio Aplicadas

- Identificação de vendas de alto valor (`Venda_Alta`)
- Identificação de pedidos grandes (`Pedido_Grande`)
- Criação de campo `AnoMes` para análises temporais
- Cálculo do valor unitário médio por item
- Padronização de categorias

---

## 📊 Dashboards Desenvolvidos

- Visão geral de faturamento
- Participação por categoria e subcategoria
- Top produtos por faturamento
- Top clientes
- Página analítica com filtros dinâmicos

*(Imagens do dashboard disponíveis na pasta `/powerbi`)*

---

## 🚀 Tecnologias Utilizadas

- SQL Server
- Python
  - Pandas
  - PyODBC
  - SQLAlchemy
- Power BI

---

### Visualização de Dados
- Power BI conectado via Direct Lake
- Modelo semântico leve (PBIX sem carga de dados)
- Dados consumidos diretamente da camada analítica no SQL Server / Lakehouse


📌 Projeto desenvolvido como parte do meu processo de evolução em Engenharia e Análise de Dados, aplicando práticas reais utilizadas em ambientes corporativos.


## 👤 Autor

**Mariano Bomfim**  
Analista de Dados | SQL | Python | Power BI  






