/*O setor financeiro precisa de um relatório sobre os fornecedores dos produtos que vendemos.
Os relatórios contemplam todas as categorias, mas por algum motivo, os fornecedores dos produtos
cuja categoria é a executiva, não estão no relatório.

Seu trabalho é retornar os nomes dos produtos e dos fornecedores cujo código da categoria é 6.*/

select
    p.name,
    n.name
from
    products p
    inner join categories c on c.id = p.id_categories
    inner join providers n on n.id = p.id_providers
where
    id_categories = 6