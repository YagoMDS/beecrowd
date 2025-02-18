/*O setor de importação da nossa empresa precisa de um relatório sobre a importação de
 produtos do nosso fornecedor Sansul.
 
 Sua tarefa é exibir o nome dos produtos, o nome do fornecedor e o nome da categoria,
 para os produtos fornecidos pelo fornecedor ‘Sansul SA’ e cujo nome da categoria seja 'Imported'.
 */
SELECT
    prod.name,
    prov.name,
    cat.name
FROM
    products as prod
    INNER JOIN providers as prov ON prov.id = prod.id_providers
    INNER JOIN categories as cat ON cat.id = prod.id_categories
WHERE
    prov.name = 'Sansul SA'
    and cat.name = 'Imported'