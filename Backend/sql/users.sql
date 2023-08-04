CREATE TABLE tipo_usuario (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL
);

CREATE TABLE permissoes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  tipo_usuario_id INT,
  permissao VARCHAR(255) NOT NULL,
  FOREIGN KEY (tipo_usuario_id) REFERENCES tipo_usuario(id)
);

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  tipo_usuario_id INT,
  FOREIGN KEY (tipo_usuario_id) REFERENCES tipo_usuario(id);
);
