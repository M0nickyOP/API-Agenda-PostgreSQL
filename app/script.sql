CREATE TABLE contatos (
id SERIAL PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
telefone VARCHAR(20) NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE
);
CREATE INDEX ix_contatos_nome ON contatos (nome);

INSERT INTO contatos (nome, telefone, email) VALUES
('Ana', '11 9111-1111', 'ana@teste.com'),
('Bruno', '11 9222-2222', 'bruno@teste.com'),
('Carla', '11 9333-3333', 'carla@teste.com');

SELECT * FROM contatos;