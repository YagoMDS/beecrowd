/*Quando os dados foram migrados de Banco de Dados, houve um pequeno mal-entendido por parte do antigo DBA.

Seu chefe precisa que você exiba o código e o nome dos produtos, cuja categoria inicie com 'super'.*/

select
    p.id,
    p.name
from
    products p
    inner join categories c on c.id = p.id_categories
where
    c.name like 'super%'