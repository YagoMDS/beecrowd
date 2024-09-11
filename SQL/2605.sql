select 
    p.name,
    n.name
from 
    products p
inner join categories c
on c.id = p.id_categories
inner join providers n
on n.id = p.id_providers

where id_categories = 6