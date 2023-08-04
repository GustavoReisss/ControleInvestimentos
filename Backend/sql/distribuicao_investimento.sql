CREATE TABLE distribuicao_investimento (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  tipo_investimento_id INT,
  porcentagem DECIMAL(5, 2),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (tipo_investimento_id) REFERENCES tipo_investimento(id)
);
