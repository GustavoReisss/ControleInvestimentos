SELECT `t2`.`id`, `t1`.`descricao`, `t1`.`id`, coalesce(`t2`.`porcentagem`, 0)
FROM `tipos_investimentos` `t1`, (
    SELECT `d`.*
    FROM `distribuicao_investimento` `d`
    WHERE `d`.`user_id` = %s
    ) `t2`
