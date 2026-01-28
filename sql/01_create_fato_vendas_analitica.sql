SELECT
	soh.SalesOrderID,
	sod.SalesOrderDetailId,
	soh.OrderDate,
	YEAR(soh.OrderDate) AS Ano,
	MONTH(soh.OrderDate) as Mes,
	
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
