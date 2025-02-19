/*Os diretores do setor de comunicação da sua empresa querem um relatório sobre os dados
dos clientes físicos que estão cadastrados no banco de dados. Porem o antigo relatório teve
um problema. Os dados do CPF dos clientes vieram sem a máscara.

Por isso seu trabalho agora é selecionar todos os CPFs de todos os clientes, e aplicar
uma máscara sobre o retorno dos dados.

A máscara do CPF é parecida com: '000.000.000-00'.*/


SELECT
    n.id_customers,
    CONCAT(
        SUBSTRING(n.cpf FROM 1 FOR 3), '.', 
        SUBSTRING(n.cpf FROM 4 FOR 3), '.', 
        SUBSTRING(n.cpf FROM 7 FOR 3), '-', 
        SUBSTRING(n.cpf FROM 10 FOR 2)
    ) AS CPF
FROM
    natural_person AS n
INNER JOIN customers AS c ON c.id = n.id_customers

    