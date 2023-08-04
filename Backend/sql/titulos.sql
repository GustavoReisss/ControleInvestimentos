CREATE TABLE titulos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  tipo_titulo_id INT NOT NULL,
  descricao VARCHAR(255) NOT NULL,
  data_insercao DATE NOT NULL,
  quantidade DECIMAL(10,2) NOT NULL,
  data_vencimento DATE NOT NULL,
  valor_aplicado DECIMAL(10,2) NOT NULL,
  valor_bruto DECIMAL(10,2) NOT NULL,
  valor_liquido DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (tipo_titulo_id) REFERENCES tipo_titulo(id)
);