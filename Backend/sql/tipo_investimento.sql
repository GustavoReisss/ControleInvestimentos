CREATE TABLE tipos_investimentos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  descricao VARCHAR(255) NOT NULL,
  descricao_abreviada VARCHAR(50) NOT NULL
);

INSERT INTO tipos_investimentos (descricao, descricao_abreviada)
VALUES ('Ações Nacionais', 'AN'),
       ('Ações Internacionais', 'AI'),
       ('Fundos Imobiliários', 'FI'),
       ('Renda Fixa', 'RF');


CREATE TABLE tipos_titulos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tipo_investimento_id INT,
  descricao VARCHAR(255) NOT NULL,
  FOREIGN KEY (tipo_investimento_id) REFERENCES tipos_investimentos(id)
);

-- Renda Fixa
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'CDB');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'LC');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'LCA');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'LCI');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'Tesouro Direto');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'Debêntures');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'CRI');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'CRA');
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Renda Fixa'), 'LF');

-- Ações Nacionais
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Ações Nacionais'), 'Ação');

-- Fundos Imobiliários
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Fundos Imobiliários'), 'FII');

-- Ações Internacionais
INSERT INTO tipos_titulos (tipo_investimento_id, descricao) VALUES ((SELECT id FROM tipos_investimentos WHERE descricao = 'Ações Internacionais'), 'BDR');