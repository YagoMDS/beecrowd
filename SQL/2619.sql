/*A nossa empresa está querendo fazer um novo contrato para o fornecimento de novos produtos
 superluxuosos, e para isso precisamos de alguns dados dos nossos produtos.
 
 Seu trabalho é exibir o nome dos produtos, nome dos fornecedores e o preço, 
 para os produtos cujo preço seja maior que 1000 e sua categoria seja ‘Super Luxury.
 */
SELECT
    prd.name,
    prv.name,
    prd.price
FROM
    products as prd
    INNER JOIN providers as prv ON prv.id = prd.id_providers
    INNER JOIN categories as cat ON cat.id = prd.id_categories
WHERE
    prd.price > 1000
    and cat.name = 'Super Luxury'