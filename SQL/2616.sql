/*A locadora pretende fazer uma promoção para os clientes que ainda não fizeram nenhuma locação.

Seu trabalho é nos entregar o ID e o nome dos clientes que não realizaram nenhuma locação. 
Ordene a saída por ID.*/

SELECT 
    c.id,
    c.name
FROM
    customers as c 
LEFT JOIN 
    locations as l ON l.id_customers = c.id 
WHERE 
    l.locations_date IS NULL
ORDER BY 
    c.id