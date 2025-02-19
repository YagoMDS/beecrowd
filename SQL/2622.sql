/*O setor de vendas quer fazer uma promoção para todos os clientes que são pessoas jurídicas. 
 Para isso você deve exibir o nome dos clientes que sejam pessoa jurídica.*/
SELECT
    c.name
FROM
    customers AS c
    LEFT JOIN legal_person AS leg ON leg.id_customers = c.id
WHERE
    leg.cnpj IS NOT NULL