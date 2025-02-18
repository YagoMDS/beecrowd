/*A vídeo locadora está fazendo seu relatório semestral e precisa da sua ajuda.
 Basta você selecionar o nome dos clientes e a data de locação, das locações realizadas
 no mês de setembro de 2016.*/

SELECT
    c.name,
    r.rentals_date
FROM
    customers as c
    INNER JOIN rentals as r ON c.id = r.id_customers
WHERE
    r.rentals_date > '2016-09-01'
    AND r.rentals_date < '2016-09-30'