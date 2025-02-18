/*O setor financeiro encontrou alguns problemas na entrega de um dos nossos fornecedores, 
a entrega dos produtos não condiz com a nota fiscal.
 
 Seu trabalho é exibir o nome dos produtos e o nome do fornecedor, para os produtos fornecidos
pelo fornecedor ‘Ajax SA’.
 */
SELECT
    prd.name,
    prv.name
FROM
    providers as prv
    INNER JOIN products as prd ON prd.id_providers = prv.id
WHERE
    prv.name = 'Ajax SA'