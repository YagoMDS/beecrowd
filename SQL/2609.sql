/*Como de costume o setor de vendas está fazendo uma análise de quantos produtos temos em estoque, 
e você poderá ajudar eles.

Então seu trabalho será exibir o nome e a quantidade de produtos de cada uma categoria.*/

SELECT
    c.name,
    sum(amount)
FROM
    products as p
    INNER JOIN categories as c ON p.id_categories = c.id
WHERE
    p.id_categories > 0
GROUP BY
    c.name