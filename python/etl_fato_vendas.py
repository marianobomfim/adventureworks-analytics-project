"""
Projeto: Análise de Vendas - AdventureWorks
Autor: Mariano Bomfim
Descrição:
Script ETL responsável por:
- Extrair dados do SQL Server (AdventureWorks)
- Aplicar regras de negócio
- Criar a tabela dbo.fato_vendas_analitica
"""

import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# Conexão com SQL Server
# -------------------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=AdventureWorks2022;"
    "Trusted_Connection=yes;"
)

engine = create_engine(
    "mssql+pyodbc://localhost/AdventureWorks2022"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# -------------------------
# Query SQL
# -------------------------
query = """
SELECT
    soh.SalesOrderID,
    sod.SalesOrderDetailID,
    soh.OrderDate,

    c.CustomerID,
    p.FirstName + ' ' + p.LastName AS Cliente,

    pr.ProductID,
    pr.Name AS Produto,
    pc.Name AS Categoria,
    psc.Name AS Subcategoria,

    sod.OrderQty,
    sod.UnitPrice,
    sod.LineTotal
FROM Sales.SalesOrderDetail sod
INNER JOIN Sales.SalesOrderHeader soh
    ON sod.SalesOrderID = soh.SalesOrderID
INNER JOIN Production.Product pr
    ON sod.ProductID = pr.ProductID
LEFT JOIN Production.ProductSubcategory psc
    ON pr.ProductSubcategoryID = psc.ProductSubcategoryID
LEFT JOIN Production.ProductCategory pc
    ON psc.ProductCategoryID = pc.ProductCategoryID
INNER JOIN Sales.Customer c
    ON soh.CustomerID = c.CustomerID
LEFT JOIN Person.Person p
    ON c.PersonID = p.BusinessEntityID
"""

# -------------------------
# Extração
# -------------------------
df = pd.read_sql(query, conn)

# -------------------------
# Transformações
# -------------------------
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Ano'] = df['OrderDate'].dt.year
df['Mes'] = df['OrderDate'].dt.month
df['AnoMes'] = df['OrderDate'].dt.strftime('%Y-%m')

df['Venda_Alta'] = df['LineTotal'] > 1000
df['Pedido_Grande'] = df['OrderQty'] >= 10
df['Valor_Unitario_Medio'] = df['LineTotal'] / df['OrderQty']
df['Categoria'] = df['Categoria'].str.upper().str.strip()

# -------------------------
# Carga
# -------------------------
df.to_sql(
    name='fato_vendas_analitica',
    con=engine,
    schema='dbo',
    if_exists='replace',
    index=False
)

conn.close()

print("ETL finalizado com sucesso!")

